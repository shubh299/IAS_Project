import socket
from random import randint
import time
v=socket.socket()
port=4001
v.bind(("127.0.0.30",port))
v.listen(5)
conn,addr=v.accept()
while(1):
    print("waiting..gps")
    x, y = randint(0, 7), randint(0, 7)
    data=str(x)+":"+str(y)
    print(data)
    conn.send(data.encode())
    time.sleep(2)
conn.close()
v.close()