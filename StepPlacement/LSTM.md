# LSTM

RNN (Recurrent neural network) : 스스로를 반복하면서 이전 단계에서 얻은 정보가 지속되도록 하는 모델

LSTM (Long Short-Term Memory Network)은 RNN의 일종

RNN은 짧은 기간에 의존하는 반면, LSTM은 긴 기간에 의존한다. 

다음 데이터를 예측할 때 가까운 지난 정보를 참조할 때 RNN을 사용할 수 있지만 더 많은 지난 데이터들을 필요로 할 때, 시간 격차가 커지게 된다.

이 격차가 늘어날 수록 RNN으로는 학습하는 정보를 계속 이어나가기 힘들다. 

긴 의존 기간의 문제를 피하기 위해 LSTM은 명시적으로 설계되었다. 

## 구조

RNN은 그 반복 모듈의 구조가 단순하다. tanh layer 한 층 만을 가지고 있다.

![image](https://user-images.githubusercontent.com/57888020/162364593-6c58bd8d-3ce0-457e-ae56-9320164ab030.png)

LSTM은 다른 구조를 가지고 있다. 단순히 neural network layer 한층이 아니라 4개의 layer가 특별한 방식으로 서로 정보를 주고 받는다.

![image](https://user-images.githubusercontent.com/57888020/162364612-05ad6a5f-a5f0-4566-a755-0aad9831e8a9.png)

각 도형의 뜻은 다음과 같음

![image](https://user-images.githubusercontent.com/57888020/162364638-d19f9a2f-b80c-46ed-9b73-a628f267d2ac.png)
 
Pointwise Operation : 점(벡터의 원소) 별로 연산을 해주겠다는 것

concatenate : 이어붙이기 

## Cell state of LSTM

![image](https://user-images.githubusercontent.com/57888020/162366182-da3e776d-3223-4663-a569-9b582c576632.png)

위 그림에서 표시된 부분이 LSTM에서 핵심인 cell state. 

작은 linear interaction만을 적용시켜 전체 체인을 구동시킨다.

이 cell state는 gate 구조로 뭔가가 더해지거나 없어질 수 있다.

LSTM은 3개의 gate로 cell state를 보호하고 제어한다.

gate는 정보가 전달될 수 있는 추가적인 방법으로, sigmoid layer와 pointwise 곱셈으로 이루어져잇다. 

![image](https://user-images.githubusercontent.com/57888020/162367015-5377b933-918a-4913-9e1d-6c89bcebeeff.png)

LTSM의 첫번째 gate. 

sigmoid layer는 0과 1사이의 숫자를 보내는데 이것으로 각 컴포넌트의 정보전달 여부가 결정된다. 0이면 아무 정보도 전달하지 않음

## LSTM 진행 과정

### 1. forget gate layer : sigmoid layer가 cell state로부터 어떤 정보를 버릴지 결정한다.

![image](https://user-images.githubusercontent.com/57888020/162368214-2c78c552-62e9-4ce7-acd8-b4e64a26f014.png)

### 2. input gate layer

![image](https://user-images.githubusercontent.com/57888020/162368808-f6e5402e-c529-47bf-93c6-f08fe909c127.png)


 - sigmoid layer : 어떤 값을 업데이트할 지 정한다. 

 - tanh layer : 새로운 후보 값들인 벡터를 만든다.

 - 두 레이어에서 나온 정보를 합쳐서 state를 업데이트할 재료를 만든다.

### 3. cell state pdate

![image](https://user-images.githubusercontent.com/57888020/162368999-dc03194d-f780-4361-b536-c304bb0d32de.png)

잊어버리기로 한 것을 곱하고 업데이트할 값을 더한다. 

이때 업데이트할 값은 2단계에서 만든 값에 업데이트 정도를 정해 scale한 값이다. 

### 4. output 지정 : cell state 바탕으로 필터된 값 

![image](https://user-images.githubusercontent.com/57888020/162369426-3ae85e4d-be66-44be-ac95-2d1b74b9fb14.png)

input을 받은 sigmoid layer가 cell state의 어느 부분을 output으로 할 지 결정

state를 받은 tanh layer가 -1에서 1사이의 값을 받음

sigmoid gate의 output과 곱함

참고링크 : https://dgkim5360.tistory.com/entry/understanding-long-short-term-memory-lstm-kr

RNN은 그 반복 모듈의 구조가 단순하다. tanh layer 한 층 만을 가지고 있다.

LSTM은 다른 구조를 가지고 있다. 단순히 neural network layer 한층이 아니라 4개의 layer가 특별한 방식으로 서로 정보를 주고 받는다.

