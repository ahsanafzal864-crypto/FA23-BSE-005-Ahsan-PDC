import socket

HOST = '127.0.0.1'
PORT = 65432

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))
        print(f"[CONNECTED] Connected to server at {HOST}:{PORT}")
        print("Tip: Type 'exit' to close connection.\n")
        
        while True:
            msg = input("You: ")
            
            if not msg.strip():
                continue
                
            # Message send karein
            client.send(msg.encode('utf-8'))
            
            if msg.lower() == 'exit':
                print("[CLOSING] Disconnecting from server...")
                break
                
            # Server ka response receive karein
            reply = client.recv(1024).decode('utf-8')
            print(f"Reply: {reply}")
            
    except ConnectionRefusedError:
        print("[ERROR] Server offline hai ya run nahi ho raha.")
    finally:
        client.close()

if __name__ == '__main__':
    start_client()