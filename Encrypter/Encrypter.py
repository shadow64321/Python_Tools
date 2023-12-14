import customtkinter as ctk
import base64, os

def Encrypt():
  x = app.Encrypted_File_Textbox.get('1.0', 'end-1c')
  app.Updateable_Label.configure(text=f'Encrypting {x}')
  f = open(x, 'r')
  data = f.read()
  f.close()
  Encoded_Bytes = base64.b64encode(data.encode())
  f = open('Encrypted_Data.txt', 'wb')
  f.write(Encoded_Bytes)
  f.close
  app.Updateable_Label.configure(text=f'Encrypted {x}')

def Decrypt():
  x = app.Encrypted_File_Textbox.get('1.0', 'end-1c')
  if os.path.isfile(x):
    app.Updateable_Label.configure(text=f'Decrypting')
    f = open(x, 'rb')
    Encrypted_Str = f.read()
    f.close()
    Decrypted_Str = base64.b64decode(Encrypted_Str.decode())
    f = open('Decrypted_Data.txt', 'wb')
    f.write(Decrypted_Str)
    f.close()
    app.Updateable_Label.configure(text=f'Decrypted Data: {Decrypted_Str}')
  else:
    app.Updateable_Label.configure(text=f'Failed to decrypt data')
    exit

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.grid_columnconfigure(0, weight=1)

    self.Updateable_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='')
    self.Updateable_Label.grid(row=1, column=0, columnspan=3, sticky='nsew')

    self.Encrypted_File_Label = ctk.CTkLabel(master=self, width=400, corner_radius=0, text='Encrypted File or File to Encrypt: ')
    self.Encrypted_File_Label.grid(row=2, column=0, sticky='nsew')
    self.Encrypted_File_Textbox = ctk.CTkTextbox(self, width=500, height=20, activate_scrollbars=True, corner_radius=20)
    self.Encrypted_File_Textbox.grid(row=2, column=1, padx=30, pady=20, sticky='nsew', columnspan=2)
    self.Encrypted_File_Textbox.insert(index='0.0', text='file.txt')

    self.Encrypt_Button = ctk.CTkButton(self, text='Encrypt', command=Encrypt)
    self.Encrypt_Button.grid(row=4, column=0, padx=20, pady=20, sticky='nsew', columnspan=3)
    self.Decrypt_Button = ctk.CTkButton(self, text='Decrypt', command=Decrypt)
    self.Decrypt_Button.grid(row=5, column=0, padx=20, pady=20, sticky='nsew', columnspan=3)

if __name__ == '__main__':
  app = App()
  app.title("Encrypter")
  app.geometry("800x400")
  app.mainloop()