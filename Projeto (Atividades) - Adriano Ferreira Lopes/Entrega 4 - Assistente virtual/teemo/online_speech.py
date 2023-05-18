import speech_recognition as sr

# Criar um reconhecedor de voz
r = sr.Recognizer()

# Abrir o microfone para capturar áudio
with sr.Microphone() as source:
    while True:
        # Definir microfone como fonte de áudio
        audio = r.listen(source)
        
        try:
            print(r.recognize_google(audio, language='pt'))
        except sr.UnknownValueError:
            print("Não entendi, por favor repita")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

