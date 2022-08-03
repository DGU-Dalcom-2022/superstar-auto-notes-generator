import json
import os

class SSDSJsonConverter():
    def __init__(self, output_path):
        self.output_path = output_path
        if not os.path.isdir(self.output_path):
            os.makedirs(self.output_path)
    
    def convert(self, input_path):
        self.input_path = input_path
        output_file = open(self.output_path+self.input_path.split('/')[-1], 'w')

        old_notes = json.load(open(self.input_path.__str__(), "r"))["notes"]
        new_note_list = []
        for idx in old_notes:
            for old_note in old_notes[idx]:
                time = old_note["sec"]
                new_note = {"_time": time, "_lineIndex": idx, "_lineLayer": 0, "_type": 0, "_cutDirection": 0}
                new_note_list.append(new_note)
        new_notes = {"_notes": sorted(new_note_list, key=lambda x: x['_time'])}

        output_file.write(json.dumps(new_notes))
        output_file.close()

converter = SSDSJsonConverter("./ssdsconverter_output/")
converter.convert("./SuperStarResource/json/SSM/SHINee_Love_Sick_13.json")