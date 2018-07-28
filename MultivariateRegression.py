import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

#import data
data2 = pd.read_csv("c:\\Users\\ande5\\LearningPython\\data\\ex1data2.txt", header=None, names=['Size','Bedrooms','Price'])

#normalize data2
data2 = (data2 - data2.mean()) / data2.std()

def compute_cost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

def gradient_descent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = compute_cost(X, y, theta)
    
    return theta, cost

#add ones column
data2.insert(0, 'Ones', 1)

#set theta, X and y
cols = data2.shape[1]
X2 = np.matrix(data2.iloc[:,0:cols-1].values)
y2 = np.matrix(data2.iloc[:,cols-1:cols].values)
theta2 = np.matrix(np.array([0,0,0]))

#alpha and inters
alpha = 0.01
iters = 1000

#perform linear regression
g2, cost2 = gradient_descent(X2, y2, theta2, alpha, iters)

#cost of model
print(compute_cost(X2, y2, g2))

#plot cost
fig, ax = plt.subplots(figsize=(12,8))  
ax.plot(np.arange(iters), cost2, 'r')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch') 

plt.show()