#/usr/bin/python
import numpy as np
import random
import matplotlib.pyplot as plt

def computeCost(population,profit,theta):
    err=[]
    jtheta=[]
    for city in population:
        jtheta.append(theta[0]+city*theta[1])
    for pprofit,profit in zip(jtheta,profit):
        err.append((pprofit-profit)*(pprofit-profit)*0.5)
    return err
theta0=random.uniform(-1,1)
theta1=random.uniform(-1,1)
theta=[]
theta.append(theta1)
theta.append(theta0)
i=open("ex1data1.txt").read()
l=i.split("\n")
del l[-1]
population=[]
profit=[]
for x in l:
	a=x.split(",")
	population.append(float(a[0]))
	profit.append(float(a[1]))
#plt.scatter(population,profit)
#plt.xlabel("Population")
#plt.ylabel("Profit")
#plt.show()
error=computeCost(population,profit,theta)
l=len(population)
#print(sum(error)/l)
