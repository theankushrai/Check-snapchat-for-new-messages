from bs4 import BeautifulSoup
import emoji
import re
import plyer
from plyer import notification

file=open('snapchat.html',"r",encoding='utf-8')
soup = BeautifulSoup(file,'html.parser')

text=soup.get_text()

#cleaning data
text=emoji.replace_emoji(text,' ') #replacing all the emojis
text=re.split("New Chat",text)
text=text[:-1] #removing last li because its not required

message=""
for it in text:
    it=it.split(' ')[-2:] #name of a person
    name=' '.join(it) #join the name back
    message+=name+" sent a new message !!\n"
    
 
notification.notify( #notification from plyer
            title="New Message",
            message=message,
            app_name="Message Reminder",
            timeout=10  # Duration the notification stays on the screen (in seconds)
        )
    



