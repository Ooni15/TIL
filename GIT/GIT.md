# Git 개념
## Git 
>분산 버전 관리 시스템

1. 분산 구조에서의 장점
 - 중앙 서버에 의존하지 않고도 동시에 다양한 작업을 수행할 수 있음
- 개발자들 간의 작업 충돌을 줄여주고 개발 생산성을 향상
- 중앙 서버의 장애나 손실에 대비하여 백업과 복구가 용이
- 인터넷에 연결되지 않은 환경에서도 작업 가능 
 - 변경 이력과 코드를 로컬 저장소에 기록하고, 나중에 중앙 서버와 동기화
  
2. Git의 역할 
- 코드의 버전(히스토리)를 관리 
 - 개발되어 온 과정 파악
- 이전 버전과의 변경사항 비교

3. Git의 영역
    >git의 3가지 영역 : **Working Directory, Staging Area, Repository**
    1) Working Directory : 실제 작업 중인 파일들이 위치하는 영역
    2) Staging Area : Working Directory에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
    3) Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역

4. Commit (버전)
    > 변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록하다 하여 'snapshot'이라고도 함   