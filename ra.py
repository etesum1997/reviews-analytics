data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0:
            print(len(data)) # 若想知道讀取檔案的進度（讀到第幾筆），可以設定count，再把data長度印出來
print(len(data))
print(data[100])
print('-')
print(data[105])