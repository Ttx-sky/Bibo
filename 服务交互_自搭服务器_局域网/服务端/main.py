import socket
import os
# from snownlp import SnowNLP
import mkcloud

# 创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2，绑定地址
sk.bind(('192.168.1.5', 5000))

# 3，坚挺连接请求
sk.listen(10)  # ，半连接池大小
print('服务器已启动，在5000端口等待客户端连接')

# 4，取出链接请求，开始服务
conn, addr = sk.accept()
print('连接对象:', conn)
print('客户端ip+端口：', addr)

# 5，数据传输
print('======聊天机器人_启动======')
conn.send('======聊天机器人_启动======'.encode('utf-8'))


def data():
    data = conn.recv(2048)
    data = data.decode("UTF-8")
    print('客户端数据:', data)
    response = mkcloud.robot.chat(data)
    text1 = response
    print('人工智能数据：', response)
    conn.send(response.encode('utf-8'))
    if data == '客户端关闭':
        conn.send('服务端关闭'.encode('utf-8'))
        conn.close()
        os._exit(0)


# data()
while True:
    data()

# 6，结束服务
