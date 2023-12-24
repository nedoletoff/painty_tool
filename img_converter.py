import copy
from bitstring import BitArray

pal_bytes = bytes([0, 0, 255, 0, 0, 255, 0, 0, 255,
                   0, 0, 0, 0, 0, 0, 0, 66, 71, 82,
                   115, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 255, 255, 255, 0])

test_arr = bytes([170, 170, 170, 170, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0])


def read_bmp_data(name: str):
    with open(name, "rb") as f:
        print('bfType', f.read(2))  # bfType 0
        data = f.read()
        print('bfSize', int.from_bytes(data[0:4], "little"))  # bfSize 2
        print('bfReserved1', int.from_bytes(data[4:6], "little"))  # bfReserved1 6
        print('bfReserved2', int.from_bytes(data[6:8], "little"))  # bfReserved2 8
        print('bfOffBits', int.from_bytes(data[8:12], "little"))  # bfOffBits 10
        print('biSize', int.from_bytes(data[12:16], "little"))  # biSize 14
        print('biWidth', int.from_bytes(data[16:20], "little"))  # biWidth 18
        print('biHeight', int.from_bytes(data[20:24], "little"))  # biHeight 22
        print('biPlanes', int.from_bytes(data[24:26], "little"))  # biPlanes 26
        print('biBitCount', int.from_bytes(data[26:28], "little"))  # biBitCount 28
        print('biCompression', int.from_bytes(data[28:32], "little"))  # biCompression 28
        print('biSizeImage', int.from_bytes(data[32:36], "little"))  # biSizeImage 32
        print('biXPelsPerMeter', int.from_bytes(data[36:40], "little"))  # biXPelsPerMeter 36
        print('biYPelsPerMeter', int.from_bytes(data[40:44], "little"))  # biYPelsPerMeter 40
        print('biClrUsed', int.from_bytes(data[44:48], "little"))  # biClrUsed 44
        print('biClrImportant', int.from_bytes(data[48:52], "little"))  # biClrImportant 48
        s = ''
        for i, e in enumerate(data[52:144]):
            print(f'{i + 54}-{e}', end='\t')
            if i % 20 == 0 and i > 0:
                print()
            s += str(e) + ', '
        for i, e in enumerate(data[144:]):
            if i % 8 == 0:
                print()
            print(f'{i + 146}-{e}', end='\t')
        print()


def save_img(name: str, arr=test_arr, width=28, height=28):
    with open(name, "wb") as f:
        f.write(b"BM")  # bfType 0
        f.write((258).to_bytes(4, "little"))  # bfSize 2
        f.write((0).to_bytes(2, "little"))  # bfReserved1 6
        f.write((0).to_bytes(2, "little"))  # bfReserved2 8
        f.write((146).to_bytes(4, "little"))  # bfOffBits 10
        f.write((124).to_bytes(4, "little"))  # biSize 14
        f.write(width.to_bytes(4, "little"))  # biWidth 18
        f.write(height.to_bytes(4, "little"))  # biHeight 22
        f.write((1).to_bytes(2, "little"))  # biPlanes 26
        f.write((1).to_bytes(2, "little"))  # bitCount 28
        f.write((0).to_bytes(4, "little"))  # biCompression 30
        f.write((112).to_bytes(4, "little"))  # biSizeImage 34
        f.write((0).to_bytes(4, "little"))  # biXPelsPerMeter 38
        f.write((0).to_bytes(4, "little"))  # biYPelsPerMeter 42
        f.write((2).to_bytes(4, "little"))  # biClrUsed 46
        f.write((2).to_bytes(4, "little"))  # biClrImportant 50
        f.write(pal_bytes)
        #f.write(arr[::-1])
        f.write(arr)


def main():
    save_img("t.bmp")
    read_bmp_data("imgs/1.bmp")
    print(test_arr)


if __name__ == "__main__":
    main()
