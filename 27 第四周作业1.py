height,weight = eval(input())
BMI = weight/pow(height,2)
op,yp="",""
if BMI<18.5:
    op,yp = "偏瘦","偏瘦"
if 18.5<=BMI<24:
    op,yp = "正常","正常"
if 24<=BMI<25:
    op,yp = "正常","偏胖"
if 25<=BMI<28:
    op,yp = "偏胖","偏胖"
if 28<=BMI<30:
    op,yp = "偏胖","肥胖"
if BMI>=30:
    op,yp = "肥胖","肥胖"
print("BMI数值为:{:.2f}".format(BMI))
print("BMI指标为:国际'{}',国内'{}'".format(op,yp))