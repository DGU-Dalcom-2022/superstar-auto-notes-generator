

# get_block_sequence_with_deltas

compute_state_sequence_representation_from_json : json 가져와서 state rank에 맵핑 -> 모두 같은 숫자로 바꿔줌 104

one_hot_state -> 1, 2 원소의 처음꺼 마지막꺼에 1 넣어줌 -> 왜?

times_real_extended -> 시간만 넣어줌, state 버림

feature_indices -> 전체 길이 (max_index)를 넘지 않게 저장

return
time_beats -> state_time

#

indices -> 시간을 대충 정수 단위로 만들어서 저장 원래 1.69(초) -> 169
torch.size([61])

delta_forward
delta_backward

input_forward_deltas
input_backward_deltas

y
(100, 2388)
(100, 61)

song_sequence.shape 
torch.Size([1, 100, 61])

~~~
if not opt.tgt_vector_input:
    song_sequence = torch.cat([song_sequence,input_forward_deltas.double(),input_backward_deltas.double()],1) 
    # torch.Size([1, 102, 61]) 두번째 차원으로 이어붙임
~~~

src_pos
torch.Size([1, 61])

src_mask
torch.Size([1, 61])

# translator.sample_translation ( with no_grad -> for() {take step} )
song_sequence.permute(0,2,1).float() -> torch.Size([1, 61, 102])
-> src_seq
torch.Size([1, 61, 102])

## encoder
enc_output
torch.Size([1, 61, 512])

##
-> src_enc

## take_step 

dec_seq == [1]
-> tensor ([[1]])
dec_pos == tensor([1])

### decoder



###

prob
torch.Size([2003]) ?

##

처음부터 모든 seq가 들어가는게 아님
dec_seq가 갈수록 늘어남
차례대로 하나씩 디코더를 거침

#