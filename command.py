import os
import time
print("""
	press 1 : notepad
	press 2 : msword
	press 3 : gmail
	press 4 : web whatsapp
""")
inp=int(input("\nenter the no. to open your app"))

if inp==1:
	time.sleep(5)
	os.system("notepad")
elif inp==2:
	time.sleep(5)
	os.system("start msword")
elif inp==3:
	time.sleep(5)
	os.system("start chrome gmail.com")
elif inp==4:
	time.sleep(5)
	os.system("start chrome webwhatsapp.com")
else:
	print("your input is wrong")