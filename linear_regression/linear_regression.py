# implement linear regression from scratch
# \hat{\Beta} = (X^T X)^{-1} X^T Y --> closed form solution

# libraries
import numpy as np

# generate random X matrix and Y vector from Gaussian 
nums = np.random.normal(loc=0, scale=1, size=100)
x = nums.reshape(10, 10)
y = np.random.normal(loc=1, scale=2, size=10)

# implement as function
def solveOLS(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    B = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose().dot(Y))
    return B;

beta = solveOLS(X=x, Y=y)
print(beta)

# TODO - add bootstrap procedue to estimate p-values for \hat{Beta}