import socket
from _thread import *
import pickle
from ignore import HOST, PORT

def sockctConn():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print ('>> Connect Server')
    return client_socket


# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
# def recv_data(client_socket) :
#     while True :
#         data = client_socket.recv(1024)
        
#         received = pickle.loads(data)

#         print("recive : ", received)
        

def client(client_socket):
    
    # start_new_thread(recv_data, (client_socket,))
    
    data = client_socket.recv(1024)
    
    received = pickle.loads(data)

    print("recive : ", received)
    
    return received
    
    # message = input('')
    # if message == 'quit':
    #     close_data = message
    #     break

    # client_socket.send(message.encode())


# client_socket.close()
    
# client()
