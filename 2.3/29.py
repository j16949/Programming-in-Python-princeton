#实验发现，当n小于等于101时，最终都收敛与91；大于101时，为n-10的值
def mcCarthy(n):
    if n > 100: 
        #print(n)
        return n - 10
    #print(n)
    return mcCarthy(mcCarthy(n+11))

for i in range(85,124):
    print(i,mcCarthy(i))

'''
bai@ubuntu:~/pythonProject/princeton/2.3$  cd /home/bai/pythonProject/princeton/2.3 ; /usr/bin/env /usr/bin/python3 /home/bai/.vscode/extensions/ms-python.python-2020.12.424452561/pythonFiles/lib/python/debugpy/launcher 39563 -- /home/bai/pythonProject/princeton/2.3/29.py 
89 91
90 91
91 91
92 91
93 91
94 91
95 91
96 91
97 91
98 91
99 91
100 91
101 91
102 92
103 93
104 94
105 95
106 96
107 97
108 98
109 99
110 100
111 101
112 102
113 103
'''