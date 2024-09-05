import binascii

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

def decode_protocol_2(hex_data):
    byte_data = binascii.unhexlify(hex_data)
    if len(byte_data) < 51: 
        print("data insuficiente para o Protocolo 2")
        return
    
    start_bit = byte_data[:2]
    packet_length = byte_data[2]
    protocol_number = byte_data[3]

    # GPS Information
    gps_info_start = 4
    gps_info_end = gps_info_start + 18
    gps_info = byte_data[gps_info_start:gps_info_end]
    date_time = gps_info[:6]
    quantity_of_gps_satellites = gps_info[6]
    latitude = gps_info[7:11]
    longitude = gps_info[11:15]
    speed = gps_info[16]
    course_status = gps_info[17:20]

    # LBS Information
    lbs_info_start = gps_info_end
    lbs_info_end = lbs_info_start + 8
    lbs_info = byte_data[lbs_info_start:lbs_info_end]
    mcc = lbs_info[0:2]
    mnc = lbs_info[2:3]
    lac = lbs_info[3:5]  
    cell_id = lbs_info[5:7]

    # Status Information
    status_info_start = lbs_info_end
    status_info_end = status_info_start + 7
    status_info = byte_data[status_info_start:status_info_end]
    device_information = status_info[0]
    battery_voltage_level = status_info[1]
    gsm_signal_strength = status_info[2]
    battery_voltage = status_info[3:5]
    external_voltage = status_info[5:7]

    mileage = byte_data[status_info_end:status_info_end + 4]
    hourmeter = byte_data[status_info_end + 4:status_info_end + 8]
    information_serial_number = byte_data[status_info_end + 8:status_info_end + 10]
    error_check = byte_data[status_info_end + 10:status_info_end + 12]
    end_bit = byte_data[status_info_end + 12:status_info_end + 14]

    print("Start Bit:", start_bit.hex())
    print("Packet Length:", packet_length)
    print("Protocol Number:", protocol_number)
    print("GPS Information:")
    print("  Date Time:", date_time.hex())
    print("  Quantity of GPS Satellites:", quantity_of_gps_satellites)
    print("  Latitude:", latitude.hex())
    print("  Longitude:", longitude.hex())
    print("  Speed:", speed)
    print("  Course Status:", course_status.hex())
    print("LBS Information:")
    print("  MCC:", mcc.hex())
    print("  MNC:", mnc.hex())
    print("  LAC:", lac.hex())
    print("  Cell ID:", cell_id.hex())
    print("Status Information:")
    print("  Device Information:", device_information)
    print("  Battery Voltage Level:", battery_voltage_level)
    print("  GSM Signal Strength:", gsm_signal_strength)
    print("  Battery Voltage:", hex(int.from_bytes(battery_voltage, byteorder='big')))
    print("  External Voltage:", external_voltage.hex())
    print("Mileage:", mileage.hex())
    print("Hourmeter:", hourmeter.hex())
    print("Information Serial Number:", information_serial_number.hex())
    print("Error Check:", error_check.hex())
    print("End Bit:", end_bit.hex())

    return {
        "start_bit": start_bit.hex(),
        "packet_length": packet_length,
        "protocol_number": protocol_number,
        "gps_information": {
            "date_time": date_time.hex(),
            "quantity_of_gps_satellites": quantity_of_gps_satellites,
            "latitude": latitude.hex(),
            "longitude": longitude.hex(),
            "speed": speed,
            "course_status": course_status.hex()
        },
        "lbs_information": {
            "mcc": mcc.hex(),
            "mnc": mnc,
            "lac": lac.hex(),
            "cell_id": cell_id.hex()
        },
        "status_information": {
            "device_information": device_information,
            "battery_voltage_level": battery_voltage_level,
            "gsm_signal_strength": gsm_signal_strength,
            "battery_voltage": battery_voltage.hex(),
            "external_voltage": external_voltage.hex()
        },
        "mileage": mileage.hex(),
        "hourmeter": hourmeter.hex(),
        "information_serial_number": information_serial_number.hex(),
        "error_check": error_check.hex(),
        "end_bit": end_bit.hex()
    }


