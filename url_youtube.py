import sys
import requests

def playonyt(topic):
    """Will play video on following topic, takes about 10 to 15 seconds to load"""
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        raise Exception("No video found.")
    
    # print("Videos found, opening most recent video")
    # web.open("https://www.youtube.com"+lst[count-5])
    return "https://www.youtube.com"+lst[count-5]

# print(playonyt("tu tas dura sin ir al gym"))
song = sys.argv
del song[0]
del song[0]
cancion = " ".join(song)
# print(sys.argv)
# print(cancion)
print(playonyt(cancion))
# print(playonyt("cancion de amor"))
