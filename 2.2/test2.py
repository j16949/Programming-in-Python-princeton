def func_a(func,args):
    print(func(args))

def func_b(args):
    return args

if __name__ == '__main__':
    a=[1,2,3]
    func_a(func_b,a)
