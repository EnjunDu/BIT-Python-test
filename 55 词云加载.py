import jieba
import wordcloud
from scipy.misc import imread
mk = imread("fivestart.png")
f = open("关于实施乡村振兴战略的意见.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls =jieba.lcut(t)
txt = " ".join(ls)
w =wordcloud.WordCloud(     font_path="msyh.ttc",mask=mk,width=1000,height=700,background_color="white")
w.generate(txt)
w.to_file("gywordcloud.png")