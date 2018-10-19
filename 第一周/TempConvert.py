# -*- coding: utf-8 -*-

TempStr = input('请输入带有符号的温度值:')
if TempStr[-1] in ['f', 'F']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ["C",'c']:
    F = 1.8* eval(TempStr[0:-1]) +32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")

TempStr2 = input('请输入带有符号的温度值:')
if TempStr2[0] in ['f', 'F']:
    C2 = (eval(TempStr2[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C2))
elif TempStr2[-1] in ["C",'c']:
    F2 = 1.8* eval(TempStr2[0:-1]) +32
    print("转换后的温度是{:.2f}F".format(F2))
else:
    print("输入格式错误")

TempStr3 = input()
if TempStr3[0 : 3] in ['RMB']:
    USD = eval(TempStr3[3:]) / 6.78
    print("USD{:.2f}".format(USD))
elif TempStr3[0:3] in ['USD']:
    RMB = 6.78 * eval(TempStr3[3:])
    print("RMB{:.2f}F".format(RMB))
