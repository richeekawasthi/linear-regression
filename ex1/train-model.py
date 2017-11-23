#/usr/bin/python
import numpy as np
import random
import matplotlib.pyplot as plt

def assign():
	theta0=random.uniform(-1000,1000)
	theta1=random.uniform(-1000,1000)
	theta=[]
	theta.append(theta1)
	theta.append(theta0)
	i=open("ex1data1.txt").read()
	l=i.split("\n")
	population=[]
	profit=[]
	for x in l:
	        a=x.split(",")
	        population.append(float(a[0]))
	        profit.append(float(a[1]))
	return population,profit,theta

def Jtheta(population,theta):
	jtheta=[]
	for city in population:
        	jtheta.append(theta[0]+city*theta[1])
	return jtheta

def computeCost(population,profit,theta):
    err=[]
    m=len(population)
    jtheta=Jtheta(population,theta)
    for pprofit,profitt in zip(jtheta,profit):
        err.append((pprofit-profitt)/m)
    return err

def computeError(population,profit,theta):
	err=computeCost(population,profit,theta)
	m=len(population)
	for i in range(m):
		err[i]=err[i]*err[i]*m/2.0
	return sum(err)

def matmul(a,b):
	result=[]
	for ai,bi in zip(a,b):
		result.append(ai*bi)
	return result

def gradientDescent(theta,population,profit,rate,iterations):
	m=len(population)
	for i in range(iterations):
		temp1=theta[0]-rate*sum(computeCost(population,profit,theta))
		temp2=theta[1]-rate*sum(matmul(population,computeCost(population,profit,theta)))
		theta[0]=temp1
		theta[1]=temp2
		print("Iteration No. : " + str(i+1) + " Error: " + str(computeError(population,profit,theta)))
	return theta

population,profit,theta=assign()
#plt.scatter(population,profit)
#plt.xlabel("Population")
#plt.ylabel("Profit")
#plt.show()
rate=float(input("Specify Learning Rate: "))
iterations=int(input("Specify Number of iterations: "))
theta=gradientDescent(theta,population,profit,rate,iterations)
f=open("result.txt",'w')
s=str(theta[0])+"\n"+str(theta[1])+"\nError: "+str(computeError(population,profit,theta))
f.write(s)
f.close()
