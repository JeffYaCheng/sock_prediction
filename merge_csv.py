import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
#glob是一個檔名模式匹配(filename pattern matching)模組(Module)，用來定義檔案規則，取得相匹配的檔案清單串列(List)
#讓我們在合併多個檔案資料的過程中，能夠一次取得所有的檔案清單，提升讀取效率
files = glob(r'D:\111-1\machine_learning\make_change_rate_data/*.csv')
print("file length=",len(files))
df = pd.concat(
    (pd.read_csv(file, encoding='Big5', usecols=[r'日期',r'美元／新台幣',r'人民幣／新台幣'], dtype={ r'日期': str, r'美元／新台幣':str,r'人民幣／新台幣': str}) for file in files),ignore_index=True)
df.to_csv(f"exchage_rate.csv")
print("df shape=",df.shape[0],df.shape[1])
print(df.head())
print(df.tail())
buy_list=list(df.loc[:,'人民幣／新台幣'])
print("buy_list type=",type(buy_list))
print("buy_list length=",len(buy_list))
df = df.set_index('日期')  # 指定日期欄位為datafram的index
df = df.sort_index(ascending=True)
plt.figure(figsize=(30, 8))
df['人民幣／新台幣'].plot()  # x=['date'], y=[['buy_rate','sell_rate']] 
plt.legend(loc="upper left")
plt.show()
