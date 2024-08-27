import socket
# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
server_address = ('10.10.1.25', 8090)
sock.connect(server_address)

def decode_hex(hex_string):
    # Remove any whitespace characters from the hex string
    hex_string = hex_string.replace(" ", "")
    # Decode the hex string into bytes
    bytes_data = bytes.fromhex(hex_string)
    # Convert the bytes into a string
    decoded_string = bytes_data.decode("utf-8", errors="replace")
    return decoded_string

hexstring = "78780D010865080044015069003A53F20D0A"
it=iter(hexstring); [a+b for a,b in zip(it, it)]
['78', '78', '0D', '01', '08', '65', '08', '00', '44', '01', '50', '69', '00', '3A', '53', 'F2', '0D', '0A']

def explain_hex(hex_string):
    # Define a dictionary of hexadecimal terms
    hex_terms = {
        "0x78 , 0x78": "Start Bit",
        "0x0D": "Package Length from protocol number to error checksum",
        "0x01": "Protocol Number",
        "0x08 , 0x65 , 0x08 , 0x00 , 0x44 , 0x01 , 0x50 , 0x69": "Device ID",
        "0x00 , 0x3A": "Information Serial Number",
        "0x53 , 0xF2": "Error Check",
        "0x0D , 0x0A": "End Bit",
    }

    # Initialize an empty list to store the explanations
    explanations = []

    # Iterate over each byte in the hex string
    for i in range(0, len(hex_string), 2):
        byte = hex_string[i:i+2]

        # Check if the byte is in the dictionary of hexadecimal terms
        for term in hex_terms:
            if "-" in term:
                start, end = term.split("-")
                if int(start, 16) <= int(byte, 16) <= int(end, 16):
                    explanations.append(f"{byte}: {hex_terms[term]}")
                    break
            elif byte == term:
                explanations.append(f"{byte}: {hex_terms[term]}")
                break
        else:
            explanations.append(f"{byte}: Unknown")

    return explanations

def main():
    # Get the hexadecimal code from the user
    hex_string = input("Enter a hexadecimal code: ")

    # Decode the hexadecimal code
    decoded_string = decode_hex(hex_string)

    # Explain each part of the hexadecimal code
    explanations = explain_hex(hex_string)

    # Print out the results
    print(f"Decoded string: {decoded_string}")
    print("Explanations:")
    for explanation in explanations:
        print(explanation)

if __name__ == "__main__":
    main()

# Close the socket
sock.close()
