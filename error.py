import random

def inject_single_error(data):
    print("Injecting single error")
    newData = list(data)
    pos = random.randint(0, len(data) - 1)
    newData[pos] = '1' if data[pos] == '0' else '0'
    return ''.join(newData)

def inject_double_error(data):
    print("Injecting double error")
    newData = list(data)
    pos1 = random.randint(0, len(data) - 1)
    pos2 = random.randint(0, len(data) - 1)
    while pos2 == pos1:
        pos2 = random.randint(0, len(data) - 1)
    newData[pos1] = '1' if data[pos1] == '0' else '0'
    newData[pos2] = '1' if data[pos2] == '0' else '0'
    return ''.join(newData)

def inject_burst_error(data,n):
    print(f"Injecting burst error of {n} errors")
    newData = list(data)
    start = random.randint(0, len(data) - 10)
    for i in range(start, start + n):
        newData[i] = '1' if data[i] == '0' else '0'
    return ''.join(newData)