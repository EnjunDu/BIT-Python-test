import jieba
with open('comment.csv', 'r', encoding='GBK') as f:
    ls=[i.strip().split(',',maxsplit=1) for i in f.readlines()[1:]]

def comments():
    good=0
    bad=0
    for line in ls:
        if line[0]=='1':
            good+=1
        if line[0]=='0':
            bad+=1
    print("总评论: {}\n好评: {}\n差评: {}".format(good+bad,good,bad))

def average():
    sum =0
    n=0
    for line in ls:
        comment_text = line[1]  # 获取评论文本
        sum+=len(comment_text)
        n+=1
    print("{}".format(round(sum/n)))

def goodcomments():
    s=[]
    for line in ls:
        if line[0]=='1':
            s.append(line[1])
    good_comments_text = ''.join(s)
    words =jieba.lcut( good_comments_text)
    counts={}
    excludes={'不错','比较','可以','感觉','没有', '我们','就是','还是','非常','但是', '不过','有点','一个','一般','下次',  '携程','不是','晚上','而且','他们', '什么','不好','时候','知道','这样', '这个','还有','总体','位置','客人', '因为','如果','这里','很多','选择','居然','不能','实在','不会','这家','结果','发现','竟然','已经','自己','问题','不要','地方','只有','第二天','酒店','房间','虽然'}
    for word in words :
        if len(word)==1 or word.isdigit():
            continue
        counts[word]=counts.get(word,0)+1
    for word in excludes:
        del counts[word]
    items = list(counts.items())
    items.sort(key=lambda  x:x[1],reverse =True)
    for i in range(15):
        word, count = items[i]
        print("{}: {}".format(word,count))

def badcomments():
    s=[]
    for line in ls:
        if line[0]=='0':
            s.append(line[1])
    bad_comments_text = ''.join(s)
    words =jieba.lcut( bad_comments_text)
    counts={}
    excludes={'不错','比较','可以','感觉','没有', '我们','就是','还是','非常','但是', '不过','有点','一个','一般','下次',  '携程','不是','晚上','而且','他们', '什么','不好','时候','知道','这样', '这个','还有','总体','位置','客人', '因为','如果','这里','很多','选择','居然','不能','实在','不会','这家','结果','发现','竟然','已经','自己','问题','不要','地方','只有','第二天','酒店','房间','虽然'}
    for word in words :
        if len(word)==1 or word.isdigit():
            continue
        counts[word]=counts.get(word,0)+1
    for word in excludes:
        del counts[word]
    items = list(counts.items())
    items.sort(key=lambda  x:x[1],reverse =True)
    for i in range(15):
        word, count = items[i]
        print("{}: {}".format(word, count))

def main():
    op=input()
    if op=='总评':
        comments()
    elif op=='平均':
        average()
    elif op=='好评':
        goodcomments()
    elif op=='差评':
        badcomments()
    else:
        print("无数据")

if __name__ == "__main__":
    main()
