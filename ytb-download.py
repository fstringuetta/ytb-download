#!/usr/bin/python
from pytube import YouTube
import moviepy.editor as mp
import re,os

# Limpando a tela
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Cabecalho do aplicativo
print ('==='*7)
print ('=== YTB-Download ===')
print ('==='*7)

# Digite o link do video
link = input('Digite o link do video: ')
path = input('Digite o diretorio que deseja salvar: ')
opcao = input('Deseja musica ou video: ')
yt = YouTube(link)

# Realiza download do video em .mp4
if opcao == 'video':
	print ('Baixando...')
	ys = yt.streams.first().download(path)
	print ('Download completo!')
else:
# Realiza o download do video .mp4 para converter em .mp3
	print ('Baixando...')
	ys = yt.streams.filter(only_audio=True).first().download(path)
	print ('Download completo!')

# Converte de mp4 para mp3
	print ('Convertendo arquivo...')
	for file in os.listdir(path):
	    if re.search('mp4', file):
	        mp4_path = os.path.join(path, file)
        	mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        	new_file = mp.AudioFileClip(mp4_path)
        	new_file.write_audiofile(mp3_path)
        	os.remove(mp4_path)
	print('Sucesso!')
