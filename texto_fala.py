from gtts import gTTS
import os 

texto = "Criando um script para ser transformado de texto para áudio"
idioma = 'pt'
sotaque = 'com.br'

tts = gTTS(texto, lang=idioma, tld=sotaque)

# criando a faixa de áudio
tts.save("audio.mp3")


#rodando o áudio de forma automática
os.system('ffplay audio.mp3')

