#字符串加密，用给定字符串替换规则

import sys

KEY1='THEQUICKBROWN'
KEY2='FXJMPSVLAZYDG'
s = 'MEET AT ELEVEN'

def kamaSutra(key1,key2,s):
    sr = ''
    for i in range(len(s)):
        t = key1.find(s[i])
        if t != -1:
            sr +=  key2[t]
        else:
            t = key2.find(s[i])
            if t!= -1:
                sr += key1[t]
            else:
                sr += s[i]
    return sr

print(kamaSutra(KEY1,KEY2,s))
           
