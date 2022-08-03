# train.py
 training/block_placement_ddc2/opt.json     => ddc
 training/block_selection_new2/opt.json     => transformer

 opt에 옵션을 받고 모델 생성 => 모델명에 맞는 models/모델명_model.py를 이용함
 내부에는 nn.Module을 상속받아 인공지능 세팅을 진행함 
 ex) ddc2의 경우 ddc_model.py의 DDCNet 클래스를 이용 => nn.Module 상속 받음
 Conv2d, MaxPool2d, Conv2d, LSTM, Linear로 구성되어있음 => C-LSTM임
 Forward도 구성 
 ex) relu로 활성화, shape 바꿔가면서 결론 내는 듯
 ## dataSet
  scripts.training.data.song_dataset 모듈에 dataset이 존재해야함
  song_dataset의 
