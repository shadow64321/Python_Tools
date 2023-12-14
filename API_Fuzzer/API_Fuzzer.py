import customtkinter as ctk
import requests
import json as jf

def API_Fuzz():
  Url = app.Url_Textbox.get('1.0', 'end')
  Wordlist = app.Wordlist_Textbox.get('1.0', 'end-1c')
  f = open(f'{Wordlist}', 'r')
  Wordlist_Data = f.readlines()
  for word in Wordlist_Data:
    res = requests.get(url=f'{Url}/{word}')
    if res.status_code == 404:
      API_Fuzz()
    else:
      data = res.json()
      x = jf.dumps(data, separators=('\n'))
      f = open(f'Logs/Log.json', 'w')
      f.write(x)
      f.close()
  API_Fuzz()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(0, weight=1)

        self.Welcome = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Welcome to my API Fuzzer')
        self.Welcome.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.Updateable_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Fuzz Status Unknown')
        self.Updateable_Label.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.Url_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Url: ')
        self.Url_Label.grid(row=2, column=0, sticky='nsew')
        self.Url_Textbox = ctk.CTkTextbox(self, width=500, height=20, activate_scrollbars=True, corner_radius=20)
        self.Url_Textbox.grid(row=2, column=1, padx=30, pady=20, sticky='nsew', columnspan=2)
        self.Url_Textbox.insert(index='0.0', text='https://www.google.com')

        self.Wordlist_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Wordlist (Search starts in current dir): ')
        self.Wordlist_Label.grid(row=3, column=0, columnspan=2, sticky='nsew')
        self.Wordlist_Textbox = ctk.CTkTextbox(self, width=500, height=20, activate_scrollbars=True, corner_radius=20)
        self.Wordlist_Textbox.grid(row=3, column=2, padx=30, pady=20, sticky='nsew', columnspan=2)
        self.Wordlist_Textbox.insert(index='0.0', text='Wordlist.txt')

        self.Api_Fuzz_Button = ctk.CTkButton(self, text='Fuzz API', command=API_Fuzz)
        self.Api_Fuzz_Button.grid(row=4, column=0, padx=20, pady=20, sticky='nsew', columnspan=3)

if __name__ == '__main__':
  app = App()
  app.title("API Fuzzer")
  app.geometry("800x400")
  app.mainloop()