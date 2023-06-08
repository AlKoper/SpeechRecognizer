import whisper
from time import time
from pathlib import Path

# основная функиция, в которой будет происходить транскрибация аудио файла
def speech_recognition(model='base'):    # whisper предлагает 5 разных моделей дла обрабокти звука, по умолчанию используем base
    start_time = time()
    speech_model = whisper.load_model(model)  # загрузим модель
    input_files = Path('D:\Audio&Image editing\SpeechRecognizer\Input audio').glob('*.mp3')    #пробежимся по всем mp3 йафлам в папке
    for audio_file in input_files:
        file_name = Path(audio_file).stem
        print(audio_file)
        print(file_name)
        result = speech_model.transcribe(str(audio_file), fp16=False)    #выполняем транскрибацию аудио файла
        with open(f'D:\Audio&Image editing\SpeechRecognizer\Output texts\{file_name}_{model}.txt', 'w') as file:    #сохраняем полученный текст в файл
            file.write(result['text'])
    end_time = time()
    print(f'Транскрибация завершена за {int(end_time-start_time)} секунд')

def main():
    trans_models = {1: 'tiny', 2: 'base', 3: 'small', 4: 'medium', 5: 'large'}    #создадим список доступных моделей для дальнейшего выбора и покажем их
    for n, m in trans_models.items():
        print(f'{n}:{m}')

    user_model = int(input('Выберите модель для транскрибации, указав соответствующий номер: '))    #предлагаем пользователю выбрать модель трансрибации
    if user_model not in trans_models.keys():
        raise KeyError(f'Модель {user_model} отсутствует в списке')

    print('Выполняю процесс транскрибации, немного подождите... ')    #Запускаем
    speech_recognition(model=trans_models[user_model])

if __name__ == '__main__':
    main()