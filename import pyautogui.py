import pyautogui
import speech_recognition as sr
import time

def rolar_para_baixo():
    pyautogui.scroll(-500)  # Ajuste a quantidade de rolagem conforme necessário

def rolar_para_cima():
    pyautogui.scroll(500)  # Ajuste a quantidade de rolagem conforme necessário

def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga 'rolar' para rolar a tela para baixo ou 'voltar' para rolar a tela para cima...")
        r.adjust_for_ambient_noise(source)  # Ajuste o reconhecimento de ruído de fundo
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Não consegui entender o comando.")
        return ""
    except sr.RequestError as e:
        print(f"Erro ao acessar o serviço de reconhecimento de fala: {e}")
        return ""

while True:
    comando = ouvir_comando()
    if "rolar" in comando:
        rolar_para_baixo()
    elif "voltar" in comando:
        rolar_para_cima()
    time.sleep(1)  # Aguarda 1 segundo antes de ouvir o próximo comando
