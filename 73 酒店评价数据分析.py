import jieba


def total():
    print('总评论:', len(ls))
    lp = [i[0] for i in ls]  # 统计好评和差评的0/1列表
    print('好评:', lp.count('1'))
    print('差评:', lp.count('0'))


def goodcomment():
    lgood = [i[1] for i in ls if i[0] == '1']
    good = ''.join(lgood)  # 好评字符串
    lq = jieba.lcut(good)
    d = {}
    for i in lq:
        if len(i) > 1 and i.isdigit() == False and i not in ex:
            d[i] = d.get(i, 0) + 1
    p = sorted(d.items(), key=lambda x: x[1], reverse=True)[:15]
    for i in p:
        print(i[0] + ':', i[1])


def badcomment():
    lbad = [i[1] for i in ls if i[0] == '0']
    bad = ''.join(lbad)  # 差评字符串
    lt = jieba.lcut(bad)
    d = {}
    for i in lt:
        if len(i) > 1 and i.isdigit() == False and i not in ex:
            d[i] = d.get(i, 0) + 1
    p = sorted(d.items(), key=lambda x: x[1], reverse=True)[:15]
    for i in p:
        print(i[0] + ':', i[1])


def ave():
    s = sum([len(i[1]) for i in ls]) / len(ls)
    print('{:.0f}'.format(s))


with open('comment.csv', 'r', encoding='GBK') as f:
    ls = [i.strip().split(',', maxsplit=1) for i in f.readlines()[1:]]

ex = ['不错', '比较', '可以', '感觉', '没有',
      '我们', '就是', '还是', '非常', '但是',
      '不过', '有点', '一个', '一般', '下次',
      '携程', '不是', '晚上', '而且', '他们',
      '什么', '不好', '时候', '知道', '这样',
      '这个', '还有', '总体', '位置', '客人',
      '因为', '如果', '这里', '很多', '选择',
      '居然', '不能', '实在', '不会', '这家',
      '结果', '发现', '竟然', '已经', '自己',
      '问题', '不要', '地方', '只有', '第二天',
      '酒店', '房间', '虽然']
n = input()
if n == '总评':
    total()
elif n == '平均':
    ave()
elif n == '好评':
    goodcomment()
elif n == '差评':
    badcomment()
else:
    print('无数据')