r = int(input('Enter no of Rows: '))
c = int(input('Enter no of Cols: '))
arr=[
  [(i*j)for j in range(c)]
  for i in range(r)
  ]

print(arr)