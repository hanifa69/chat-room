import socket
import threading

def recv(conn):
    while True:
        try:
            data =conn.recv(1024)
            if not data:
                print("disconection for server..")
                break
            print(data.decode())
        except:
            print("Error")
            break

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 60000))
        username = input("Please enter username: ")
        s.sendall(username.encode())

        # Thread جدا برای دریافت پیام ها
        t = threading.Thread(target=recv, args=(s,))
        t.start()
        while True:
            try:
                message= input()
                s.sendall(message.encode())
            
            except Exception as e:
                print(f"Error sending message: {e}")
                break
main()