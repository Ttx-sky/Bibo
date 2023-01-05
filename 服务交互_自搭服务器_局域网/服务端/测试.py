import socket
import os
import datetime



#，创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2建立连接
sk.connect(('192.168.1.5', 5000))
data = sk.recv(2048)
print(data.decode('utf-8'))

#3传输据
def data():
   f = input('>>>')
   if f == 'kill':
       sk.send('客户端关闭'.encode('utf-8'))
       data = sk.recv(2048)
       print('服务端数据：', data.decode('utf-8'))
       sk.close()
       os._exit(0)
   sk.send(f.encode('utf-8'))
   data = sk.recv(2048)
   print('服务端数据：', data.decode('utf-8'))

def Time_Now():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("当前时间:", current_time)
Time_Now()
while True:
    data()

sk.close()