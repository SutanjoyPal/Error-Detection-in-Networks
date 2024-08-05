import random

def inject_single_error(data):
    data = list(data)
    pos = random.randint(0, len(data) - 1)
    data[pos] = '1' if data[pos] == '0' else '0'
    return ''.join(data)

def inject_double_error(data):
    pos1 = random.randint(0, len(data) - 1)
    pos2 = random.randint(0, len(data) - 1)
    while pos2 == pos1:
        pos2 = random.randint(0, len(data) - 1)
    data[pos1] = '1' if data[pos1] == '0' else '0'
    data[pos2] = '1' if data[pos2] == '0' else '0'
    return ''.join(data)

def inject_burst_error(data,n):
    start = random.randint(0, len(data) - 5)
    for i in range(start, start + n):
        data[i] = '1' if data[i] == '0' else '0'
    return ''.join(data)