fo =open("data.csv").readlines()
ls = []
for line in fo:
    line =line.replace('\n',"")
    line=line.split(",")
    print(",".join(line[::-1]))
fo.close()