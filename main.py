from bs4 import BeautifulSoup
import emoji
import re

file=open('snapchat.html',"r",encoding='utf-8')
soup = BeautifulSoup(file,'html.parser')

text=soup.get_text()
index=text.find('New Chat')
text=text[:index]
text=emoji.replace_emoji(text,' ')
text=text.split(' ')[2:]

name=' '.join(text)

print(name,"sent a new message")