from gtts import gTTS
import os 

texto = "Criando um script para ser transformado de texto para áudio"
idioma = 'pt'
sotaque = 'com.br'

tts = gTTS(texto, lang=idioma, tld=sotaque)

# criando a faixa de áudio
tts.save("audio.mp3")


#rodando o áudio de forma automática
os.system('ffplay -autoexit -nodisp audio.mp3')
# -autoexit: para encerrar após o fim da mensagem
# -nodisp: para nao abrir o display

