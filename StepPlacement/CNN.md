# CNN

Convolution을 통한 Filtering과 Max pooling을 반복하여, 정말 중요한 특징들을 정제한 후, Classification을 하는것

![image](https://user-images.githubusercontent.com/57888020/162371304-bccac427-a851-486c-96a0-94f222ea8e16.png)

https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53

## Convolution

![image](https://user-images.githubusercontent.com/57888020/162371649-def347f9-004d-4bf2-899c-bbc4de209174.png)

정보의 손실이 일어나지만 특징들을 모아서 작은 값으로 저장함 (정보의 손실을 줄이기 위해서 zero padding을 쓰기도)

컬러 사진의 경우 RGB 값 각각 하여 다음과 같음

![image](https://user-images.githubusercontent.com/57888020/162372091-8cac0c04-1bc2-468c-87ff-eeeea1fe01e8.png)

Feature Map : 입력 데이터를 필터가 순회한 후 합성곱으로 만든 결과물

Activation Map : Feature Map에 활성함 수 적용, Convolution layer의 최종 결과물

## Max pooling

그렇게 필터를 거치고 나온 값 중에서 가장 큰 값 하나만 선택

<img width="251" alt="image" src="https://user-images.githubusercontent.com/57888020/162372689-ec03e3c7-66d0-4ea9-b485-6006402c7aa1.png">

![image](https://user-images.githubusercontent.com/57888020/162372489-3ff19d44-9b29-41f3-9a1a-39cfaff27a70.png)

Convolution layer 의 결과물이 값이 너무 많기 때문에 하는 것

이 과정을 통해서 각 feature map의 차원을 축소하고 오버피팅을 줄이고 연산속도를 올려줌


참고자료

https://velog.io/@noooooh_042/%EB%94%A5%EB%9F%AC%EB%8B%9D-CNN
