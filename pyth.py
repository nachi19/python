ts=['2021-01-01','2021-01-02','2021-01-08']
def print_list(*args):
    arg1,arg2 = args
    return arg1,arg2
ret=print_list(ts,"iii")
print(ret)