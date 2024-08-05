# def calculate_checksum(data):
#     checksum = 0
#     for i in range(0, len(data), 16):
#         word = int(data[i:i+16], 2)
#         print(f"{word}")
#         checksum = (checksum + word) & 0xFFFF
#     checksum = ~checksum & 0xFFFF
#     return format(checksum, '016b')

# def verify_checksum(data):
#     print("Result:   ",calculate_checksum(data))
#     return calculate_checksum(data) == '0000000000000000'
def calculate_checksum(data):
    checksum = 0
    for i in range(0, len(data), 16):
        word = data[i:i+16]
        if len(word) < 16:
            word = word.ljust(16, '0')  # Pad the word to make sure it is 16 bits long
        try:
            word_value = int(word, 2)
        except ValueError as e:
            print(f"Error converting word '{word}' to int: {e}")
            continue
        checksum = (checksum + word_value) & 0xFFFF
    checksum = ~checksum & 0xFFFF
    checksum_bin = format(checksum, '016b')
    print(f"Calculated Checksum: {checksum_bin}")
    return checksum_bin

def verify_checksum(data):
    # Extract the checksum from the data and verify it
    expected_checksum = data[-16:]  # Last 16 bits are the checksum
    data_to_verify = data[:-16]     # Data to verify is all but the checksum
    
    calculated_checksum = calculate_checksum(data_to_verify)
    #print(f"Checksum Verification: Calculated Checksum: {calculated_checksum}, Expected: {expected_checksum}")
    
    return calculated_checksum == expected_checksum
