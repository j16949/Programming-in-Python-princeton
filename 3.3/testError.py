#没有try except时
'''
while True:
    x = int(input('请输入数字:'))
'''
#用try except
while True:
    try:
        x = int(input('请输入数字:'))
    except:
        print('输入数字非法。')
