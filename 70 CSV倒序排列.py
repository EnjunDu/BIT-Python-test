import csv
# 读取CSV文件并将数据存储在列表中
data = []
with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
# （1）按行进行倒序排列
data.reverse()
# （2）每行数据倒序排列
for i in range(len(data)):
    data[i].reverse()
# （3）使用分号（;）代替逗号（,）分割数据
for i in range(len(data)):
    data[i] = ';'.join(data[i])
# 将处理后的数据print输出，去除字符之间的空格
for row in data:
    print(row.replace(' ', ''))
