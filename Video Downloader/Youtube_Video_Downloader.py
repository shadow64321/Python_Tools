import customtkinter as ctk
from pytube import YouTube
from sys import argv
import os

def Download_Video_Button_Callback():
  Url = app.Url_Textbox.get('1.0', 'end')
  yt = YouTube(Url)
  app.Updateable_Label.configure(text=f'Downloading {yt.title}')
  yd = yt.streams.get_highest_resolution()
  yd.download('Downloaded-Content/Videos')
  print(f'Downloaded-Content/Videos/{yt.title}.mp4')

  # This message doesn't work correctly
  if os.path.isfile(f'Downloaded-Content/Videos/{yt.title}.mp4'):
    app.Updateable_Label.configure(text=f'Downloaded {yt.title}')
  else:
    app.Updateable_Label.configure(text=f'Failed to Download {yt.title}')
     

def Download_Audio_Button_Callback():
  Url = app.Url_Textbox.get('1.0', 'end')
  yt = YouTube(Url)
  app.Updateable_Label.configure(text=f'Downloading {yt.title}')
  t = yt.streams.filter(only_audio=True)
  downloaded_file = t[0].download('Downloaded-Content/Audio')
  base, ext = os.path.splitext(downloaded_file)
  new_file = base + '.mp3'
  os.rename(downloaded_file, new_file)
  # This message doesn't work correctly
  if os.path.isfile(f'Downloaded-Content/Audio/{yt.title}.mp3'):
    app.Updateable_Label.configure(text=f'Downloaded {yt.title}')
  else:
    app.Updateable_Label.configure(text=f'Failed to Download {yt.title}')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(0, weight=1)

        self.Welcome = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Welcome to Youtube Video Downloader')
        self.Welcome.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.Updateable_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Download Staus Unknown')
        self.Updateable_Label.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.Url_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Url: ')
        self.Url_Label.grid(row=2, column=0, sticky='nsew')
        self.Url_Textbox = ctk.CTkTextbox(self, width=500, height=20, activate_scrollbars=True, corner_radius=20)
        self.Url_Textbox.grid(row=2, column=1, padx=30, pady=20, sticky='nsew', columnspan=2)
        self.Url_Textbox.insert(index='0.0', text='https://www.youtube.com')

        self.Download_Button = ctk.CTkButton(self, text='Download Video & Audio', command=Download_Video_Button_Callback)
        self.Download_Button.grid(row=3, column=0, padx=20, pady=20, sticky='nsew', columnspan=3)

        self.Download_Button = ctk.CTkButton(self, text='Download Only Audio', command=Download_Audio_Button_Callback)
        self.Download_Button.grid(row=4, column=0, padx=20, pady=20, sticky='nsew', columnspan=3)

if __name__ == '__main__':
  app = App()
  app.title("Youtube Video Downloader")
  app.geometry("700x400")
  app.mainloop()