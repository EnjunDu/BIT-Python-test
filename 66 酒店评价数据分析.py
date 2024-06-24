import jieba
with open('comment.csv', 'r', encoding='GBK') as f:
    ls=[i.strip().split(',',maxsplit=1) for i in f.readlines()[1:]]
