# TIL 생성하기

## Git 기본 사용
git init
> 로컬 저장소 설정(초기화) : git의 버전 관리를 시작할 디렉토리에서 진행

git add
> 변경사항이 있는 파일을 staging area에 추가

git commit 
>  staging area에 있는 파일들을 저장소에 기록 : 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
   
## 개인 TIL 생성하기
**Remote Reposotory**
> 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간 

git remote add origin remote_repo_url
> 별칭을 사용해 로컬 저장소 한 개에 여러 원격 저장소를 추가할 수 있음

git push origin master
> 원격 저장소에 commit 목록을 업로드

git pull origin master
> 원격 저장소의 변경사항만을 받아옴 (업데이트)

git clone remote_repo_url
> 원격 저장소 전체를 복제 (다운로드)
**clone으로 받은 프로젝트는 이미 git init이 되어있음**


## 개인 TIL 생성 과정
```SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R
$ git init
Initialized empty Git repository in C:/DEV/TIL_R/.git/

SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ touch README.md

SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ git add README.md

SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ git commit -m 'first commit'
[master (root-commit) 63f609f] first commit     
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md

SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ git remote add origin **개인URL**
SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 206 bytes | 206.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To **개인URL**
 * [new branch]      master -> master

SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ git push origin master
Everything up-to-date

SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ git add .

SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ git commit -m '기본 학습 파일 생성'
[master 0fae536] 기본 학습 파일 생성
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 ALGORITHM/README.md
 create mode 100644 PYTHON/README.md

SSAFY@2□□PC174 MINGW64 /c/DEV/TIL_R (master)
$ git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 306 bytes | 306.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To **개인 URL**
   63f609f..0fae536  master -> master