def decode_protocol_3(hex_data):
    byte_data = binascii.unhexlify(hex_data)
    if len(byte_data) < 13:
        print("Dados insuficientes para o Protocolo 3")
        return
    
    start_bit = byte_data[:2]
    packet_length = byte_data[2]
    protocol_number = byte_data[3]
    device_info = byte_data[4]
    battery_voltage_level = byte_data[5]
    gsm_signal_strength = byte_data[6]
    external_voltage = byte_data[7]
    language = byte_data[8]
    
    if language == 0x01:
        language_str = 'Chinês'
    elif language == 0x02:
        language_str = 'Inglês'
    else:
        language_str = 'Desconhecido'

    info_serial_number = byte_data[9:11]
    error_check = byte_data[11:13] 
    end_bit = byte_data[13:]       

    print("Start Bit:", start_bit.hex())
    print("Packet Length:", packet_length)
    print("Protocol Number:", protocol_number)
    print("Device Info:", device_info)
    print("Battery Voltage Level:", battery_voltage_level)
    print("GSM Signal Strength:", gsm_signal_strength)
    print("External Voltage:", external_voltage)
    print("Language:", language_str)
    print("Information Serial Number:", info_serial_number.hex())
    print("Error Check:", error_check.hex())
    print("End Bit:", end_bit.hex())

    return {
        'start_bit': start_bit.hex(),
        'packet_length': packet_length,
        'protocol_number': protocol_number,
        'device_info': device_info,
        'battery_voltage_level': battery_voltage_level,
        'gsm_signal_strength': gsm_signal_strength,
        'external_voltage': external_voltage,
        'language': language_str,
        'info_serial_number': info_serial_number.hex(),
        'error_check': error_check.hex(),
        'end_bit': end_bit.hex(),
    }


