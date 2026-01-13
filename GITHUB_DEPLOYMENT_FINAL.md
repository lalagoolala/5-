# 🚀 GitHub에서 직접 배포하기 (과제용)

## ✨ **GitHub에서 배포하는 완벽한 방법**

이제 **GitHub에 코드를 push하면 자동으로 웹사이트가 배포**됩니다!
과제 요구사항을 완벽하게 충족합니다!

---

## 📋 **설정 방법 (4단계)**

### **Step 1: GitHub에 Secrets 추가** ⭐ 매우 중요!

1. https://github.com/lalagoola/home 방문
2. **Settings** 클릭
3. 좌측 메뉴 → **Secrets and variables** → **Actions** 클릭
4. **"New repository secret"** 클릭
5. 다음 2개를 추가:

**Secret 1: RAILWAY_TOKEN**
```
Name: RAILWAY_TOKEN
Value: (Railway 대시보드에서 계정 설정 → API Token 복사)
```

**Secret 2: RAILWAY_PROJECT_ID**
```
Name: RAILWAY_PROJECT_ID
Value: (Railway 프로젝트 ID)
```

### **Step 2: Railway에서 API Token 얻기**

1. https://railway.app 로그인
2. 우측 상단 **Account** → **Settings** 클릭
3. **"API Tokens"** 찾기
4. **"Create Token"** 클릭
5. 생성된 토큰 **복사**
6. GitHub의 Step 1에서 RAILWAY_TOKEN에 붙여넣기

### **Step 3: 환경 변수 설정 (Railway)**

Railway 대시보드에서:

1. 프로젝트 선택
2. **Variables** 탭
3. 아래 환경 변수 모두 추가:

```
FLASK_ENV=production
SECRET_KEY=your-secret-key-12345
FIREBASE_API_KEY=AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k
FIREBASE_AUTH_DOMAIN=homepage-63d32.firebaseapp.com
FIREBASE_PROJECT_ID=homepage-63d32
FIREBASE_STORAGE_BUCKET=homepage-63d32.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=515012802016
FIREBASE_APP_ID=1:515012802016:web:4c3db8588aa7f00df8a785
FIREBASE_DATABASE_URL=https://homepage-63d32-default-rtdb.firebaseio.com
PORT=8080
```

### **Step 4: GitHub에 코드 최종 푸시**

```bash
cd "c:\Users\cyh99\Documents\프로젝트"

git add .
git commit -m "Setup GitHub auto deployment - final version"
git push origin main
```

---

## 🎉 **완료! 이제 자동 배포됨**

### GitHub에서 배포 상태 확인:

1. https://github.com/lalagoola/home 방문
2. **Actions** 탭 클릭
3. 최신 workflow 보기
4. "Deploy to Railway from GitHub" 실행 중 확인 ✅
5. 초록색 체크 = 배포 완료! ✨

### Deployments 확인:

1. GitHub 리포지토리 페이지
2. 우측 **"Deployments"** 클릭
3. **"production"** 환경에서 배포 상태 확인
4. 배포된 URL 클릭해서 웹사이트 방문 🌐

---

## 🔄 **이제 코드만 수정해서 push 하면 됨!**

```bash
# 파일 수정
# (예: templates/index.html 디자인 변경)

# GitHub에 푸시
git add .
git commit -m "Update homepage"
git push origin main

# 자동으로:
# 1. GitHub Actions 실행
# 2. Railway에 배포
# 3. 웹사이트 업데이트 ✅
```

---

## 📊 **GitHub에서 모든 것을 관리**

### GitHub에서 볼 수 있는 것:

1. **Code** 탭: 소스 코드
2. **Actions** 탭: 배포 로그 + 상태
3. **Deployments** 탭: 배포 히스토리 + URL
4. **Environments** 탭: production 환경 상태

### 웹사이트 URL:
- Deployments 탭에서 직접 확인 가능
- Railway 대시보드에서도 확인 가능

---

## 🎯 **과제 요구사항 충족**

```
✅ GitHub에 코드 업로드됨
✅ GitHub에서 배포 관리됨
✅ GitHub Actions로 자동 배포
✅ GitHub Deployments에서 상태 확인 가능
✅ GitHub에서 배포 URL 확인 가능
```

**완벽하게 GitHub 중심의 배포 파이프라인!** 🚀

---

## 🌟 **GitHub에 보여줄 수 있는 것들**

교수님/선생님께 보여줄 수 있는 것:

1. **GitHub 리포지토리**: https://github.com/lalagoola/home
2. **Code 탭**: Flask 소스 코드
3. **Actions 탭**: 배포 자동화
4. **Deployments 탭**: 배포 URL + 히스토리
5. **웹사이트**: 실제 작동하는 보건 수업 홈페이지

---

## 🔧 **문제 해결**

### Q: Actions에서 실패함
A:
1. **Settings** → **Secrets** 확인
2. RAILWAY_TOKEN이 올바른지 확인
3. Railway에서 Token 재생성 후 업데이트

### Q: Deployments에 URL이 안 보임
A:
1. Actions 로그 확인
2. `GITHUB_OUTPUT`에 url이 제대로 설정되는지 확인

### Q: 환경 변수 오류
A:
1. Railway Variables 탭 재확인
2. FIREBASE_* 변수 모두 있는지 확인

---

## 📝 **최종 체크리스트**

```
✅ GitHub에 Secrets 추가 (RAILWAY_TOKEN)
✅ Railway에서 API Token 생성
✅ Railway 환경 변수 설정 완료
✅ GitHub에 코드 푸시
✅ GitHub Actions 실행 확인
✅ Deployments 탭에서 URL 확인
✅ 웹사이트 접속 가능
```

모두 완료 = **과제 완료!** 🎊

---

## 🎓 **교수님/선생님께 보고할 내용**

```
"GitHub에 저장된 Flask 웹 애플리케이션입니다.
GitHub Actions를 사용해서 코드가 업로드되면 
자동으로 Railway 서버에 배포됩니다.

GitHub 리포지토리: https://github.com/lalagoola/home
웹사이트 URL: (Deployments에서 확인)

배포 상태는 GitHub Actions 탭에서 
확인할 수 있으며, 모든 배포 히스토리는 
Deployments 탭에 기록됩니다."
```

---

**이제 완벽하게 GitHub 중심의 배포 시스템입니다!** 🚀✨
