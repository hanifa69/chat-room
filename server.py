import socket 
import threading
import time
members=[]
user_names=[]
def connection(conn):
    global members
    with conn:
        #conn.sendall(b"Welcome! Type something:\n")
        while True:
            user_name= conn.recv(1024)

            members.append(conn)
            user_names.append(user_name)

            message_join="joined the chat room"
            send(user_name,message_join,conn)
            
def send (user_name,message,conn):
    global members
    for client in members:
        try:
            if client != conn:
                messages=user_name+message
                print(messages)
                client.sendall(messages.encode())
        except:
            print("eror")    
def many():
       
    HOST= '127.0.0.1'
    PORT=60000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        while True:
            conn,addr= s.accept()
            t=threading.Thread(target=connection,args=(conn,))
            t.start()
many()