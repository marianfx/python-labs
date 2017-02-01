
###########
# SOCKETS
###########

# SERVER TCP
ip_port = ("127.0.0.1", 6996)
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IpV4, TCP
s.bind(ip_port)
s.listen()
while True:
    connection, address = s.accept() # wait to accept
    while True:
        data = connection.recv(2048).decode("UTF-8") # buffered, need to decode
        if not data:
            break
    connection.close() # close connection with the current user

# Client TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IpV4, TCP
s.connect(ip_port)
s.send(str("Marian").encode("UTF-8"))
s.close()

# Server UDP
# remove the 'listen' part
# to receive: data, addrinfo = s.recvfrom(2048)

# Client UDP
# the esame as in server - to receive, use bind first, otherwise use sendto



#############
# URLLIB
############
import urllib
from urllib import request
response = urllib.request.urlopen("path_to_url").read()


#############
# FTP
############
from ftplib import FTP
client = FTP("ftp.debian.org")
commandLIST = "LIST /debian/" # listdir
commandRETR = "RETR /debian/extrafiles" # dl
# list
client.retrlines(commandLIST, lambda line: print(line))
# dl
localdir = open("Dir", "wb")
client.retrbinary(commandRETR, lambda buf: localdir.write(buf))
localdir.close()
client.quit()



###############
# SMTP
###############
import smtplib
MIMEText = lambda x: x
# also this, but on top => from email.MIMEText import MIMEText
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login("<user_name>@gmail.com", "<Password>")
msg = MIMEText("My first email")
msg['Subject'] = "First email"
msg['From'] = "<user_name>@gmail.com"
msg['To'] = "<recipient email address>"
# mail.sendmail("<from>", "<to>", msg.as_string())
mail.quit()


###############
# SIMPLE HTTP
##############
#1. run python -m http.server 9000 OR:
import http.server
import socketserver
srv_address = ("127.0.0.1", 6996)
httpd = socketserver.TCPServer(srv_address, http.server.SimpleHTTPRequestHandler) # displays dir the simple one
print("Server started on {0}:{1}.\n".format("127.0.0.1", str(6996)))
httpd.serve_forever()