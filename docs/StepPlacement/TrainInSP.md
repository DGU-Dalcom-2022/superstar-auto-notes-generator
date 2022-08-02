# Training/README.md

deepsaber-master/scripts/training/train.py로 학습이 이루어짐

전체 DeepSaber 모델을 학습시키려면 ./script_block_placement ./script_block_selection 실행

`binarized` : StepPlacement의 경우 현재 노트 집합이 존재하는지 여부(binarized), Step Selection의 경우 현재 특정 상태(not binarized)

...

# Training Options

`nepoch` : 훈련할 epoch 수. "epoch"는 모든 곡의 모든 부분을 통과하는 것
그런데 특정 수의 window들만을 사용하기 때문에 반드시 모든 곡의 모든 부분을 통과하는 것은 아님(아래의 자세한 설명 참조).

`nepoch_decay` : decaying the learning rate 이후에 학습을 위한 epoch 수

* Learning Rate Decay : Learning Rate를 점점 감소시킴. 
  왜? 미니배치가 작을 경우에 미니 배치별로 데이터 분포가 상당히 달라서 생각만큼 최적값에 가까이 도달하지 못할 수도
  
  <img width="225" alt="image" src="https://user-images.githubusercontent.com/57888020/165876922-027b726f-71ba-4f8f-af48-7cdbf2aee82d.png">

  위 그림의 파란색 선처럼, 최적값으로 향하기는 하지만, 정확히 수렴하지 않을 수 있음. 
  
  고정된 러닝레이트를 사용할 때 미니 배치별로 노이즈가 있기 때문. 그래서 러닝레이트를 갈수록 감소시킴 
