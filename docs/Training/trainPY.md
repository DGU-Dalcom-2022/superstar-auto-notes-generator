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
    모든 indices의 i마다
    blocks_reduced_classes[i+time_offset+receptive_field-1:i+time_offset+receptive_field-1+output_length,:]
    
    
    [start:stop:step]
    step => 시작부분부터 해서 ex)  2이면 0 2 4 6 8 3이면 0 3 6
    2:6:2이면 2 4 임 2:7:2면 2 4 6 임
    
    start : i+time_offset+receptive_field-1
    stop : i+time_offset+receptive_field-1+output_length

    i => indices임
    indices => (10,1) 10개의 값이 존재 
    ex) 10457, 19373, 13366, 14874, 5983, 5148, 20145, 7593, 17681, 18335임
    time_offset => 0
    receptive_field => 1
    output_length => 100
    다 opt임
    이건 고정임
    indices와 blocks_reduced_classes가 달라짐
    indices+100이 blocks_reduced_classes의 length보다 길어지면 오류가 생김
    blocks_reduced_classes => 전처리된 것임
    indices = np.random.choice(
        range(self.opt.time_shifts//2,sequence_length-(input_length+self.opt.time_shifts//2+self.opt.time_offset)),size=self.opt.num_windows,
        replace=True
        )
    self.opt.time_shifts//2,sequence_length-(input_length+self.opt.time_shifts//2+self.opt.time_offset))
    15 // 2, 
    sequence_length는 y.shape[-1]
    y는 80, 3, 21777 but blocks_reduced_classes는 size가 21762임
    y => 그냥 feature 추출 
    처음에는 같음 but 곡 생성때와 같은 방식으로 패딩을 진행, wavenet과 같은 거에 유리하기 때문에


    block_reduced_targets_windows = torch.tensor(block_reduced_targets_windows, dtype=torch.long)
    문제가 없을 시 
    10x100x1 다 3,4
    문제 발생
    10x100x1이 아닌 그 중 하나의 리스트가 100이 아닌 97이 된다. expected sequence of length 100 at dim 1 (got 97)



    

    