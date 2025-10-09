import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1" , 60000))
    while True:
        a= input("please enter username:")
        s.sendall(a.encode())
        data = s.recv(1024)
        print(data.decode())