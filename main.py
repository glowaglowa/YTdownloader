from pytube import YouTube, exceptions
import os

try:
    video_link = input("Paste the Youtube video URL: \n")
    yt = YouTube(video_link)

    print("Title: ", yt.title)
    print("Lenght", yt.length, "seconds")
    print("Views: ", yt.views)

    mp3_mp4 = input("Choose extention: MP3 / MP4 / 1080p \n")

    if mp3_mp4.lower() == "mp3":
        print("Downloading...")
        mp3 = yt.streams.get_audio_only()
        downloaded_mp3 = mp3.download(output_path="D:\Pythonprojekty\YTdownloaderDOWNLOADS\music")
        print("Mission accomplished!")

        print("Change from MP4 to MP3...")
        base, ext = os.path.splitext(downloaded_mp3)
        new_file = base + ".mp3"
        os.rename(downloaded_mp3, new_file)
    elif mp3_mp4.lower() == "mp4":
        print("Downloading...")
        mp4 = yt.streams.get_highest_resolution()
        downloaded_mp4 = mp4.download(output_path="D:\Pythonprojekty\YTdownloaderDOWNLOADS\movies")
        print("Mission accomplished!")
    elif mp3_mp4.lower() == "1080p":
        print("Downloading...")
        mp4_without_audio = yt.streams.filter(res="1080p", progressive=False).first()
        downloaded_mp4_without_audio = mp4_without_audio.download(
            output_path="D:\Pythonprojekty\YTdownloaderDOWNLOADS\movies")
        print("Mission accomplished!")
    else:
        print("Wrong value, try again.")

except exceptions.RegexMatchError:
    print("This is not a valid youtube video link: {}".format(video_link))

except exceptions.ExtractError:
    print('An extraction error occurred for the video: {}'.format(video_link))

except exceptions.VideoUnavailable:
    print('The following video is unavailable: {}'.format(video_link))
