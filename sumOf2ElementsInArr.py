def sumOfElem(a,sumele):
    j=0
    i=0
    print("length of list",len(a))
    for i in range(0,len(a)):
        while j < len(a):
          print(f"i={i},j={j}")
          if a[i]+a[j]==sumele:
              return a[i],a[j]
          j=j+1
        j=0



l=[1,4,5,8,10,12,3]
sumele=5
res=sumOfElem(l,sumele)
print(res)