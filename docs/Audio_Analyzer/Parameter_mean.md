# SR(Sample rate)
 초당 얻어지는 Sample 횟수
즉, SR이 44,100이면 초당 44,100의 Sample이 포함되는 것
따라서 보통 쓰는 audio source의 y값 = SR * Song_Duration

# time series
 일반적인 audio Signal => y임 
 즉, 총 샘플수

# hop
 음성을 얼마나 겹친 상태로 잘라서 칸으로 보여줄 것인지
 window 간의 거리
 즉, window_length - frame_stride 만큼 겹쳐서 1칸을 뽑는것임
 ex) 데이터 = 7초, window_length = 0.025초, frame_stride = 0.01초이면 1칸은 0.015초가 겹치며 총 700칸을 얻음

 # window 길이
 윈도우의 길이가 짧으면 피치, 음색과 같은 Low-Level 특징을 뽑아냄
 윈도우의 길이가 길면 멜로디, 리듬과 같은 High-Level 특징을 뽑아냄

 # 멜 스펙트럼
 실제 사람이 인식하는 주파수를 이용하는 스펙트럼

 # Ceptral 분석
 배음(Harmonics)의 구조에서 음색 등의 고유한 특성을 찾아내는 것

 # 푸리에 변환(FT)
 시간, 공간에 대한 함수 => 시간, 공간 주파수 성분으로 분해하는 것
 ex) 디지털 신호 <-> 디지털 주파수
 고속 푸리에 변환(FFT)
 시간에 따른 진폭 -> 주파수에 따른 진폭

 # n_fft
 한 번 fft를 진행할 만큼의 sequence 길이

