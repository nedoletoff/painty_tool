import copy

from bitstring import BitArray


def bytes_to_bin(arr: bytes):
    a = copy.deepcopy(arr)
    res = []
    for i in range(0, 112, 4):
        temp = a[i:i + 4]
        b = BitArray(temp)
        res.append(list(b.bin))
    return res


def bin_to_bytes(arr: list):
    a = copy.deepcopy(arr)
    res = []
    for b in a:
        r = [0, 0, 0, 0]
        b = b[::-1]
        temp = ''.join(b) + '0000'
        for i in range(0, 32, 8):
            r[i // 8] = int(temp[i:i + 8], 2)
        r = bytes(r)
        res.append(r)
    res = res[::-1]
    res = b''.join(res)
    return res


def d2_to_d1(arr: list):
    a = copy.deepcopy(arr)
    res = []
    for i in range(28):
        temp = ''
        for j in range(28):
            temp += str(a[i][j])
        temp = temp[::-1]
        res.append(temp)
    return res
