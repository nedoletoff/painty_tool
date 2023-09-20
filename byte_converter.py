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
    res = bytearray()
    for b in a:
        r = [0, 0, 0, 0]
        temp = ''.join(b) + '0000'
        for i in range(0, 32, 8):
            r[i // 8] = int(temp[i:i + 8], 2)
        r = bytes(r)
        res += r
    return b"" + res
