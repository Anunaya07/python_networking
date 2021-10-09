import socket

target_host="127.0.0.1"
target_port=9997

#create a socket
client =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#AF_INET --> IPV4
#SOCK_DGRAM --> UDP client

#send some data
client.sendto(b"AAABBBCCC", (target_host,target_port))

#UDP is a connectionless protocol

#recieve some data
data ,addr =client.recvfrom(4096)

print(data.decode())
client.close()