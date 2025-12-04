import numpy as np
f = np.loadtxt("input", dtype=str)

list1 = []
big_arr = []
for i in f:
    list1 = list(i)
    arr = np.array(list1)
    big_arr.append(arr)
mat = np.array(big_arr)
mat[mat == '@'] = 1
mat[mat == '.'] = 0
mat = np.array(mat,dtype=int)

count = 0
removed = True

# Keep going as long as something is removed 
while removed:
    mat_new = mat
    removed = False
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            region = mat[max(0,i-1):i+2,max(0,j-1):j+2]
            if(mat[i,j] == 1 and (np.sum(region) - mat[i,j]) < 4):
                mat_new[i,j] = 0
                removed = True
                count += 1
print(count)
