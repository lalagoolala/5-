# ⭐ GitHub에서만 배포하기 - 최종 단계별 가이드

## 🎯 **지금 바로 3단계만 하세요!** (5분)

---

## **1️⃣ Vercel 연동** (2분)

1. https://vercel.com 방문
2. **GitHub로 로그인** (또는 가입)
3. **"New Project"**
4. **"Select a Git Repository"** → **lalagoola/home** 선택
5. **"Deploy"** 클릭
6. 완료! ✅

---

## **2️⃣ GitHub Secrets 추가** (2분)

### Vercel에서 정보 얻기:

1. Vercel 대시보드 열기
2. **Settings** → **Tokens** 클릭
3. **Create Token** → 복사 (VERCEL_TOKEN)
4. **Dashboard** → 프로젝트 선택
5. URL 끝부분 확인:
   - `vercel.com/:ORG/:PROJECT` 형태
   - `:ORG` = VERCEL_ORG_ID
   - `:PROJECT` = VERCEL_PROJECT_ID

### GitHub에 추가:

1. https://github.com/lalagoola/home
2. **Settings** → **Secrets and variables** → **Actions**
3. **New repository secret** 3개 추가:
   ```
   VERCEL_TOKEN=(위에서 복사한 Token)
   VERCEL_ORG_ID=(프로젝트 URL의 ORG 부분)
   VERCEL_PROJECT_ID=(프로젝트 URL의 PROJECT 부분)
   ```

---

## **3️⃣ Vercel 환경 변수 설정** (1분)

1. Vercel 대시보드 → 프로젝트 선택
2. **Settings** → **Environment Variables**
3. 다음 변수들 추가:

```
FLASK_ENV = production
SECRET_KEY = health-app-secret-key
FIREBASE_API_KEY = AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k
FIREBASE_AUTH_DOMAIN = homepage-63d32.firebaseapp.com
FIREBASE_PROJECT_ID = homepage-63d32
FIREBASE_STORAGE_BUCKET = homepage-63d32.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID = 515012802016
FIREBASE_APP_ID = 1:515012802016:web:4c3db8588aa7f00df8a785
FIREBASE_DATABASE_URL = https://homepage-63d32-default-rtdb.firebaseio.com
```

---

## **4️⃣ GitHub에 최종 push** (1분)

```bash
cd "c:\Users\cyh99\Documents\프로젝트"

git add .
git commit -m "Setup GitHub automatic deployment with Vercel"
git push origin main
```

---

## 🎉 **완료!**

이제:
- ✅ GitHub에 push → 자동 배포
- ✅ GitHub Actions에서 상태 확인
- ✅ GitHub Deployments에서 URL 확인
- ✅ 웹사이트 자동으로 업데이트됨

---

## 🌐 **웹사이트 주소 확인**

### 방법 1: GitHub에서
```
리포지토리 → Deployments → production → URL 클릭
```

### 방법 2: Vercel에서
```
Vercel 대시보드 → Domains → 링크 클릭
```

---

## 🔄 **이제부터 할 일**

파일 수정 후 → `git push` → 자동 배포! ✅

```bash
# 파일 수정 (예: index.html)

# GitHub에 푸시
git add .
git commit -m "Update design"
git push origin main

# 1-2분 후 웹사이트에 반영됨 🎊
```

---

## 📞 **문제 해결**

### Q: GitHub Actions에서 실패함
A: Secrets 확인
```
Settings → Secrets → VERCEL_TOKEN, VERCEL_ORG_ID, VERCEL_PROJECT_ID 모두 있는지 확인
```

### Q: Vercel에서 빌드 실패함
A: 환경 변수 확인
```
Vercel → Settings → Environment Variables → FIREBASE_* 모두 있는지 확인
```

### Q: 웹사이트가 안 열려요
A: 배포 대기
```
Vercel 대시보드에서 배포 상태 확인 (초록색 = 완료)
```

---

## ✨ **최종 체크리스트**

```
✅ Vercel 계정 생성 및 GitHub 연동
✅ GitHub Secrets에 VERCEL_TOKEN 등 추가
✅ Vercel 환경 변수 설정 완료
✅ GitHub에 최종 push 완료
✅ GitHub Actions 초록색 체크 확인
✅ Deployments에서 URL 확인
✅ 웹사이트 접속 가능
```

모두 완료 = **배포 완료!** 🚀

---

**축하합니다! GitHub에서 자동으로 배포되는 완벽한 시스템을 갖춘 과제입니다!** 🎊
