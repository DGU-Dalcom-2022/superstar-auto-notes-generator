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

 ## 실행시 에러 발생
  랜덤한 epoch 값에서 아래 함수를 호출하는 과정에서 에러가 발생함
  여러 개의 곡이 문제인가 하여 하나의 곡만으로 실행시켜도 문제 발생함
  blocks_targets = get_binary_reduced_tensors_from_level_faster
  (blocks_reduced_classes,indices,sequence_length,1+constants.NUM_SPECIAL_STATES,bpm,sr,num_samples_per_feature,blocks_receptive_field,blocks_input_length, output_length,blocks_time_offset)
  - blocks_reduced_classes 
  shape : (7543,1)
  max : 4.0, min : 1.0
  float
  - indices
  shape : (10,)
  max : 7121, min : 2639
  int
  - receptive_field
   1
  - output_length
   100
  - time_offset
   0

    block_reduced_targets_windows = [blocks_reduced_classes[
                                     i + time_offset + receptive_field - 1:i + time_offset + receptive_field - 1 + output_length,
                                     :] for i in indices]
    block_reduced_targets_windows = torch.tensor(block_reduced_targets_windows, dtype=torch.long)
    문제가 없을 시 
    10x100x1 다 3

    