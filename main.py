import pandas as pd
import os

pth = os.path.join(os.getcwd(), 'imgs') + '/'
imgs = [pth + str(i) + '.bmp' for i in range(1, 1001)]
num_types = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
annotations = ([(imgs[i-1], num_types[(i-1) // 100]) for i in range(1, 1001)])


pd.DataFrame(annotations, columns=['image', 'type']).to_csv('annotations.csv', index=False)