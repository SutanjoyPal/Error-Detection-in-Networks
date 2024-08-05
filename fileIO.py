def read_input_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read().strip()
    return data

def prepare_datawords(data, word_size):
    datawords = [data[i:i+word_size] for i in range(0, len(data), word_size)]
    return datawords


