import pytube
link = " Link Here"
yt = pytube.YouTube(link)
print("Title:", yt.title)
print("Author:", yt.author)
print("Length of video:", yt.length, "seconds")
yt.streams.get_highest_resolution().download()
print("Video successfullly downloaded from", link)
