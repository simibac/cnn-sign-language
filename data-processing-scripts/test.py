def map(num):
    if num==63:
        return 36
    elif num < 91 and num > 64:
        return num - 55
    elif num < 58 and num > 47:
        return num - 48

def map_back(num):
    if num==36:
        return chr(63)
    elif num < 36 and num > 9:
        return chr(num + 55)
    elif num < 10 and num > -1:
        return chr(num + 48)

print(map_back(36))
