#-*-coding:utf8;-*-

import vk
import re
import pyperclip
import time

while 1:
    app_id=''
    login=''
    password=''

    try:
        needed=int(input('\nEnter user:\n->'))
    except:
        print('Только номер!')
        continue
        
    try:
        file=open('list.txt','r')
        with file as fp:
            for i, line in enumerate(fp):
                if i == needed:
                    login=line.split(' ')[0]
                    password=line.split(' ')[1]
                    app_id=line.split(' ')[2]
    except:
        print('#404')
        continue

    try:
        session=vk.AuthSession(app_id, login, password, scope='friends, messages')
        vk_api=vk.API(session, v='5.87', lang='ru')
    except:
        print('Данные неверны или приложение устарело!')
        continue
        
    ids_list=[]

    def sent(your,message):
        yourLove=your
        messageTo=message
        if re.match(r'^http', yourLove):
            yourLove=yourLove.split('com/')[1]
        if re.match(r'id', yourLove):
            yourLove=yourLove.split('d')[1]
            for i in vk_api.users.get(user_ids=yourLove):
                print ('Sent!')
                vk_api.messages.send(user_ids=yourLove, message=messageTo, peer_id=yourLove)
        else:
            for i in vk_api.users.get(user_ids=yourLove):
                print ('Sent!')
                vk_api.messages.send(user_ids=yourLove, message=messageTo, domain=yourLove)

    def check(perid,has):
        if has==1:
            try:
                mesid=vk_api.messages.send(user_ids=perid, peer_id=perid, message='1')
                time.sleep(1)
                vk_api.messages.delete(message_ids=mesid, delete_for_all=1)
                return True
            except:
                return False
        else:
            try:
                mesid=vk_api.messages.send(user_ids=perid, domain=perid, message='1')
                time.sleep(1)
                vk_api.messages.delete(message_ids=mesid, delete_for_all=1)
                return True
            except:
                return False


    while len(ids_list)<21:
        hasdom=0
        if re.match(r'^http',pyperclip.paste()):
            yourLove=pyperclip.paste()
            if re.match(r'id', yourLove):
                yourLove=yourLove.split('d')[1]
                hasdom=1
            else:
                yourLove=yourLove.split('com/')[1]
                hasdom=0
            if yourLove not in ids_list:
                if check(yourLove,hasdom)==True:
                    print(yourLove)
                    ids_list.append(yourLove)
                    if len(ids_list)<21:
                        print('Добавь еще %d ссылок' % (21-len(ids_list)))
                else:
                    time.sleep(2)
            else:
                time.sleep(2)
        else:
            time.sleep(2)

    messageTo=input('Enter message:\n->')


    for love in ids_list:
        loh=vk_api.users.get(user_ids=love)[0]
        try:
            messageUp='%s, '% loh['first_name'] + messageTo
        except:
            name= u''.join(loh['first_name']).encode('utf-8').strip()
            messageUp='%s, ' % name + messageTo
        sent(love,messageUp)

exit=input()
