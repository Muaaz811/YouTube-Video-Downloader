from pytube import YouTube


def download(link):
    yobj = YouTube(link)
    yobj = yobj.streams.get_highest_resolution()


def downloadByQuality(link, quality):
    yobj = YouTube(link)
    if quality == "1080p":
        yobj = yobj.streams.get_by_resolution(resolution="1080p")
    elif quality == "720p":
        yobj = yobj.streams.get_by_resolution(resolution="720p")
    elif quality == "480p":
        yobj = yobj.streams.get_by_resolution(resolution="480p")
    elif quality == "360p":
        yobj = yobj.streams.get_by_resolution(resolution="360p")
    try:
        print("Downloading....")
        yobj.download()
    except:
        print("Internet Connection Failed or link is invalid")


print("Video Downloaded")

if __name__ == "__main__":
    link = input("Enter Youtube video link - ")
    print()
    print()
    print("Video Quality")
    print("1.1080p")
    print("2.720p")
    print("3.480p")
    print("4.360p")
    quality = int(input("Please select the download Quality - "))
    if quality == 1:
        downloadByQuality(link, "1080p")
    elif quality == 2:
        downloadByQuality(link, "720p")
    elif quality == 3:
        downloadByQuality(link, "480p")
    elif quality == 2:
        downloadByQuality(link, "360p")
