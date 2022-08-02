https://docs.google.com/document/d/1wOtaH9X033DHvCPnox_Yj2MvNUXONKZ_SOst4k9FFpY/edit?usp=sharing

# TODO LIST

## Step Placement
- [x] ddc 논문 이해하기
- [x] peak 찍는 방법 이해하기
- [x] generate level 부분 분석

## Step Placement(Time)
- [ ] 원본 오디오 파일이 변환되는 과정 확인
- [ ] 세부 파라미터들이 의미하는 것을 파악(이론적)
- [ ] 왜 이러한 Time이 찍혔는지 이해

## Step Selection
- [x] Transformer(stage2 model) 이해
- [x] Teacher Forcing : 어떤 정답값을 주고 있는지 파악 -> 인코더와 같은 정답 값을 가지고 있음
- [x] Transformer의 용도 : generate -> generated_sequence
- [x] Step Placement의 결과물 사용처 : generated_sequence 생성
- [x] 멀티 노트 시점 선정 기준 -> states_grid(==grid_state)의 원소(tuple)이 값을 두개 가지고 있는 경우

## SuperStar Resource
- [x] 노트 데이터 형식
- [x] 난이도에 따른 차이
- [x] 노트를 찍는 기준, 스타일

## 20220204 이후 
- [x] Transformer 이해
    - [x] beam search 이해
- [ ] json 형식 맞추기
- [ ] 보컬, 멜로디 별 샘플 확인, 비교

## 20220215 이후
- [ ] hyp
- [ ] tick
- [ ] SEQEditor code, dotpeek, dll파일, 데스크톱 앱개발..?

## 생각해볼 것
- [ ] 롱노트
- [ ] 방향성 : 최종 결과물의 활용 방면
- [ ] 새로운 unique state....???
- [ ] SuperStar 가이드라인에 맞는 모델 변형
- [ ] Editor exe 파일 뜯어보기

