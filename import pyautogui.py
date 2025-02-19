import pyautogui
import speech_recognition as sr
import time

def move_mouse(direction, duration=1):
    if direction == 'chima':
        pyautogui.moveRel(0, -100, duration)
    elif direction == 'direita':
        pyautogui.moveRel(100, 0, duration)
    elif direction == 'esquerda':
        pyautogui.moveRel(-100, 0, duration)
    elif direction == 'baixo':
        pyautogui.moveRel(0, 100, duration)
    else:
        print("Direção não reconhecida. Use 'chima', 'direita', 'esquerda' ou 'baixo'.")

def click_mouse():
    pyautogui.click()

def double_click_mouse():
    pyautogui.doubleClick()

def listen_and_execute():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga a direção (chima, direita, esquerda, baixo) ou 'Click' para clicar ou 'Duplo Click' para clicar duas vezes:")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {command}")
                if command.lower() == 'click':
                    click_mouse()
                elif command.lower() == 'duplo click':
                    double_click_mouse()
                else:
                    move_mouse(command.lower())
                break
            except sr.UnknownValueError:
                print("Não entendi o comando. Por favor, repita.")
            except sr.RequestError:
                print("Erro ao se comunicar com o serviço de reconhecimento de fala. Tentando novamente...")

# Exemplo de uso
while True:
    listen_and_execute()
    time.sleep(1)  # Esperar 1 segundo antes de ouvir o próximo comando
