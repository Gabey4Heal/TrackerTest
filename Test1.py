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

# código deste: (0x01)

def decode_hex_data_protocol1():
    hex_data = input("Escreva aqui seu data: ")
    data_bytes = bytes.fromhex(hex_data)

    if len(data_bytes) < 9:
        print("Não consegui ler seu data corretamente, reinicie e tente novamente")
        return

    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')
    GPS_information(5:25):
        date_time = [5:10]
        quantity_GPS_satellites = [11:12]
        latitude = [13:16]
        longitude = [17:20]
        Speed = [21:22]
        Course_Status = [23:25]
    LBS_information(26:36):
        MCC = [26:28]
        MNC = [29:30]
        LAC = [31:33]
        cell_ID = [34:36]
    status_information(37:48):
        device_information = [37:38]
        battery_voltage_level = [39:40]
        GSM_signal_strength = [41:42]
        battery_voltage = [43:45]
        external_volume = [46:48]
    mileage = [49:52]
    hourmeter = [53:56]
    information_serial_number = [57:59]
    error_check = [60:62]
    end_bit = [63:65]

# código deste: (0x17)

def decode_hex_data_protocol2():
    # duplicated function implementation...

def decode_hex_data_protocol3():
    # duplicated function implementation...

if __name__ == "__main__":
    decode_hex_data()
