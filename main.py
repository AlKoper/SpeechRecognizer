import whisper

# основная функиция, в которой будет происходить транскрибация аудио файла
def speech_recognition(model='base'):    # whisper предлагает 5 разных моделей дла обрабокти звука, по умолчанию используем base
    speech_model = whisper.load_model(model)  # загрузим модель
    result = speech_model.transcribe('/media/andrew/75A74AA74301978F/PycharmProjects/SpeechRecognizer/Input/1.mp3', fp16=False)    #выполняем трансрибацию текста
    with open(f'transcription_{model}.txt', 'w') as file:    #сохраняем полученный текст в файл
        file.write(result['text'])

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