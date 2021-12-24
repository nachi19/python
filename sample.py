def run(n):
  if n==0:
    return
  run(n-1)
  print(n)

res=run(3)
print(res)