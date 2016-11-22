import webbrowser
import time

songUrl = 'https://www.youtube.com/watch?v=ktvTqknDobU'

# chrome=webbrowser.get('open -a /Applications/Google\ Chrome.app %s')
#
# webbrowser.open(songUrl, True)

max=3
now=0
print("Program started at " + time.ctime())
while now < max:
    webbrowser.open(songUrl, True)
    time.sleep(10)
    now += 1


#simplified command to open url
# chrome.open(songUrl)