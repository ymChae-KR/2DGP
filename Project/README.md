제목 : 1945

\1.

https://play.google.com/store/apps/details?id=com.os.airforce&hl=en_ZA

목적 : 제트기를 조종하여 총알을 피하고 몬스터들을 격추시킨다.

방법 : ←→↑↓키를 이용하여 조종하고 space키를 입력하여 총알을 발사한다.



\2.  

Scene 총 3개. 

Login Scene

Menu Scene

Play Scene



\3. 

Login Scene : 아무키 입력 → Menu Scene으로 전환

스프라이트 이미지 출력



Menu Scene : 몇가지의 비행기 모델을 선택할 수 있고 그 비행기로 게임을 플레이한다.

각 비행기별 모델.

←, →, SDLK_SPACE 키.

Space키 입력시 해당 모델로 캐릭터가 정해지고 Play Scene으로 전환



Play Scene : 실제 게임 화면

플레이어 객체, 몬스터 객체, 총알 객체.

←, →, SDLK_SPACE 키.



\4. 

class를 이용한 객체 지향 프로그래밍. 스프라이트 이미지 출력과 더블버퍼링을 이용한 원활한 애니메이션

파이썬만의 충돌처리 기법. 그에 연관된 모듈에 대한 소개