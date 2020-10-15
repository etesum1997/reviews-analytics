data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f: # 寫for loop來一筆一筆讀裡面的資料
        data.append(line)
        count += 1 # count = count + 1
        if count % 10000 == 0:
            print(len(data)) # 若想知道讀取檔案的進度（讀到第幾筆），可以設定count，再把data長度印出來
print('檔案讀取完了，總共有', len(data), '筆資料')
sum_len = 0 # 總長度
for d in data:
    sum_len += len(d) # sum_len = sum_len + len(d) # 每筆長度加上前面累積的總長，再存回總總長
print('留言的平均長度為', sum_len / len(data))

new = []
for d in data: # 把data裡的資料一筆一筆讀出來
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆資料小於100字')
print(new[5])

awful = []
for d in data:
    if 'awful' in d:
        awful.append(d)
print('一共有', len(awful), '筆資料提及\'awful\'')
print('For example:', '\'', awful[0], '\'')