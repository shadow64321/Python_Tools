import requests
chunk_size = 256
url = input('Paste the url you wish to download from here: ')
r = requests.get(url, stream=True)
with open('Video.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)
