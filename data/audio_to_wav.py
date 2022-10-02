import os
from pydub import AudioSegment


def transform_format(input_dir, output_dir):
    files_list = []

    for path in os.listdir(input_dir):
        if os.path.isfile(os.path.join(input_dir, path)):
            files_list.append(path)

    for i, file_nm in enumerate(files_list):
        print(file_nm)
        sound = AudioSegment.from_file(os.path.join(input_dir, file_nm), str(file_nm.split(".")[-1]))
        sound.export(os.path.join(output_dir, str('scream' + str(i) + ".wav")), format="wav")
        
    return

if __name__ == "__main__":
    input_dir = r'NonverbalVocalization/screaming'
    output_dir = r'train_data'
    transform_format(input_dir, output_dir)