'''Simple script that checks your ip address, and if it has changed since the
last time the program was run, send you an email. Useful for home servers
without a static IP address. Address is saved in a file in the same directory
as the script.
'''
import os
import smtplib
from urllib.request import urlopen
#==========
#FILL OUT FEILDS BELOW
#==========

# The address of the smtp server
SMTP_SERVER = 'smtp.gmail.com:000'
# The address you wantt he email to come from
SENDER_ADDRESS = 'matthewauld@example.org'
# The Username and Password for the smtp server
SENDER_USERNAME = 'matthewauldserver@example.org'
SENDER_PASSWORD = 'password'
# The address you want the username to be sent todo
DESTINATION_ADDRESS = 'user@example.org'
# The name of this computer - if youleave it blank, it will pull from the environment variable.
COMPUTER_NAME = ''

#get the current ip address
my_ip = urlopen('http://ip.42.pl/raw').read()
my_ip = my_ip.decode("UTF-8")

#open the file that stored the ip address from the last time script was run
PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(PATH, "your_ip.txt")
config=open(CONFIG_PATH,"w+")

# Get the name of your computer
if COMPUTER_NAME is '':
	COMPUTER_NAME  = os.environ['COMPUTERNAME']

config=open(CONFIG_PATH,"r+")

"""Configure Notification Mail"""

sender = 'matthewauldserver@gmail.com'
receivers = ['matthewauld@gmail.com']

message = """From: Server <{0}>
To: Admin <{1}>
Subject: New IP Address

Hello,
I hope your date is going well. Your server '{2}'' has been assinged a new IP Address: {3}
Have a wonderful day.""".format(SENDER_ADDRESS,DESTINATION_ADDRESS,COMPUTER_NAME,my_ip)


# If the IP address has changed, send an email, and update the listed config file
if config.read() == my_ip:
	pass
else:
	try:
		server = smtplib.SMTP(SMTP_SERVER)
		server.ehlo()
		server.starttls()
		server.login(SENDER_USERNAME,SENDER_PASSWORD)
		server.sendmail(sender, receivers, message)
		server.quit()
		config.write(my_ip)
	except:
		print("Error, unable to send IP update")

config.close()
