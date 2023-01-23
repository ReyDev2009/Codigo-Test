from pytube import YouTube

def download():
    link = str(input("Copy your link here: "))
    quality = input("Quality: ")
    
    yt = YouTube(link)
    print(f'\n Dowloading:\n Nombre: {yt.title}\n Youtuber: {yt.author}\n Duration: {round(yt.length / 60, 2)} minutes')
    stream = yt.streams.get_highest_resolution(quality)     
    stream.download()
    print("\n File is downloaded succefull")
