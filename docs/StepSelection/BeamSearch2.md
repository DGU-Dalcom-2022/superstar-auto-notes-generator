# BeamSearch   

조건부 확률에 따라 각 단계에서 입력 시퀀스에 대한 여러개의 대안을 고른다.       

  Beam Width B(빔의 넓이) : 대안의 수   

각 단계에서 그 단계에서 가장 선택될 가능성이 높은 확률을 갖는 최고 대안의 수 B를 선택한다.   
예를들어, B의 크기가 3, 단어집 크기가 10,000 이라고 하자.   

### step 1

입력문장이 주어지면 가장 높은 확률을 가진 상위 3개의 단어를 찾음.   
모든 단어집에 softmax 적용 -> 여기서 가능성 가장 높은 3개의 단어 선택해서 메모리에 저장. 

![image](https://user-images.githubusercontent.com/69388421/153822835-02ec946a-bd81-475b-b7c9-6256bc2fc953.png)

### step2

첫번째 단어 3개를 두번째 단계로 보낸다. 모든 단어집에 다시 softmax 적용 
첫번째와 두번째 단어에 대한 최고의 3쌍을 찾기 위해 첫번째 단어 중 하나를 가져와 단어집 내 10,000개의 모든 단어에 softmax 적용

-> 총 30,000개의 조합 실행

쌍이 만들어지지 않으면 단어를 drop

![image](https://user-images.githubusercontent.com/69388421/153822863-79c0e43d-43d9-4755-94bc-e89077b46cda.png)


### step3
![image](https://user-images.githubusercontent.com/69388421/153822889-1e996687-ee3e-42ab-902e-4a024384e671.png)

같은 방식으로 세번째 단어를 찾는다. 이 절차를 계속 반복하면 결국 3개의 문장이 선택된다. 
상위 3개의 문장은 다양한 길이일 수 있다.
여기서 가장 높은 확률을 가진 문장을 디코더 출력으로 선택한다.

![image](https://user-images.githubusercontent.com/69388421/153822917-892dfc5d-aac3-4fbc-b6d6-5818c7446109.png)




  빔 넓이가 크면 더 정확한 결과가 나오지만 많은 메모리와 컴퓨팅 파워를 사용한다.
