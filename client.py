import socket
def send(message):
    s.sendall(message.encode())
    data = s.recv(1024)
    print(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1" , 60000))

    user_name=input("please enter username:").send()

    while True:
        message = input("please enter message: ")
        send (message)
