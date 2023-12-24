from bitstring import BitArray


def img_to_bin(img):
    with open(img, 'rb') as f:
        header = f.read(146)
        data = f.read()
    data = BitArray(data)
    # split data
    bd = []
    for i in data:
        bd.append(i)
    d = []
    for i in data:
        if i:
            d.append(0)
        else:
            d.append(1)
    return bd, data, d


def img_to_binf(img: str):
    with open(img.split('.')[0] + '.bb', 'w') as f:
        f.write(img_to_bin(img)[1].bin)


if __name__ == "__main__":
    img_to_binf("imgs/1.bmp")

