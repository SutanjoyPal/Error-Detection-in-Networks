# def calculate_checksum(data):
#     checksum = 0
#     for i in range(0, len(data), 16):
#         word = data[i:i+16]
#         if len(word) < 16:
#             word = word.ljust(16, '0')  # Pad the word to make sure it is 16 bits long
#         try:
#             word_value = int(word, 2)
#         except ValueError as e:
#             print(f"Error converting word '{word}' to int: {e}")
#             continue
#         checksum = (checksum + word_value) & 0xFFFF
#     checksum = ~checksum & 0xFFFF
#     checksum_bin = format(checksum, '016b')
#     print(f"Calculated Checksum: {checksum_bin}")
#     return checksum_bin

# def verify_checksum(data):
#     # Extract the checksum from the data and verify it
#     expected_checksum = data[-16:]  # Last 16 bits are the checksum
#     data_to_verify = data[:-16]     # Data to verify is all but the checksum
    
#     calculated_checksum = calculate_checksum(data_to_verify)
#     #print(f"Checksum Verification: Calculated Checksum: {calculated_checksum}, Expected: {expected_checksum}")

#     return calculated_checksum == expected_checksum

def calculate_checksum(data):
    checksum = 0
    for i in range(0, len(data), 16):
        word = data[i:i+16]
        word_value = int(word, 2)  # Convert the binary string to an integer
        #checksum = (checksum + word_value) & 0xFFFF  # Keep it to 16 bits
        checksum += word_value
        # Handle overflow by adding the overflow bits back
        while checksum > 0xFFFF:
            checksum = (checksum & 0xFFFF) + (checksum >> 16)
    checksum = ~checksum & 0xFFFF  # One's complement
    return format(checksum, '016b')

# def verify_checksum(data):
#     x = calculate_checksum(data)
#     print(f"Checksum: {x}")
#     return x == '0000000000000000'

# def calculate_checksum(data):
#     intSum=0
#     for i in range(0, len(data), 16):
#         word = data[i:i+16]

#         word_value = int(word, 2)  # Convert the binary string to an integer
#         #checksum = (checksum + word_value) & 0xFFFF  # Keep it to 16 bits
#         intSum += word_value
#     Sum = bin(intSum)[2:]
#     k=16
#     # Adding the overflow bits
#     if(len(Sum) > k):
#         x = len(Sum)-k
#         Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
#     if(len(Sum) < k):
#         Sum = '0'*(k-len(Sum))+Sum    
    

#     # Calculating the complement of sum
#     Checksum = ''
#     for i in Sum:
#         if(i == '1'):
#             Checksum += '0'
#         else:
#             Checksum += '1'
#     return Checksum
