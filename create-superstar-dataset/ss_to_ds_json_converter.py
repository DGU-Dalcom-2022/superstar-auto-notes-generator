import json
import os
from glob import glob
OUTPUT_DIR = "./ssdsconverter_output"

class SSDSJsonConverter():
    def __init__(self):
        print('새로운 converter 생성됨. 이름 마지막에 4, 7, 13으로 난이도 설정이 되어 있지 않은 파일은 생성 불가')
        pass

    def set_output_path(self, output_path):
        self.output_path = output_path
        if not os.path.isdir(self.output_path):
            os.makedirs(self.output_path)

    def get_difficulty(self, song_idx_num):
        return {'4' : 'Easy.dat', '7' : 'Normal.dat', '13' : 'Hard.dat'}.get(song_idx_num, '-1')
    
    def convert(self, input_path, output_path):
        self.set_output_path(output_path)

        song_title = input_path.split('/')[-1].split('_')[:-1]
        song_idx_num = input_path.split('/')[-1].split('_')[-1].split('.')[0]
        song_title = '_'.join(song_title)
        song_diff = self.get_difficulty(song_idx_num)
        if song_diff == '-1':
            return print(input_path + ' : 잘못된 난이도 설정')

        self.set_output_path(self.output_path+'/'+song_title)
        output_file = open(self.output_path+'/'+song_diff, 'w')

        old_notes = json.load(open(input_path.__str__(), "r"))["notes"]
        new_note_list = []
        for idx in old_notes:
            for old_note in old_notes[idx]:
                time = old_note["sec"]
                new_note = {"_time": time, "_lineIndex": idx, "_lineLayer": 0, "_type": 0, "_cutDirection": 0}
                new_note_list.append(new_note)
        new_notes = {"_notes": sorted(new_note_list, key=lambda x: x['_time'])}

        output_file.write(json.dumps(new_notes))
        output_file.close()

if __name__ == '__main__':
    converter = SSDSJsonConverter()
    json_dir = glob('../SuperStarResource/json/*')
    for game_dir in json_dir:
        json_path_list = glob(game_dir+"/*.json")
        for json_path in json_path_list:
            converter.convert(json_path, OUTPUT_DIR+'/'+game_dir.split('/')[-1])
