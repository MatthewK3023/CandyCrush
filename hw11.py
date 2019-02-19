import numpy as np   # import packages
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("candy_input1.txt", header=None)   # read txt file
#data=pd.read_csv("candy_input2.txt", header=None)

while True:   # main code for candy crush
    box=[]
    for x in range(data.shape[1]):       # 列 掃描
        for y in range(data.shape[0]-2):
            if (data.iloc[y,x]==data.iloc[y+1,x]) and (data.iloc[y,x]==data.iloc[y+2,x]) and (data.iloc[y,x]!=0):
                box.append(y*10+x); box.append((y+1)*10+x); box.append((y+2)*10+x)   # 收集 列 相連值 的坐標
    for y in range(data.shape[0]):       # 行 掃描
        for x in range(data.shape[1]-2):
            if (data.iloc[y,x]==data.iloc[y,x+1]) and (data.iloc[y,x]==data.iloc[y,x+2]) and (data.iloc[y,x]!=0):
                box.append(y*10+x); box.append(y*10+x+1); box.append(y*10+x+2)   # 收集 行 相連值 的坐標
    box=list(set(box))   # 去除重複的判定值
    data_map=pd.DataFrame(np.ones(shape=(data.shape[0],data.shape[1])))
    for i in range(len(box)):   # 建立新data frame 以0與1為記錄符號 
        data_map.iloc[box[i]//10, box[i]%10]=0   # 0為相連值的坐標 1為非相連值的坐標 
    if (data_map == 0).sum().sum() == 0: break   # 用以判斷資料  當前是否仍存在 相連值； 假設不再存在相連值 則結束code的運作
    for x in range(data.shape[1]):
        col0=data_map[x][data_map[x]==0]   # 將當前 的相連值進行去除； 非相連值進行往後移位； 空缺的坐標位置以0補上 
        col1=data[x][data_map[x]==1]
        data[x]=pd.concat([col0,col1],axis=0,ignore_index=True)
    print(data)

fmt=""; length=str(len(str(int(data.values.max()))))   # output txt file
for i in range(data.shape[1]): 
    fmt=fmt+"%"+length+"d"
    if i != (data.shape[1]-1): fmt=fmt+", "
np.savetxt('candy_output.txt', data.values, fmt=fmt)