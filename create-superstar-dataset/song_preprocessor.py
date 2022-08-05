import numpy as np
import librosa
OUTPUT_DIR = "./ssdsconverter_output"

class SongPreprocessor():
    def __init__(self):
        pass

    def set_output_path(self, output_path):
        self.output_path = output_path

    def extract_features_multi_mel(self, y, sr=44100.0, hop=512, nffts=[1024, 2048, 4096], mel_dim=100):
        featuress = []
        for nfft in nffts:
            mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=mel_dim, n_fft=nfft, hop_length=hop)  # C2 is 65.4 Hz
            features = librosa.power_to_db(mel, ref=np.max)
            featuress.append(features)
        features = np.stack(featuress, axis=1)
        return features

    def extract_features_mel(self, y, sr, hop, mel_dim=100):
        mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=mel_dim, hop_length=hop)  # C2 is 65.4 Hz
        features = librosa.power_to_db(mel, ref=np.max)
        return features

    def preprocess(self, song_path, feature_name='mel', feature_size=100, sampling_rate=44100.0, step_size=0.01, using_bpm_time_division="store_true"):
        song_title = song_path.split('/')[-1]
        output_file_name = self.output_path+'/'+song_title+'.npy'
        # get song
        y_wav, sr = librosa.load(song_path, sr=sampling_rate)

        sr = sampling_rate
        hop = int(sr * step_size)

        #get feature
        if feature_name == "mel":
            features = self.extract_features_mel(y_wav, sr, hop, mel_dim=feature_size)
        elif feature_name == "multi_mel":
            features = self.extract_features_multi_mel(y_wav, sr=sampling_rate, hop=hop, nffts=[1024,2048,4096], mel_dim=feature_size)

        np.save(output_file_name, features)

if __name__ == '__main__':
    preprocessor = SongPreprocessor()
    preprocessor.set_output_path(OUTPUT_DIR)
    preprocessor.preprocess('../SuperStarResource/json/SSAT/210623_ateez_promise_2.ogg')
