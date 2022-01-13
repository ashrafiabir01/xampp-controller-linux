# author : me
import os 
os.system("clear")
print('''\033[91m
██╗░░██╗░█████╗░███╗░░░███╗██████╗░██████╗░
╚██╗██╔╝██╔══██╗████╗░████║██╔══██╗██╔══██╗
░╚███╔╝░███████║██╔████╔██║██████╔╝██████╔╝
░██╔██╗░██╔══██║██║╚██╔╝██║██╔═══╝░██╔═══╝░
██╔╝╚██╗██║░░██║██║░╚═╝░██║██║░░░░░██║░░░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░░░░ \033[00m''')
print("\n\n\n 1. Start Xampp server")
print("\n 2. Stop Xampp server")
print("\n 3. Run Xampp controll panel")
print("\n\n")
option= int(input("e͟x͟e͟c͟u͟t͟e͟ > "))

if option==1:
   os.system("sudo service mysql stop")
   os.system("sudo service apache2 stop")
   os.system("sudo /opt/lampp/lampp start")
elif option==2:
   os.system("sudo service mysql stop")
   os.system("sudo service apache2 stop")
   os.system("sudo /opt/lampp/lampp stop")
elif option==3:
   os.system("sudo /opt/lampp/manager-linux-x64.run")
else :
   exit()
