# implement linear regression from scratch
# \hat{\Beta} = (X^T X)^{-1} X^T Y --> closed form solution

# libraries
import numpy as np

# generate random X matrix and Y vector from Gaussian 
nums = np.random.normal(loc=0, scale=1, size=100)
X = np.array(nums.reshape(10, 10))
Y = np.random.normal(loc=1, scale=2, size=10)

# solve
B = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose().dot(Y))
print(B)

# TODO - add bootstrap procedue to estimate p-values for \hat{Beta}