import webbrowser

chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
u='https://app.gotomeeting.com/?meetingId='

code=input("Enter the access code or paste the link:").strip()
v=""

for i in code:
    if i.isdigit():
        v+=i
url=u+v
webbrowser.get(chrome).open(url)
