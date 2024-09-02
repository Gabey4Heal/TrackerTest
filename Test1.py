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

# código deste: (0x01)  Login information packet

def decode_hex_data_protocol1():
    hex_data = input("Escreva aqui seu dado: ")
    data_bytes = bytes.fromhex(hex_data)

    if len(data_bytes) < 9:
        print("Não consegui ler seu dado corretamente, reinicie e tente novamente")
        return

    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')

    gps_information = {
        "date_time": data_bytes[5:10],
        "quantity_GPS_satellites": data_bytes[11:12],
        "latitude": data_bytes[13:16],
        "longitude": data_bytes[17:20],
        "speed": data_bytes[21:22],
        "course_status": data_bytes[23:25]
    }

    lbs_information = {
        "MCC": data_bytes[26:28],
        "MNC": data_bytes[29:30],
        "LAC": data_bytes[31:33],
        "cell_ID": data_bytes[34:36]
    }

    status_information = {
        "device_information": data_bytes[37:38],
        "battery_voltage_level": data_bytes[39:40],
        "GSM_signal_strength": data_bytes[41:42],
        "battery_voltage": data_bytes[43:45],
        "external_volume": data_bytes[46:48]
    }

    mileage = data_bytes[49:52]
    hourmeter = data_bytes[53:56]
    information_serial_number = data_bytes[57:59]
    error_check = int.from_bytes(data_bytes[60:62], byteorder= 'big')
    print(error_check)
    end_bit = data_bytes[63:65]

    print("Informações GPS:", gps_info)
    print("Informações LBS:", lbs_info)
    print("Informações de Status:", status_info)
    print("Quilometragem:", mileage)
    print("Horímetro:", hourmeter)
    print("Número de Série:", information_serial_number)
    print("Verificação de Erro:", error_check)
    print("Bit Final:", end_bit)

# código deste: (0x17)  Location data Packet ^

def decode_hex_data_protocol2():
    hex_data = input("Escreva aqui seu dado: ")
    data_bytes = bytes.fromhex(hex_data)
    
    if len(data_bytes) < 10:
        print("Não consegui ler seu dado corretamente, reinicie e tente novamente")
        return
    
    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')
    status_information = {
        "device_information": data_bytes[5:6],
        "battery_voltage_level": data_bytes[7:8],
        "GSM_signal_strength": data_bytes[9:10],
        "external_voltage": data_bytes[11:12],
        "language": data_bytes[13:14],
    }
    information_serial_number = int.from_bytes(data_bytes[15:17], byteorder='big')
    error_check = int.from_bytes(data_bytes[18:20], byteorder= 'big')
    print(error_check)
    end_bit = data_bytes[21:23]
    
    #código deste: (0x13)  Status information Packet (Heartbeat Packet) ^
    
    
def decode_hex_data_protocol3():
    hex_data = input("Escreva aqui seu dado: ")
    data_bytes = bytes.fromhex(hex_data)
    
    if len(data_bytes) < 10:
        print("Não consegui ler seu dado corretamente, reinicie e tente novamente")
        return
    
    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')
    GPS_information = {
        "date_time": data_bytes[5:10],
        "quantity_of_GPS_satellites": data_bytes[11:12],
        "latitude": data_bytes[13:16],
        "longitude": data_bytes[17:20],
        "speed": data_bytes[21:22],
        "course_status": data_bytes[23:25],
    }
    
    lbs_information = {
        "LBS": data_bytes[26:27],
        "MCC": data_bytes[28:30],
        "MNC": data_bytes[31:32],
        "LAC": data_bytes[33:35],
        "cell_ID": data_bytes[36:38],
    }
    
    status_information = {
        "device_information": data_bytes[39:40],
        "battery_voltage_level": data_bytes[41:42],
        "GSM_signal_strength": data_bytes[42:43],
        "alarm_type": data_bytes[44:45],
        "language": data_bytes[46:47],
        "battery_voltage": data_bytes[48:50],
        "external_volume": data_bytes[51:53]
    }
    mileage = data_bytes[54:57]
    hourmeter = data_bytes[58:61]
    information_serial_number = data_bytes[62:64]
    error_check = int.from_bytes(data_bytes[65:67], byteorder= 'big')
    print(error_check)
    end_bit = data_bytes[68:70]

    #código deste: (0x16) Alarm Packet ^ 
    
    
def decode_hex_data_protocol4():
    hex_data = input("Escreva aqui seu dado: ")
    data_bytes = bytes.fromhex(hex_data)
    
    if len(data_bytes) < 11:
        print("Não consegui ler seu dado corretamente, reinicie e tente novamente")
        return
    
    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')
    flag = int.from_bytes(data_bytes[5:6], byteorder='big')
    device_id = data_bytes[5:12]
    imsi = data_bytes[13:21]
    iccid = data_bytes[22:31]
    information_serial_number = data_bytes[32:34]
    error_check = int.from_bytes(data_bytes[35:37], byteorder= 'big')
    print(error_check)
    end_bit = data_bytes[38:40]

    #código deste: (0x094) ICCID Packer ^
    
def decode_hex_data_protocol5():
    hex_data = input("Escreva aqui seu dado: ")
    data_bytes = bytes.fromhex(hex_data)
    
    if len(data_bytes) < 12:
        print("Não consegui ler seu dado corretamente, reinicie e tente novamente")
        return
    
    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')
    length_of_command = int.from_bytes(data_bytes[5:6], byteorder='big')
    server_flag_bit = int.from_bytes(data_bytes[7:10])
    command_content = data_bytes[11:12]
    serial_number = int.from_bytes(data_bytes [13:15])
    error_check = int.from_bytes(data_bytes[16:18], byteorder= 'big')
    print(error_check)
    end_bit = data_bytes[19:21]
    
    #código deste: (0x080) Packet Sent by Server ^
    
def decode_hex_data_protocol6():
    hex_data = input("Escreva aqui seu dado: ")
    data_bytes = bytes.fromhex(hex_data)
    
    if len(data_bytes) < 13:
        print("Não consegui ler seu dado corretamente, reincie e tente novamente")
        return
    
    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')
    length_of_command = int.from_bytes(data_bytes[5:6], byteorder='big')
    server_flag_bit = int.from_bytes(data_bytes[7:10])
    command_content = data_bytes[11:12]
    reserved = int.from_bytes(data_bytes [13:16])
    information_serial_number = data_bytes[17:19]
    error_check = int.from_bytes(data_bytes[20:22])
    print(error_check)
    end_bit = data_bytes[23:25]
    
    
if __name__ == "__main__":
    decode_hex_data()
