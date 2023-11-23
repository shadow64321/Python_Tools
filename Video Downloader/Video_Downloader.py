from pytube import YouTube
from sys import argv
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

    print(f'Downloading {Name}')
    yd.download('Downloaded-Content')

    #if os.path.isfile(f'~/Videos/{Name}'):
    #    print(f'{Name} Downloaded')
    #else:
    #    print(f'Error occured while downloading {Name}')

elif 2 == Usr_Input:
    print(f'Downloading {Name}')
    yt.streams.get_audio_only(link)
    
    if os.path.isfile('Downloaded-Content/{Name}'):
        print(f'{Name} Downloaded')
    else:
        print(f'Error occured while downloading {Name}')
