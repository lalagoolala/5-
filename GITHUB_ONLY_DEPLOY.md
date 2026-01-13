# 🚀 GitHub에서만 배포하기 (Vercel 자동 연동)

## ✨ **가장 간단한 방법 - GitHub에 push만 하면 됨!**

이제 GitHub에 코드를 push하면 **자동으로 웹사이트가 배포**됩니다.
다른 사이트를 따로 건드릴 필요가 없습니다!

---

## 📋 **설정 (3단계 - 5분)**

### **Step 1: Vercel 연동** (2분)

1. https://vercel.com 방문 (무료)
2. **GitHub로 로그인**
3. **"New Project"** 클릭
4. **"lalagoola/home"** 저장소 선택
5. **"Deploy"** 클릭
6. 배포 완료! ✅

### **Step 2: GitHub Secrets 추가** (2분)

1. https://github.com/lalagoola/home
2. **Settings** → **Secrets and variables** → **Actions**
3. **New repository secret** 추가:
   - `VERCEL_TOKEN` (Vercel 대시보드 → Settings → Tokens에서 복사)
   - `VERCEL_ORG_ID` (Vercel 대시보드에서 확인)
   - `VERCEL_PROJECT_ID` (Vercel 대시보드에서 확인)

### **Step 3: 환경 변수 설정 (Vercel)** (1분)

Vercel 대시보드에서:

1. 프로젝트 선택
2. **Settings** → **Environment Variables**
3. 아래 변수들 추가:

```
FLASK_ENV=production
SECRET_KEY=health-app-secret
FIREBASE_API_KEY=AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k
FIREBASE_AUTH_DOMAIN=homepage-63d32.firebaseapp.com
FIREBASE_PROJECT_ID=homepage-63d32
FIREBASE_STORAGE_BUCKET=homepage-63d32.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=515012802016
FIREBASE_APP_ID=1:515012802016:web:4c3db8588aa7f00df8a785
FIREBASE_DATABASE_URL=https://homepage-63d32-default-rtdb.firebaseio.com
```

---

## 🎉 **완료! 이제 자동 배포됨**

### GitHub에서 할 수 있는 모든 것:

```bash
# 파일 수정

# GitHub에 푸시
git add .
git commit -m "Update homepage"
git push origin main

# 자동으로:
# 1. GitHub Actions 실행
# 2. Vercel에 배포
# 3. 웹사이트 업데이트 ✅
```

---

## 🌐 **웹사이트 접속**

### GitHub에서 확인:
1. 리포지토리 → **Deployments**
2. URL 클릭

### Vercel에서 확인:
1. Vercel 대시보드 → 프로젝트 선택
2. **Domains**에서 URL 확인

---

## 🎯 **GitHub UI에서 모든 것 관리**

- **Code 탭**: 소스 코드 확인
- **Actions 탭**: 배포 자동화 확인
- **Deployments 탭**: 배포 상태 + URL 확인
- **Push**: 자동 배포 트리거

---

## 💡 **핵심**

```
GitHub에 push
    ↓
GitHub Actions 자동 실행
    ↓
Vercel에 배포 (GitHub에서 관리)
    ↓
웹사이트 라이브! 🌐
```

**GitHub에서만 작업하면 됩니다!** ✨

---

## 🚨 **만약 배포가 안 되면?**

1. GitHub **Actions** 탭에서 로그 확인
2. Secrets가 모두 있는지 확인
3. Vercel 환경 변수가 모두 설정되었는지 확인

---

**이제 정말로 GitHub에서만 배포됩니다!** 🚀
