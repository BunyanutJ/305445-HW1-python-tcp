import sys
import socket 

TCP_IP = "127.0.0.1"
TCP_PORT = 5017
fileImage = 'file_image.jpg'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Image:", fileImage

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

fUploadFile = open(fileImage,"rb")
sRead = fUploadFile.read(1024)
while sRead:
    sock.send(sRead)
    sRead = fUploadFile.read(1024)
print "Sending the Image Completed"
