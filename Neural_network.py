import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def relu(X):
    return np.maximum(0,X)
#Dataset
x=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y=np.array([[0],[0],[0],[0],[1],[1],[1],[1],[1],[1]])
#initialize the weights and bias
#np.random.seed(42)
W1=np.random.rand(1,4)*0.1
b1=np.zeros((1,4))
W2=np.random.rand(4,1)*0.1
b2=np.zeros((1,1))
learning_rate=0.01
for i in range(10000):
    #forward pass
    Z1=np.dot(x,W1)+b1
    A1=relu(Z1)
    Z2=np.dot(A1,W2)+b2
    A2 =sigmoid(Z2)
    #Calculate the error
    error=A2-y
    #Backpropagation 
    dW2=np.dot(A1.T,error)
    db2=np.sum(error)
    dA1=np.dot(error,W2.T)
    dZ1=dA1*(Z1>0)
    dW1=np.dot(x.T, dZ1)
    db1=np.sum(dZ1)
    #update weights
    W1-=learning_rate*dW1
    b1-=learning_rate*db1
    W2-=learning_rate*dW2
    b2-=learning_rate*db2
print("After Training ")
print(A2)