import socket
import threading

# TCP Server
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()

    print("O servidor está ouvindo ")
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
            print(f"Received: {data.hex()}")
            parse_data(data)
            conn.sendall(data)

def parse_data(data):
    if len(data) == 10:  
        start_bit = data[0:2]
        length = data[2] 
        protocol_number = data[3:4]
        information_serial_number = data[4:6]
        error_check = data[6:8]
        end_bit = data[8:10]

        print(f"Start bit: {start_bit.hex()}")
        print(f"Length: {length}")
        print(f"Protocol number: {protocol_number.hex()}")
        print(f"Information serial number: {information_serial_number.hex()}")
        print(f"Error check: {error_check.hex()}")
        print(f"End bit: {end_bit.hex()}")
    elif len(data) == 14:  
        parse_data_v2(data)
    else:
        print("Error: tamanho incorreto de data.")

def parse_data_v2(data):
    start_bit = data[0:2]
    length = data[2] 
    protocol_number = data[3:4]
    information_serial_number = data[4:6]
    error_check = data[6:8]
    end_bit = data[8:10]

    print(f"Start bit(V2): {start_bit.hex()}")
    print(f"Length(V2): {length}")
    print(f"Protocol number(V2): {protocol_number.hex()}")
    print(f"Information serial number(V2): {information_serial_number.hex()}")
    print(f"Error check(V2): {error_check.hex()}")
    print(f"End bit(V2): {end_bit.hex()}")

def parse_data_v3(data):
    start_bit = data[0:2]
    length = data[2]
    protocol_number = data[3:4]
    information_serial_number = data[4:6]
    error_check = data[6:8]
    end_bit = data[8:10]
    
    print(f"Start bit(V3): {start_bit.hex()}")
    print(f"Length(V3): {length}")
    print(f"Protocol Number(V3): {protocol_number.hex()}")
    print(f"Information serial number(V3): {information_serial_number.hex()}")
    print(f"Error check(V3): {error_check.hex()}")
    print(f"End bit(V3): {end_bit.hex()}")
    
def parse_data_v4(data):
    start_bit = data[0:2]
    length = data[2]
    protcol_number = data[3:4]
    information_serial_number = data[4:6]
    error_check = data[6:8]
    end_bit = data[8:10]
    
    print(f"Start bit(V4): {start_bit.hex()}")
    print(f"Length(V4): {length}")
    print(f"Protocol Number(V4): {protocol_number.hex()}")
    print(f"Information serial number(V4): {information_serial_number.hex()}")
    print(f"Error check(V4): {error_check.hex()}")
    print(f"End bit(V4): {end_bit.hex()}")


if __name__ == "__main__":
    threading.Thread(target=tcp_server).start()
    
    hex_input = input("por favor copie o código abaixo: ")
    hex_data = bytes.fromhex(hex_input)
