from pytube import YouTube

def Download(link):
    youtubeObject =YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occured!")
    print("Video downloaded successfully!")

linkInput = input("Please enter the Youtube link: ")
Download(linkInput)