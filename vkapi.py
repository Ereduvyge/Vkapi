#-*-coding:utf8;-*-

import vk
import unicodedata
import re


app_id='6752155'
login='89118236470'
password='R1HWO62FMyPNftWmiCDnhxd6wb38skCeqebreTNf'

session=vk.AuthSession(app_id, login, password, scope='friends, messages')
vk_api=vk.API(session, v='5.87', lang='ru')

ids_list=[]

def sent(your,message):
    yourLove=your
    messageTo=message
    if re.match(r'^http', yourLove): 
        yourLove=yourLove.split('com/')[1]
    if re.match(r'id', yourLove):
        yourLove=yourLove.split('d')[1]
        for i in vk_api.users.get(user_ids=yourLove):
            print 'Sent!'
            vk_api.messages.send(user_ids=yourLove, message=messageTo, peer_id=yourLove)
    else:
        for i in vk_api.users.get(user_ids=yourLove):
            print 'Sent!'
            vk_api.messages.send(user_ids=yourLove, message=messageTo, domain=yourLove)

while len(ids_list)<1:
    yourLove=raw_input('Enter id or domain or link:\n->')
    ids_list.append(yourLove)

messageTo=raw_input('Enter message:\n->')


for love in ids_list:
    loh=vk_api.users.get(user_ids=love)[0]
    name = u''.join(loh['first_name']).encode('utf-8').strip()
    messageTo='%s, '% name + messageTo
    print messageTo 
