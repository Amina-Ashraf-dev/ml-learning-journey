import numpy as np
import matplotlib.pyplot as plt
#study hours vs scores
X=np.array([1,2,3,4,5,6,7,8,9,10])
Y=np.array([20,35,40,50,65,70,80,85,90,95])
"""plt.scatter(X,Y)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Scores")
plt.show()"""
#claculating the slope (m) and intercept (b)
m=np.sum((X-X.mean())*(Y-Y.mean()))/np.sum((X-X.mean())**2)
b=Y.mean()-m*X.mean()
print(f"slope:{m}")
print(f"intercept:{b}")
#Draw the line
Y_pred=m*X+b
plt.scatter(X,Y)
plt.plot(X,Y_pred,color='red')
plt.xlabel("study hours")
plt.ylabel("marks")
plt.title("Linear Regression")
plt.show()


