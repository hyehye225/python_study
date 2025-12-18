# join , append, range, list


print("hello python!")

colors = ['red','blue','green','yellow']
result = ''
for s in colors:
    result += s

## 1) join
result = ','.join(colors); # 좋은 코드
# 앞의 문자로 join
print(result)
# list 값 들을 하나의 문자열로 합침

# 2) append > 뒤에 추가
result = []
for i in range(10):
    result.append(i)

print(result)

# 3) range() # 일정 범위의 연속된 정수 생성

# 4) list 함수 > 리스트의 형식을 반환
a = [10,20,30,40,50]
print(list(a))
















