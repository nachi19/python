def numbers(num):
    A = []
    for i in range(num):
        A.append(str(i+1))
    print(A)
    b = ''.join(A)
    return b
result = numbers(10)
print(result)