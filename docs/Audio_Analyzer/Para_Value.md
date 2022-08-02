-----------------------------------------------------------Stage1--------------------------------------------------------------
sr = 44,100 / y = 1,342,464
nfft => 1024, 2048, 4096
hop = 441
y / hop(window) =>3044.xxx => 3045
n_mel = 80 => mel 스펙토그램의 주파수 해상도(얼마나 촘촘하게 볼지)
features => (80, 3045)
features_size => 80*3045 = 243,600
nfft에 따라서 featuress => ( features(1024), features(2048), features(4096) )
-> features = (80, 3, 3045)
feature 뒤에 zeros concatenate 진행 => padding => (80, 3, 3060)

input windows => (1, 80, 3, 3045)
-time_shifts//2 ~ time_shifts//2+1

input => (1, 15, 80, 3, 3045)
=> N, L, deltaT, dim, winsizes
=> reshape( N(1) * L(3045) , deltaT(15) , dim(80) , winsizes(3) )
3045,15,80,3
3045,20,9,26
3045, 20, 7 ,8
reshape( N(1) , L(3045) , 20*7*8)
(1, 3045, 1120)
lstm => (1, 3045, 512)
logits => (1, 3045, 5)
.cpu().detach().numpy() => 3045
=> find_peaks




step_size가 실제 초를 어느정도로 나눌지를 의미
ex) 30초가 조금 넘어가는 30.47초에 step_size == 0.01이면 마지막 인덱스가 30.46임
-----------------------------------------------------------Stage2--------------------------------------------------------------
sr = 16,000 / y = 487,062
song_duration = 30.44
hop = 160 = step_size*sr

n_mels = 100
feature = (100, 3045)
100 => 주파수 해상도
3045 => 시간 관련
내부값 => 진폭

feature 뒤에 zeros concatenate 진행 => padding => (100,3047)

state_sequence => state(아마 peak)의 sequence를 뽑아냄 => json파일에 있는거
json파일 => peak의 시간대 별로 note가 만들어짐 => 84개 있음
time이 real이 아님
state_sequence_real => 실제 시간으로 바꿈

times_real_extended => 제일 처음에 0, 제일 끝에 30.47 추가 => 86개임
times_beats = 실제 시간으로 바꾸기 전의 state_sequence를 형태만 변환 시간만 뽑아옴

max_index = 3046
feature_indices = times_real_extended를 30.38 => 3038로 변환 즉, 86개
states => 86개이고, 아직은 default값이 104임 but startState = 1, endState = 2임

one_hot_states = (2003, 86)
2003 => top_k(2000) + NUM_SPECIAL_STATES(3) / 86 => states.shape[0]

time_diff => ex) 58 - 57 => 57번 인덱스에 저장 / 뒷 시간과의 차이를 저장함, 따라서 85개

delta_backward (1, 86) /  0번 인덱스에 0추가 => 86개
delta_forward (1, 86) / 제일 끝에 0추가 => 86개

truncated_sequence_length => opt의 max_token(2048), len(state) 중 작은거 택함 => 86

indices => 시간이 담겨있는 크기 86의 텐서 => 양 끝(시작, 끝)이 있음
feature => y에 넣고 변형
y => 정해진 시간 부분(indices)만 뽑아냄 (100, 86) , 해당 값

100 => 주파수 / 86 => stage1에서 선택된 시간 / 해당 값 => 진폭
86은 원래 84개인데 양 끝에 0 추가해서 86된거임
=> input _windows (1, 100, 86) = song_sequence

(선택된 시간대에 해당하는 주파수의 진폭 - 전체 진폭의 평균) / 전체 진폭의 절댓값중 최고값
song_sequence => y에서 
song_sequence - song_sequence.mean() / song_sequence.abs.max.float (1, 100, 86)
song_sequence.mean() = -33.0951
song_sequence.abs.max.float = 80
song_sequence + input_forward_deltas + input_backward_deltas => concat
뒤에 2, 0, 0, 0 ~~ 와 0, 2, 0, 0, ~~ 붙음 (1, 102, 86)

src_pos = (1, 86)   => 0, 1, ... ,85
src_mask = (1, 86)  => 4, 4, ... ,4

src_seq = (1, 86, 102)

USE_BEAM_SEARCH => translate_batch(song_sequence, src_pos, src_mask, truncated_sequence_length)
song_sequence(1, 102, 86) => 정해진 시간에서의 주파수, 진폭 데이터 / 가공되어있음
src_pos(1,86) => transformer에 필요한 위치 정보를 담고 있음 / 인덱스의 증가에 따라서 0~85까지 1씩 증가함
src_mask(1,86) => transformer에서 사용할 mask 정보
truncated_sequence_length => 시퀀스의 사이즈 86

transformer => opt
beam_size => 20
beat_subdivision => 16

n_bm = beam_size
src_enc = encoder, (1, 86, 512)
n_inst = 1
len_s = 86
d_h = 512

src_seq = .repeat(1, n_bm,1).view() => (20, 86, 102) 기존과 같은 값임
src_mask = (1, 86) => (20, 86)
src_env = (20, 86, 512)



dec_seq (20,1) 1,1,1,1,1,1,1
dec_pos (20,1) 1,1,1,1,1,1,1

dec_output -> (20, 1, 512) -> (20, 512) => 어차피 하나의 batch로 진행하기 때문에 lastStep을 가져오면 해당 형태

# inst_dec_beams 
scores => 처음 다 0 size만큼 (20)
all_scores => 대기중(빔)
next_ys => 처음 다 0 size만큼 (20) => 다 1로
prev_ks => 대기중(빔)

collect_active_inst_idx_list(inst_beams, word_prob, inst_idx_to_position_map)
inst_beams => inst_dec_beams
for => inst_idx, inst_position => inst_idx_to_position_map.items()

word_prob => 단어 유사도, 확률 같은 것

beam.advance => word_prob에서 유사도 높은 것을 뽑음
처음 => word_prob[0] => beam_1k에 저장(2003)
beam_1k에서
topk(size = 20)를 통해 값이 가장 큰 순서대로 20개의 값을 뽑앙서 score에 저장
score_id => 이에 대한 index값
prev_ks = best_scores_id // num_words 를 넣음
num_words => 2003
next_ys = best_scores_id - prev_k * num_words => 처음에는 prev가 0이기 때문에 다 기본값이 들어감



score 채움
1 => all_score => 다 0 next_ys 0 - 다 1 / 1 - 다양 prev_ks => 다 0

한번 진행
all_score => score 값이 저장 
next_ys => 쌓임
prev_ks => 쌓임
score(20) => 값이 변화

len_dec_seq의 크기와 같음 next_ys만 하나 더 size가 큼 => 마지막에는 all_score에 하나 더 넣기 떄문에 결국 prev_ks만 하나 작은 상태

all_scores가 size 85가 되면 끝 => 제일 앞은 그냥 다 0임


get_hypothe3sis
 j => prev_ks.length(84) -1 = 83 부터 시작 => -1씩 계속
 k => tail[0] => 0부터
 hyp = next_ys[j+1][k]
 k = prev_ks[j][k]
hyp가 결국 generated_sequence 이므로 next_ys, prev_ks를 살펴봐야함
j => 0 되면 나가리
총 84번 반복, 84개의 hyp가 생김