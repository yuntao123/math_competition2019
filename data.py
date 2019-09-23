import numpy as np
import pandas as pd
def get_data(st,row):
    # data = pd.read_csv("./data_set/文件1修正1-3.csv", header=0,encoding='gbk')  # 要哪行就排除剩下的几行
    # data = pd.read_csv("./data_set/pianduan1.csv", header=0, encoding='gbk')  # 要哪行就排除剩下的几行
    data = pd.read_csv("./data_set/feature_PCA_1.csv", header=0, encoding='gbk')  # 要哪行就排除剩下的几行
    data = np.array(data)
    x = data[:, st:row]
    print(data.shape)
    return x
get_data(0,1)
#
# print(x)