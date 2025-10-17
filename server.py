import socket 
import threading
import time
members=[]
user_names=[]
def connection(conn):
    global members
    with conn:
        #conn.sendall(b"Welcome! Type something:\n")
     #   while True:
        user_name= conn.recv(1024).decode('utf-8')

        members.append(conn)
        user_names.append(user_name)

        message_join=" joined the chat room"
        send(user_name,message_join,conn)
        while True:
            try:
                message = conn.recv(1024).decode('utf-8')
                if not message:
                    break
                if message =="list":
                    message=', '.join(user_names) 
                send(user_name,message, conn)
            except:
                break
        #index = members.index(conn)
        #members.remove(conn)
        #left_user = user_names.pop(index)
        #send( left_user, 'left the chat room.', conn)
            
def send (user_name,message,conn):
    global members
    for client in members:
              
            time_now=str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            messages=user_name+":"+message+"\n"+time_now

            print(messages)
            client.sendall(messages.encode('utf-8'))
            
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