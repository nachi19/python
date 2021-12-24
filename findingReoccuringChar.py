def recurring_char(string):
    print("string passed", string)
    unique_chars=sorted(list(set(string)))
    print("unique characters ",unique_chars)
    i=0
    j=0
    temp=[]
    mainList=[]
    while i < len(unique_chars):
        while j < len(string):
           if string[i] == unique_chars[j]:
            #append the value to list
            temp=string[i]
            j=j+1
        mainList.append(temp)
    return mainList



strings="MyNameisName"
res=recurring_char(sorted(strings))
print(res)
