import customtkinter as ctk
import requests
import shutil

def Download(url: str, username: str, password: str):
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0" # other args in curly braces include: X11; Ubuntu; Linux x86_64;
  }

  with requests.get(
    f'https://www.netflix.com/{url}',
    stream=True,
    auth=(username, password),
    headers=headers,
  ) as response:
    with open('output.mp4', 'wb') as file:
      shutil.copyfileobj(response.raw, file)

def main():
  Username = app.Username_Textbox.get('1.0', 'end')
  Password = app.Password_Textbox.get('1.0', 'end')
  Url = app.Url_Textbox.get('1.0', 'end')
  Download(Url, Password, Username)

def Download_Button_Callback():
  main()
  Username = app.Username_Textbox.get('1.0', 'end')
  Password = app.Password_Textbox.get('1.0', 'end')
  Url = app.Url_Textbox.get('1.0', 'end')
  app.Updateable_Label.configure(text=f'Attempting download:\n Username: {Username}\n Password: {Password}\n Url: {Url}')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(0, weight=1)

        self.Welcome = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Welcome to Netflix Movie and TV Show Downloader')
        self.Welcome.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.Updateable_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Download Staus Unknown')
        self.Updateable_Label.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.Username_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Username: ')
        self.Username_Label.grid(row=2, column=0, sticky='nsew')
        self.Username_Textbox = ctk.CTkTextbox(self, width=300, height=20, activate_scrollbars=True, corner_radius=20)
        self.Username_Textbox.grid(row=2, column=1, padx=30, pady=20, sticky='nsew', columnspan=2)
        self.Username_Textbox.insert(index='0.0', text='HelloFriend123@Gmail.com')

        self.Password_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Password: ')
        self.Password_Label.grid(row=3, column=0, sticky='nsew')
        self.Password_Textbox = ctk.CTkTextbox(self, width=300, height=20, activate_scrollbars=True, corner_radius=20)
        self.Password_Textbox.grid(row=3, column=1, padx=30, pady=20, sticky='nsew', columnspan=2)
        self.Password_Textbox.insert(index='0.0', text='Password123')

        self.Url_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Url: ')
        self.Url_Label.grid(row=4, column=0, sticky='nsew')
        self.Url_Textbox = ctk.CTkTextbox(self, width=300, height=20, activate_scrollbars=True, corner_radius=20)
        self.Url_Textbox.grid(row=4, column=1, padx=30, pady=20, sticky='nsew', columnspan=2)
        self.Url_Textbox.insert(index='0.0', text='https://www.netflix.com')

        self.Download_Button = ctk.CTkButton(self, text='Download', command=Download_Button_Callback)
        self.Download_Button.grid(row=5, column=0, padx=20, pady=20, sticky='nsew', columnspan=3)

if __name__ == '__main__':
  app = App()
  app.title("Netflix Downloader")
  app.geometry("500x500")
  app.mainloop()
