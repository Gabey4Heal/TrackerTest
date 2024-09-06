import socket
import threading

# TCP Server
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.10.1.25', 8090))
    server_socket.listen()

    print("O Servidor está ouvindo...")
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        threading.Thread(target=handle_client, args=(conn,)).start()

def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recebido (string): {data.decode('utf-8', errors='ignore')}")
            parse_data(data)
            conn.sendall(data)

def parse_data(data):
    if len(data) != 16:  
        print("Error: Tamanho incorreto de data.")
        return

    start_bit = data[0:2]
    length = data[2:3]
    protocol_number = data[3:4]
    information_serial_number = data[4:6]
    error_check = data[6:8]
    end_bit = data[8:10]

    print(f"Start bit: {start_bit.hex()}")
    print(f"Length: {length.hex()}")
    print(f"Protocol number: {protocol_number.hex()}")
    print(f"Information serial number: {information_serial_number.hex()}")
    print(f"Error check: {error_check.hex()}")
    print(f"End bit: {end_bit.hex()}")
    
# TCP Client
def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.10.1.25', 8090))

    hex_data = bytes.fromhex('787805170026DF2D0D0A')
    client_socket.sendall(hex_data)

    response = client_socket.recv(1024)
    print(f"Response: {response.hex()}")

    client_socket.close()

# Run server e client
if __name__ == "__main__":
    threading.Thread(target=tcp_server).start()