def decode_protocol_4(hex_data):
    byte_data = binascii.unhexlify(hex_data)
    if len(byte_data) < 54:
        print("Insufficient data for Protocol 4")
        return
    
    start_bit = byte_data[:2]
    packet_length = byte_data[4]
    protocol_number = byte_data[5]

    # GPS Information
    gps_info_start = 4
    gps_info_end = gps_info_start + 18
    gps_info = byte_data[gps_info_start:gps_info_end]
    date_time = gps_info[:6]
    quantity_of_gps_satellites = gps_info[6]
    latitude = gps_info[7:11]
    longitude = gps_info[11:15]
    speed = gps_info[16]
    course_status = gps_info[17:20]

    # LBS Information
    lbs_info_start = gps_info_end
    lbs_info_end = lbs_info_start + 8
    lbs_info = byte_data[lbs_info_start:lbs_info_end]
    mcc = lbs_info[0:2]
    mnc = lbs_info[2:4]  
    lac = lbs_info[4:6]  
    cell_id = lbs_info[6:8]

    # Status Information
    status_info_start = lbs_info_end  
    status_info_end = status_info_start + 9
    device_information = byte_data[6]  
    battery_voltage_level = byte_data[7]
    gsm_signal_strength = byte_data[8]
    alarm_type = byte_data[9]
    language = byte_data[10]
    battery_voltage = byte_data[11]
    external_voltage = byte_data[12]

    if language == 0x01:
        language_str = 'Chinese'
    elif language == 0x02:
        language_str = 'English'
    else:
        language_str = 'Unknown'

    mileage = byte_data[status_info_end:status_info_end + 4]
    hourmeter = byte_data[status_info_end + 4:status_info_end + 8]
    information_serial_number = byte_data[status_info_end + 8:status_info_end + 10]
    error_check = byte_data[status_info_end + 10:status_info_end + 12]
    end_bit = byte_data[status_info_end + 12:status_info_end + 14]
    
    print("Start Bit:", start_bit.hex())
    print("Packet Length:", packet_length)
    print("Protocol Number:", protocol_number)
    print("GPS Information:")
    print("  Date Time:", date_time.hex())
    print("  Quantity of GPS Satellites:", quantity_of_gps_satellites)
    print("  Latitude:", latitude.hex())
    print("  Longitude:", longitude.hex())
    print("  Speed:", speed)
    print("  Course Status:", course_status.hex())
    print("LBS Information:")
    print("  MCC:", mcc.hex())
    print("  MNC:", mnc.hex())  
    print("  LAC:", lac.hex())
    print("  Cell ID:", cell_id.hex())
    print("Status Information:")
    print("  Device Information:", device_information)
    print("  Battery Voltage Level:", battery_voltage_level)
    print("  GSM Signal Strength:", gsm_signal_strength)
    print("  Alarm Type:", alarm_type)  
    print("  Language:", language_str)
    print("  Battery Voltage:", hex(battery_voltage))
    print("  External Voltage:", bytes([external_voltage]).hex())
    print("Mileage:", mileage.hex())
    print("Hourmeter:", hourmeter.hex())
    print("Information Serial Number:", information_serial_number.hex())
    print("Error Check:", error_check.hex())
    print("End Bit:", end_bit.hex())
    
    return {
        'start_bit': start_bit.hex(),
        'packet_length': packet_length,
        'protocol_number': protocol_number,
        
        "gps_information": {
            "date_time": date_time.hex(),
            "quantity_of_gps_satellites": quantity_of_gps_satellites,
            "latitude": latitude.hex(),
            "longitude": longitude.hex(),
            "speed": speed,
            "course_status": course_status.hex()
        },
        
        "lbs_information": {
            "lbs": lbs_info.hex(),  
            "mcc": mcc.hex(),
            "mnc": mnc.hex(),
            "lac": lac.hex(),
            "cell_id": cell_id.hex()
        },
        
        "status_information": {
            "device_information": device_information,
            "battery_voltage_level": battery_voltage_level,
            "gsm_signal_strength": gsm_signal_strength,
            "alarm_type": alarm_type,  
            'language': language_str,
            "battery_voltage": hex(battery_voltage),
            "external_voltage": bytes([external_voltage]).hex()
        },
        
        "mileage": mileage.hex(),
       
        "hourmeter": hourmeter.hex(),
        "information_serial_number": information_serial_number.hex(),
        "error_check": error_check.hex(),
        "end_bit": end_bit.hex()
    }
    

import binascii

def decode_protocol_5(hex_data):
    byte_data = binascii.unhexlify(hex_data)
    if len(byte_data) < 41: 
        print("Dados insuficientes para Protocolo 5")
        return
    
    start_bit = byte_data[:2]
    packet_length = byte_data[4]
    protocol_number = byte_data[5]
    flag = byte_data[6]
    device_id = byte_data[7:14]
    imsi = byte_data[15:22]
    iccid = byte_data[23:32]
    information_serial_number = byte_data[33:35]
    error_check = byte_data[36:38]
    end_bit = byte_data[39:41]
    
    print("Start Bit:", start_bit.hex())
    print("Packet Length:", packet_length)
    print("Protocol Number:", protocol_number)
    print("Flag:", flag.hex())
    print("Device ID:", device_id.hex())
    print("IMSI:", imsi.hex())
    print("ICCID:", iccid.hex())
    print("Information Serial Number:", information_serial_number.hex())
    print("Error Check:", error_check.hex())
    print("End Bit:", end_bit.hex())
    
    return {
        "start_bit": start_bit.hex(),
        "packet_length": packet_length,
        "protocol_number": protocol_number,
        "flag": flag,
        "device_id": device_id.hex(),
        "imsi": imsi.hex(),
        "iccid": iccid.hex(),
        "information_serial_number": information_serial_number.hex(),
        "error_check": error_check.hex(),
        "end_bit": end_bit.hex()
    }


