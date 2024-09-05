import socket
import binascii
import threading

def decode_protocol_1(hex_data):
    byte_data = binascii.unhexlify(hex_data)
    if len(byte_data) < 18:
        print("data insuficiente para o Protocolo 1")
        return
    
    start_bit = byte_data[:2]
    length = byte_data[2]
    protocol_number = byte_data[3]
    device_id = byte_data[4:12]
    information_serial_number = byte_data[12:14]
    error_check = byte_data[14:16]
    end_bit = byte_data[16:18]

    print("Start Bit:", start_bit.hex())
    print("Length:", length)
    print("Protocol Number:", protocol_number)
    print("Device ID:", device_id.hex())
    print("Information Serial Number:", information_serial_number.hex())
    print("Error Check:", error_check.hex())
    print("End Bit:", end_bit.hex())

    return {
        "start_bit": start_bit.hex(),
        "length": length,
        "protocol_number": protocol_number,
        "device_id": device_id.hex(),
        "information_serial_number": information_serial_number.hex(),
        "error_check": error_check.hex(),
        "end_bit": end_bit.hex()
    }

def handle_client(conn, addr):
    print(f'Conexão estabelecida com {addr}')

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f'Dados recebidos: {data.hex()}')

        try:
            protocol_number = data[3]
            if protocol_number == 0x01:
                decode_protocol_1(data.hex())
            else:
                print("Número de protocolo desconhecido. Por favor tente novamente.")
        except (binascii.Error, IndexError) as e:
            print("Data Hexadecimal Inválido:", e)

        conn.sendall(data)
        conn.close()
      
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen()
    print(f'Servidor iniciado em localhost:8080')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
