#We are importing webbrowser to access the webbrowser
import webbrowser

#setting the Directory for chrome browser
chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#This the url prefix for the gotomeeting.
u='https://app.gotomeeting.com/?meetingId='

code=input("Enter the access code or paste the link:").strip()
v=""
#To seperate digits from the string we are using this for loop.
for i in code:
    if i.isdigit():  #this seperates the digits.
        v+=i
url=u+v   #Concadenating the digit and url prefix to a variable.
webbrowser.get(chrome).open(url)
#Opening Chrome webbrowser with that url
