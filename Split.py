data=input('데이터 입력(구분은 공백): ')
data=data.split()
total=0
for v in data:
    total += int(v)

print(total)