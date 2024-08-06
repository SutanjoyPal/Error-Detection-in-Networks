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

