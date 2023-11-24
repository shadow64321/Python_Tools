from pytube import YouTube
from sys import argv
import subprocess
import os


# link must be placed in ''
link = argv[1] # Takes first arg specified when runing the program
yt = YouTube(link)
Thumbnail = yt.thumbnail_url
Name = yt.title

print('1) Video')
print('2) Audio')
Usr_Input = int(input('Would you like to download an Audio or Video file? '))


if 1 == Usr_Input:

    yd = yt.streams.get_highest_resolution()
    # yd = yt.streams.filter(progressive=True).filter(mime_type='video/webm').first()
    print(f'Downloading {Name}')
    # Get Audio
    #t=yt.streams.filter(only_audio=True)
    #downloaded_file = t[0].download('Downloaded-Content/Audio')
    #base, ext = os.path.splitext(downloaded_file)
    #new_file = base + '.mp3'
    #os.rename(downloaded_file, new_file)
    # Get Video
    yd.download('Downloaded-Content/Videos')
    #Combine
    #command = 'vlc ' + Name + '.mp4 ' + new_file + ' --sout="#gather:std{access=file, mux=ts, dst=final.mp4}" --sout-keep'
    #os.system(command)

    print(f'Downloaded {Name}')

    #if os.path.isfile(f'~/Videos/{Name}.mp4'):
    #    print(f'{Name} Downloaded')
    #else:
    #    print(f'Error occured while downloading {Name}')

elif 2 == Usr_Input:
    print(f'Downloading {Name}')
    t=yt.streams.filter(only_audio=True)
    downloaded_file = t[0].download('Downloaded-Content/Audio')
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    print(f'Downloaded {Name}')
    
    #if os.path.isfile('Downloaded-Content/{Name}' + '.mp4'):
    #    print(f'{Name} Downloaded')
    #else:
    #    print(f'Error occured while downloading {Name}')

else:
    print('Error: Selection invalid')
    exit
