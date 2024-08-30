import socket
import datetime
import struct

def decode_hex_data():
    hex_data = input("Escreva aqui seu data: ")
    data_bytes = bytes.fromhex(hex_data)

    if len(data_bytes) < 8:
        print("Não consegui ler seu data corretamente, reinicie e tente novamente.")
        return

    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5 
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')
    device_id = data_bytes[5:12]
    information_serial_number = int.from_bytes(data_bytes[13:14], byteorder='big')
    error_check = int.from_bytes(data_bytes[15:16], byteorder= 'big')
    print(error_check)
    end_bit = data_bytes[16:18]  

    print("Start Bit:", start_bit.hex())
    print("Length:", length)
    print("Protocol Number:", protocol_number)
    print("Device ID:", device_id.hex())
    print("Information Serial Number:", information_serial_number)
    print("Error Check:", error_check)
    print("End Bit:", end_bit.hex())

if __name__ == "__main__":
    decode_hex_data()
