#Marvell
#OWlTeam
#Thanks To - OWlTeam - ILHAM - SatriaXGanz
#RAYNER.WIBU - Lr.13.ID - FRANKER - Mr.MTAS
#A19XPLOIT - Tn.House
#KeylaCans - Marvell
#ALL MEMBER </>

from requests import Session
import re, sys
s = Session()

try:
	print("SMS Gratis By Marvell - OWlTeam\nGunakan kode negara (ex: 62xxxxxx5)")
	no = int(input("No    : "))
except:
	print("\n\t* Check your number phone! *")
	sys.exit()
msg = input("Pesan : ")

if len(msg) < 10:
	print('\n\t* Pesan yang dikirimkan minimal 10 karakter *')
	sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    'Referer': 'http://sms.payuterus.biz/alpha/'
}

bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
	'nohp':no,
	'pesan':msg,
	'captcha':captcha,
	'key':key
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if 'SMS Gratis Telah Dikirim' in send:
	print(f"\nSukses dikirim! \n[{no}] => {msg}")
elif 'MAAF....!' in send:
	print("\n\t* Mohon Tunggu 15 Menit Lagi Untuk Pengiriman Pesan Yang Sama *")
elif 'Pesan yang dikirimkan minimal 10 karakter' in send:
	print('\n\t* Pesan yang dikirimkan minimal 10 karakter *')
else:
	print("\n\t* Gagal dikirim! Silahkan Coba Lagi*")
  
