import numpy as np
mat=np.array([[2,1],[4,5]])

eigen,feature=np.linalg.eig(mat)

print("特征值:",eigen)

print("特征向量:",feature)