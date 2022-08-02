# Unique State

나올 수 있는 모든 경우를 저장한 data/statespace/sorted_states.pkl

stage2에서 unique_state로 가져와진다.

## 생성

scripts/data_processing/identify_state_space.py에서 생성 

produce_distinct_state_space_representations 함수로 sorted_state를 생성한 뒤, 

io_functions.saveFile로 sorted_states.pkl에 저장(pickle.dump)

## produce_distinct_state_space_representations

data/extracted_data에 있는 모든 데이터를 가져와서

모든 state를 저장

각 state에 대한 빈도수를 state_frequencies에 저장 -> dictionary

sorted_states = sorted_states_by_frequency

states_counts = sorted_states_count

# 생성과정 실행 및 디버깅 해보기
-> 그런데 아직 이렇게 하면 제대로 볼 수 없음

## extracted_data

scripts/data_processing/identify_state_space.py를 실행하려면 extracted_data가 있어야 하고, 이건 scripts/data_retrieval/download_data.py로 생성 가능

-> 근데 이거 실행 안됨


### 예시 데이터 가져오기

먼저 deepsaber 폴더 위치로 이동

아래 명령으로 다운로드하거나 링크 이동 : https://mega.nz/file/sABVnYYJ#ZWImW0OSCD_w8Huazxs3Vr0p_2jCqmR44IB9DCKWxac

~~~
wget -O DataSample.tar.gz https://www.dropbox.com/s/2i75ebqmm5yd15c/DataSample.tar.gz?dl=1
~~~

아래 명령을 차례대로 실행
~~~
tar xzvf DataSample.tar.gz
mv scripts/misc/bash_scripts/extract_zips.sh DataSample/
mv DataSample/* data/extracted_data
~~~

## identify_state_space.py 실행

io_functions를 복사해서 맞는 위치에 넣기

초반에 THIS_DIR 빼고 DIR 관련 된 부분 주석 처리, 

EXTRACT_DIR에 extracted_data의 "절대 경로" 대입

sorted_states_transition_probabilities 관련 주석 처리 <- 이 부분 아직 모름 

