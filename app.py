from flask import Flask, render_template, request, redirect, url_for
import pyrebase
import os

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
    app.run(debug=True)