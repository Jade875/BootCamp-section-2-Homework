#Jadesola Kassim
#HW Questions Numpy

#question 1
import numpy as np
A = np.array([0, 2, 4, 6, 8, 10, 12])
B = np.arrary([0, 1, 3, 5, 7, 9, 11])

v_stack = np.vstack([A, B])
h_stack = np.hstack([A, B])

print("v_stack:", v_stack)
print(" h_stack:", h_stack)

#question 2
commonset= np.intersect1s(A,B)
print("common elemets:", commonset)

#question 3
idx = np.where((A >= 5) and (A <= 10))[0]
print("Range =", idx)

#question 4
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

petallenght = iris_2d[:, 2]
sepallenght = iris_2d[:, 0]

m = (petallenght > 1.5) and (sepallenght < 5.0)
filter = iris_2d[m]