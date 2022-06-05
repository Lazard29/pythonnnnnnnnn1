#/usr/bin/python3
#coding: utf-8
import numpy as np 
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

a, b = make_regression(n_samples=100, n_features=1, noise=10)
b = b + abs(b/2)

print (plt.scatter(a,b))

print (a.shape)
b = b.reshape(b.shape[0], 1)
print (b.shape)

#  matrice  grand A

A = np.hstack((a, np.ones(a.shape)))
A = np.hstack((a**2, A ))

print (A.shape)
print (A)

theta = np.random.randn(3,1)
print (theta.shape)
print (theta)


def modelll(A, theta):
    return A.dot(theta)

print (plt.scatter(a,b))
print (plt.plot(a, modelll(A, theta), c="blue"))
print (plt.show())

#  fonction coût : erreur  quoidratique moiyenne 

def fonction_côut(A, b, theta):
    m = len (b)
    return 1/(2*m) * np.sum((modelll(A, theta) - b )**2)

fonction_côut(A, b, theta)

# gradients   

def du_gradient(A, b, theta):
    m = len(b)
    return 1/m * A.T.dot(modelll(A, theta) - b)

#  descente de gradient

def descente_gradient(A, b, theta, learn_rate, n_intérative):
    cout_histoire = np.zeros(n_intérative)
    for i in range (0, n_intérative):
        theta = theta - learn_rate * du_gradient(A, b, theta)
        cout_histoire[i] = fonction_côut(A, b, theta)
    return theta, cout_histoire

# entranement du modèle 

theta_finale, cout_histoire = descente_gradient(A, b, theta, learn_rate=0.01, n_intérative=1000)
print(theta_finale)

prédiction = modelll(A, theta_finale)
plt.scatter(a, b)
plt.plot(a, prédiction, c="green")
print (plt.show())

plt.plot(range(1000), cout_histoire)
print (plt.show())

# coeff de détermination   

def coeff_détermination(b, prédiction):
    u = ((b - prédiction)**2).sum()
    v = ((b - b.mean())**2).sum()
    return 1 - u/v


print (coeff_détermination(b, prédiction))










































































































'''
a = np.array([[1,2], [3,4], [5,6]])

print (a)
print (a.shape)
print (a.T)
'''








































