import socket
import threading

HOST = '127.0.0.1'  # Localhost
PORT = 65432

# Output display synchronize karne ke liye Lock
print_lock = threading.Lock()

def handle_client(conn, addr):
    # Har thread ka unique name hota hai
    thread_name = threading.current_thread().name
    
    with print_lock:
        print(f"[NEW CONNECTION] Thread: {thread_name} | Client Connected: {addr[0]}:{addr[1]}")

    try:
        while True:
            # Client se message receive karein
            data = conn.recv(1024).decode('utf-8')
            
            # Agar connection close ho jaye ya client disconnect kare
            if not data or data.lower() == 'exit':
                break
                
            # Synchronized output
            print_lock.acquire()
            try:
                print(f"[{thread_name}] Message from {addr[0]}:{addr[1]} -> {data}")
            finally:
                print_lock.release()
            
            # Echo ya confirmation wapis bhejein
            response = f"Server received: {data}"
            conn.send(response.encode('utf-8'))
            
    except ConnectionResetError:
        pass
    finally:
        # Connection close hone par print aur socket cleanup
        print_lock.acquire()
        try:
            print(f"[DISCONNECTED] Thread: {thread_name} | Client {addr[0]}:{addr[1]} left.")
        finally:
            print_lock.release()
            
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}...")
    
    try:
        while True:
            # Naya client connection accept karein
            conn, addr = server.accept()
            
            # Har naye client ke liye alag thread banayein
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            
            print_lock.acquire()
            try:
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            finally:
                print_lock.release()
                
    except KeyboardInterrupt:
        print("\n[SERVER SHUTTING DOWN]")
    finally:
        server.close()

if __name__ == '__main__':
    start_server()