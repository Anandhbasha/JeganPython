import numpy as np

# # 1d Array 
# arr1D = np.array([10,20,30,40])
# print(arr1D)

# arr2d = np.array([[20,40,60,80],[50,10,150,200]])

# arr3d = np.array([[20,40,60,80],[50,10,150,200],[30,60,90,120]])
# print(arr3d)

# zeros = np.zeros((3,4))
# print(zeros)

# ones = np.ones((2,3))
# print(ones)

# eye = np.eye(3)

# print(eye)

# rangeArr = np.arange(0,10,2)

# print(rangeArr)


# linSpace = np.linspace(0,1,5)

# print(linSpace)

# random = np.random.rand(2,2)
# print(random)

# arr2d = np.array([[20,40,60,80],[50,10,150,200]])

# print(arr2d[0,0])

# # col
# arr3d = np.array([[20,40,60,80],[50,10,150,200],[30,60,90,120]])
# print(arr3d[:,2])
# print(arr3d[0:2,1:3])

arr = np.array([1,2,3,4,5])

# print(arr[arr>3])

arr1 = np.array([5,10,20,40,50])

print(arr+10)


# transpose
# arr1 = np.array([[10,20],[50,100]])

# print(arr1.T)

print(np.sum(arr1))
print(np.mean(arr1))
print(np.max(arr1))
print(np.min(arr1))
print(np.std(arr1))


arr = np.arange(12)

print(arr)

res = arr.reshape(3,4)
print(res)

flat = res.flatten()
print(flat)