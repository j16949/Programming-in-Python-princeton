#安全口令是否合规验证

import sys
import re

pwd = sys.argv[1]

def pwdVerify(pwd):
    if len(pwd) < 8:
        return False
    if not re.search('\d',pwd):
        return False
    if not re.search('[a-z]',pwd):
        return False
    if not re.search('[A-Z]',pwd):
        return False
    if not re.search('\W',pwd):
        return False
    return True

print(pwdVerify(pwd))
