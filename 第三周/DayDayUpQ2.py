# dayfactor = 0.01
# dayup = pow(1+dayfactor,365)
# daydown = pow(1-dayfactor,365)
# print("向上：{:.2f}，向下：{:.2f}".format(dayup,daydown))

dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i%7 in [6,0]:
        dayup = dayup * (1-dayfactor)
    else:
        dayup = dayup * (1+dayfactor)

print("工作日的力量:{:.2f}".format(dayup))
