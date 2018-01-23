import sys
import socket 
import os

TCP_IP = "127.0.0.1"
TCP_PORT = 5017
fileImage = 'file_image.jpg'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Image:", fileImage


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(10)

while 1:
    data,addr = sock.accept()
    newFoder = r'Foder Upload/' 
    if not os.path.exists(newFoder):
        os.makedirs(newFoder)

    fileUpload = open(newFoder+fileImage,"wb")
    sData = data.recv(1024)
    while sData:
        fileUpload.write(sData)
        sData = data.recv(1024)
    print "Upload Completed"
sock.close()
