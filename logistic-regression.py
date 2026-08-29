import numpy as np
import matplotlib.pyplot as plt 
def sigmoid(x):
    return 1/(1+np.exp(-x))
"""x=np.linspace(-10,10,100)
y=sigmoid(x)
plt.plot(x,y)
plt.title("Sigmoid Function")
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.grid(True)
plt.show()   """
#dataset for cancer vs non cancer (1) or (0)
X=np.array([1,2,3,4,5,6,7,8,9,10])
Y=np.array([0,0,0,0,1,1,1,1,1,1])
#initialize weights
w=0.0
b=0.0
learning_rate= 0.1
# train for 1000 iterations 
for i in range (1000):
    z=w*X+b
    Y_pred=(sigmoid(z))
    #claculate the gradients
    dw=np.mean((Y_pred-Y)*X)
    db=np.mean(Y_pred-Y)
#update the weights and bias
    w = w-learning_rate*dw
    b = b-learning_rate*db
print(f"weights: {w:.4f}")
print(f"bias: {b:.4f}")
plt.scatter(X,Y, color='blue',label='Actual')
plt.plot(X,Y_pred, color='red' , label='Predicted')
plt.title("Logistic Regereesion from Scratch")
plt.xlabel("Tumor Size")
plt.ylabel("Cancer probability")
plt.legend()
plt.grid(True)
plt.show()
