"""Преобразование текста в речь, (c) Sayfullin Ruslan.
Пример программы, использующей возможности преобразования текста в речь
модуля pyttsx3.
"""

import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    sys.exit()

tts = pyttsx3.init()    # Инициализация механизма TTS.

print('Text To Speech Talker, by Sayfullin Ruslan')
print('Text-to-speech using the pyttsx3 module, which in turn uses')
print('the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows), or')
print('eSpeak (on Linux) speech engines.')
print()
print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('> ')

    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    tts.say(text)       # Текст, который должен произнести механизм TTS.
    tts.runAndWait()     # Запускаем произнесение этого текста механизмом TTS.
