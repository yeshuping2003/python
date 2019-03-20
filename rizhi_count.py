import pandas as pd

chunks = pd.read_csv('20190301_csv.csv',  header=0, iterator = True, engine='python')
chunk1 = chunks.get_chunk(1100000)
print('事件日志记录数 : ', len(chunk1))
count = pd.DataFrame(pd.value_counts(chunk1['Unnamed: 5'].values,  sort=1))
print("不同日志个数 ：", len(count))
print("按照出现次数排序 : ")
count