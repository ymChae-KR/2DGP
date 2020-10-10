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



\5. 실행 흐름

![흐름1](https://user-images.githubusercontent.com/71045957/95655286-17805c00-0b41-11eb-8806-2078a216922a.png)

- 1

•몬스터들이 등장하고 몬스터는 몇번의 충돌판정으로 파괴시킬 수 있음.

•이 과정 중 몬스터에게 피격당하면 사망

![흐름2](https://user-images.githubusercontent.com/71045957/95655292-21a25a80-0b41-11eb-82c7-5f3bb5d063f4.png)

- 2

•보스 몬스터가 등장함. 

•보스 몬스터는 다수의 충돌판정 이후 파괴시킬 수 있으며 보스의 총알에 피격 당하면 사망



/6. 개발 범위

![개발범위](https://user-images.githubusercontent.com/71045957/95655277-0cc5c700-0b41-11eb-9727-62af34af27df.png)

/7. 개발 일정

![개발 일정](https://user-images.githubusercontent.com/71045957/95655250-e869ea80-0b40-11eb-9fc0-88c227362851.png)