def decode_protocol_6(hex_data):
    byte_data = binascii.unhexlify(hex_data)
    if len(byte_data) < 22:
        print("Dados insuficientes para Protocolo 6")
        return
    
    start_bit = byte_data[:2]
    packet_length = byte_data[2] 
    protocol_number = byte_data[3]
    length_of_command = byte_data[5]  
    server_flag_bit = byte_data[6:9]
    command_content = byte_data[10:10 + length_of_command] 
    serial_number = byte_data[7:11]  
    error_check = byte_data[13:15]
    end_bit = byte_data[16:18]
    
    print("Start Bit:", start_bit.hex())
    print("Packet Length:", packet_length)
    print("Protocol Number:", protocol_number)
    print("Length of Command:", length_of_command)
    print("Server Flag Bit:", server_flag_bit.hex())
    print("Command Content:", command_content.hex())
    print("Serial Number:", serial_number.hex())
    print("Error Check:", error_check.hex())
    print("End Bit:", end_bit.hex())
    
    return {
        "start_bit": start_bit.hex(),
        "packet_length": packet_length,
        "protocol_number": protocol_number,
        "length of command": length_of_command,
        "server flag bit": server_flag_bit.hex(),
        "command content": command_content.hex(),
        "serial number": serial_number.hex(),
        "error_check": error_check.hex(),
        "end_bit": end_bit.hex()
    }


def decode_protocol_7(hex_data):
    byte_data = binascii.unhexlify(hex_data)
    if len(byte_data) < 37:
        print("Dados insuficientes para Protocolo 7")
        return
    
    start_bit = byte_data[:2]
    packet_length = byte_data[2]
    protocol_number = byte_data[3]  
    length_of_command = byte_data[4]
    server_flag_bit = byte_data[5:8]  
    command_content = byte_data[8:8 + length_of_command]
    reserved = byte_data[8]
    information_serial_number = byte_data[10]
    error_check = byte_data[12 + length_of_command:14]
    end_bit = byte_data[14 + length_of_command:16 + length_of_command]
    
    print("Start Bit:", start_bit.hex())
    print("Packet Length:", packet_length)
    print("Protocol Number:", protocol_number)
    print("Length of Command:", length_of_command)
    print("Server Flag Bit:", server_flag_bit.hex())
    print("Command Content:", command_content.hex())
    print("Reserved:", reserved.hex())
    print("Information Serial Number:", information_serial_number.hex())
    print("Error Check:", error_check.hex())
    print("End Bit:", end_bit.hex())
    
    return {
        "start_bit": start_bit.hex(),
        "packet_length": packet_length,
        "protocol_number": protocol_number,
        "length_of_command": length_of_command,
        "server_flag_bit": server_flag_bit.hex(),
        "command_content": command_content.hex(),
        "reserved": reserved.hex(),
        "information_serial_number": information_serial_number.hex(),
        "error_check": error_check.hex(),
        "end_bit": end_bit.hex()
    }


def main():
    hex_data = input("Digite aqui o data packet desejado: ")
    
    try:
        byte_data = binascii.unhexlify(hex_data)
        protocol_number = byte_data[3]

        if protocol_number == 0x01:
            decode_protocol_1(hex_data)
        elif protocol_number == 0x17:
            decode_protocol_2(hex_data)
        elif protocol_number == 0x13:
            decode_protocol_3(hex_data)
        elif protocol_number == 0x16:
            decode_protocol_4(hex_data)
        elif protocol_number == 0x094:
            decode_protocol_5(hex_data)
        elif protocol_number == 0x80:
            decode_protocol_6(hex_data)
        elif protocol_number == 0x15:
            decode_protocol_7(hex_data)
        else:
            print("Número de protocolo desconhecido. Por favor tente novamente.")
    except (binascii.Error, IndexError) as e:
        print("Data Hexadecimal Inválido:", e)

if __name__ == "__main__":
    main()
