#去除空白行
import sys

def emovingWhitespace(oFile):
    with open(oFile, 'r') as file:
        for line in file:
            if line != '\n' and (line.strip()!= ''):    #python3.8.5    strip()默认会去掉结尾的'\n'
                print(line,end='')
                with open('201.py','a') as f:
                    f.write(line)

oFile = '19.py'
emovingWhitespace(oFile)

