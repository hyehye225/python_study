import numpy as np

# Fancy Indexing
array = np.array([10,20,30,40,50])
print(array[[0,2,4]]) # [10 30 50]

# 1) 2차원 배열에서 팬시 인덱싱
array_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(array_2d[[0,2],[1,0]]) # [2 7]

# 팬시 인덱싱 > 정수나 불린 값을 가지는 다른 Numpy 배열로 배열을 인덱싱할 수 있는 기능
# Boolean 값을 가진 배열을 사용하여 직관적으로 인덱싱 가능
arr = np.array([i for i in range(10)])
idx = np.array([True, False, True, False, True, False, True, False, True, False])

print(arr)
print(idx)
print(arr[idx]) # [0 2 4 6 8]
print(arr %2) # [0 1 0 1 0 1 0 1 0 1]
print(arr%2 == 0) # [ True False  True False  True False  True False  True False]
print(arr[arr %2 == 0]) # [0 2 4 6 8]

# arr에서 3으로 나누면 나눠지고 4로 나누면 1이 남는 수
print((arr[(arr%3 ==0) & (arr%4 ==1)])) # [9]
