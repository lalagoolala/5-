from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import pyrebase
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

app = Flask(__name__)
# 보안을 위해 환경 변수에서 키를 가져오거나, 없을 경우 기본값을 사용합니다.
app.secret_key = os.environ.get('SECRET_KEY', 'health_class_secret_key')

# Firebase 설정 (제공된 정보 + databaseURL 추가)
firebaseConfig = {
  "apiKey": "AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k",
  "authDomain": "homepage-63d32.firebaseapp.com",
  "projectId": "homepage-63d32",
  "storageBucket": "homepage-63d32.firebasestorage.app",
  "messagingSenderId": "515012802016",
  "appId": "1:515012802016:web:4c3db8588aa7f00df8a785",
  "measurementId": "G-7YVL6MDXNJ",
  "databaseURL": "https://homepage-63d32-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# 관리자 계정 확인 및 생성 함수
def create_admin():
    users = db.child("users").get()
    admin_exists = False
    if users.val():
        for user in users.each():
            if user.val().get("username") == "abc":
                admin_exists = True
                break
    
    if not admin_exists:
        print("관리자 계정(abc)을 생성합니다.")
        db.child("users").push({"username": "abc", "password": "1234", "student_id": "관리자"})

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 회원가입
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        student_id = request.form['student_id'] # 예: 5학년 1반 3번
        
        data = {
            "username": username,
            "password": password,
            "student_id": student_id
        }
        db.child("users").push(data)
        return redirect(url_for('index'))
    return render_template('signup.html')

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Firebase에서 사용자 조회
        users = db.child("users").get()
        if users.val():
            for user in users.each():
                u = user.val()
                if u.get('username') == username and u.get('password') == password:
                    session['user'] = username
                    return redirect(url_for('index'))
        
        return render_template('login.html', error="아이디 또는 비밀번호가 틀렸습니다.")
    return render_template('login.html')

# 구글 로그인 처리 (자바스크립트에서 호출)
@app.route('/google_login', methods=['POST'])
def google_login():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    
    # DB에 사용자가 있는지 확인 (이메일 기준)
    users = db.child("users").get()
    user_exists = False
    if users.val():
        for user in users.each():
            if user.val().get("email") == email:
                user_exists = True
                break
    
    if not user_exists:
        # 구글 로그인으로 처음 접속한 경우 DB에 자동 저장
        new_user = {
            "username": username,
            "email": email,
            "student_id": "구글계정",
            "password": "google_oauth_user" # 비밀번호는 임의 설정
        }
        db.child("users").push(new_user)
        
    session['user'] = username
    return "success", 200

# 로그아웃
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

# 게시판 (공지사항 및 질의응답)
@app.route('/board/<board_type>')
def board(board_type):
    board_name = "공지사항" if board_type == 'notice' else "질의응답"
    
    # Firebase에서 데이터 가져오기
    posts_data = db.child("posts").get()
    posts = []
    
    if posts_data.val():
        for item in posts_data.each():
            val = item.val()
            if val.get("type") == board_type:
                # 템플릿 호환을 위해 튜플 형태로 변환 (제목, 작성자, 내용)
                posts.append((val.get("title"), val.get("author"), val.get("content")))
    
    return render_template('board.html', board_name=board_name, posts=posts, board_type=board_type)

if __name__ == '__main__':
    create_admin() # 앱 시작 시 관리자 계정 확인/생성
    app.run(debug=True)