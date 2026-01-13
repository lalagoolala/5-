# ⭐ GitHub에서 배포하기 - 최종 실행 가이드

## 🎯 지금 바로 5단계만 하세요!

---

## **1️⃣ GitHub에 최종 코드 푸시** (2분)

```bash
cd "c:\Users\cyh99\Documents\프로젝트"
git add .
git commit -m "Setup GitHub deployment system"
git push origin main
```

---

## **2️⃣ GitHub Settings에서 Pages 비활성화** (1분)

1. https://github.com/lalagoola/home
2. **Settings** → **Pages**
3. **Source** → **"None"**
4. **Save**

---

## **3️⃣ GitHub에 Railway Token 추가** (3분)

### 3-1. Railway에서 Token 얻기

1. https://railway.app 로그인
2. 우측 상단 **Account** → **Settings**
3. **API Tokens** 찾기
4. **Create Token** 클릭
5. **복사** (아주 중요!)

### 3-2. GitHub에 Token 저장

1. https://github.com/lalagoola/home
2. **Settings** → **Secrets and variables** → **Actions**
3. **New repository secret** 클릭
4. 추가:
   ```
   Name: RAILWAY_TOKEN
   Value: (위에서 복사한 Token)
   ```
5. **Add secret**

---

## **4️⃣ Railway에 환경 변수 설정** (5분)

1. https://railway.app
2. 프로젝트 선택
3. **Variables** 탭
4. 아래 모두 추가:

```
FLASK_ENV=production
SECRET_KEY=health-app-secret-key
FIREBASE_API_KEY=AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k
FIREBASE_AUTH_DOMAIN=homepage-63d32.firebaseapp.com
FIREBASE_PROJECT_ID=homepage-63d32
FIREBASE_STORAGE_BUCKET=homepage-63d32.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=515012802016
FIREBASE_APP_ID=1:515012802016:web:4c3db8588aa7f00df8a785
FIREBASE_DATABASE_URL=https://homepage-63d32-default-rtdb.firebaseio.com
PORT=8080
```

---

## **5️⃣ GitHub Actions에서 배포 확인** (1분)

1. https://github.com/lalagoola/home
2. **Actions** 탭 클릭
3. 최신 "Deploy to Railway from GitHub" 보임
4. ✅ 초록색 체크 = 배포 완료!

---

## 🌐 **웹사이트 접속**

### 방법 1: GitHub에서 확인
1. 리포지토리 페이지
2. 우측 **Deployments** 클릭
3. URL 클릭 🌐

### 방법 2: Railway에서 확인
1. Railway 대시보드
2. 프로젝트 선택
3. Domains에서 URL 확인
4. 클릭 🌐

---

## 🎉 **완료!**

이제:
- ✅ GitHub에 코드 저장됨
- ✅ GitHub에서 배포 관리됨
- ✅ 코드 수정 → git push → 자동 배포
- ✅ GitHub Actions에서 배포 상태 확인
- ✅ GitHub Deployments에서 URL 확인

---

## 📝 **앞으로 코드 수정할 때마다**

```bash
# 1. 파일 수정

# 2. GitHub에 푸시
git add .
git commit -m "Update: (수정 내용)"
git push origin main

# 3. GitHub Actions가 자동으로 배포
# 4. Deployments에서 새로운 배포 확인
# 5. 웹사이트 새로고침해서 변경사항 확인
```

---

## 🎓 **교수님께 보고할 때**

리포지토리 링크: **https://github.com/lalagoola/home**

보여줄 것:
1. **Code 탭**: Flask 소스 코드
2. **Actions 탭**: 배포 자동화
3. **Deployments 탭**: 실제 배포됨 + URL
4. **웹사이트**: 실제 작동하는 홈페이지

---

**축하합니다! GitHub에서 배포되는 완벽한 웹 애플리케이션을 갖췄습니다!** 🚀🎊
