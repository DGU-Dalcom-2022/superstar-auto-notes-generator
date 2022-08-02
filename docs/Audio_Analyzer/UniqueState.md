Unique_State => beatsaber 노트 파일을 분석하여 노트들을 State로 지정
=> 가장 빈도수가 높은 노트를 최상위 Unique_state로 설정
# download_data.py
 http://beatsaver.com/download/ 사이트에서 zip 파일로 되어있는 json 형식의 .dat 파일을 다운 받음
 zip형태 자체로 가져와서 번호를 매기고(시작이 1), 폴더형태로 파일을 유지

# identify_state_space
 다운로드한 data파일을 토대로 state를 뽑아내는 프로그램
 produce_distinct_state_space_representations => json 파일 가져와서
 compute_explicit_states_from_bs_level => notes에서 cut_direction, col, ow, time, type을 추출하여 가공
 => index = 4 * row + col, representation = 1 + 9 * type + cut_direction
 state_dict[time][index] = representation


