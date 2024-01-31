import pytube

video_url = input("Enter the video url")
audiovideo = input("Do you want audio or video")

if audiovideo == "audio":
    yt = pytube.YouTube(video_url)
    video = yt.streams.get_audio_only()
    path = fr"C:\Users\Admin\Desktop\yt-downlaod\out\{video.itag}.mp3"
    video.download(path)
    print("Downloaded")

elif audiovideo == "video":
    yt = pytube.YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    path = fr"C:\Users\Admin\Desktop\yt-downlaod\out\{video.itag}.mp4"
    video.download(path)
    print("Downloaded")

else:
    print("Invalid input")
