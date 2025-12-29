#  NumPy 배열 연산
#  NumPy 배열은 다른 배열 또는 스칼라와의 연산을 지원
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

c = a + b
d = a * b
e = a + 1

a = np.array([1,2,3])

b = np.sum(a) # 6
c = np.mean(a) # 2.0
d = np.min(a) # 1
e = np.max(a) # 3

print(b)
print(c)
print(d)
print(e)

# 다차원 NumPy 배열에서는 각 차원의 인덱스를 콤마로 구분하여 인덱싱 할 수 있다.
a = np.array([[1,2,3],[4,5,6]])

# 인덱싱
b = a[0,0] # 1
c = a[1,2] # 6

# 슬라이싱
d = a[0, 1:3] 
# [2 3]
e = a[:,1]
# [2 5]
f = a[:,:2]
# [[1 2]
#  [4 5]]

print(b) 
print(c)
print(d)
print(e)
print(f)
