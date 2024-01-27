from gtts import gTTS

texto = "Criando um script para ser transformado de texto para áudio"
idioma = 'pt'
sotaque = 'com.br'

tts = gTTS(texto, lang=idioma, tld=sotaque)

# criando a faixa de áudio
tts.save("audio.mp3")