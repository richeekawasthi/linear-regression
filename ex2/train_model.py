import numpy as np
import random

def assign():
	i=open("ex1data2.txt").read()
	l=i.split("\n")
	m=len(l)
	n=len(l[0].split(","))
	price=np.ndarray(shape=(m), dtype=int)
	feature=np.ndarray(shape=(m,n),dtype=float)
	for i in range(m):
		a=l[i].split(",")
		price[i]=a[-1]
		#print(price[i])
		for j in range(n):
			if(j==0):
				feature[i][j]=1
			else:
				feature[i][j]=a[j-1]     
	theta=np.random.randn(n)
	for i in range(n):
		ftr=[feature[j][i] for j in range(m)]
		mean=sum(ftr)/m
		for j in range(m):
			feature[j][i]=(feature[j][i]-mean)/m
	for j in range(m):
		feature[j][0]=1
	return feature,price,theta,m,n

def Jtheta(feature,theta,m,n):
	jtheta=[sum(feature[i]*theta) for i in range(m)]
	return jtheta

def computeCost(feature,price,theta,m,n):
    jtheta=Jtheta(feature,theta,m,n)
    err=(jtheta-price)/m
    return err

def computeError(feature,price,theta,m,n):
	err=computeCost(feature,price,theta,m,n)
	err=err**2*m/2.0
	return sum(err)

def matmul(a,b):
	m=len(a)
	n=len(b[0])
	c=np.ndarray(shape=(n),dtype=float)
	for i in range(n):
		c[i]=0
		for j in range(m):
			c[i]+=a[j]*b[j][i]
	return c

def gradientDescent(feature,price,theta,m,n,rate,iterations):
	for i in range(iterations):
		theta=theta-rate*(matmul(computeCost(feature,price,theta,m,n),feature))
		print("Iteration No. : " + str(i+1) + " Error: " + str(computeError(feature,price,theta,m,n)))
	return theta

feature,price,theta,m,n=assign()
rate=float(input("Enter Learning Rate: "))
iterations=int(input("Enter number of iterations: "))
theta=gradientDescent(feature,price,theta,m,n,rate,iterations)
f=open("./result.txt",'w')
f.write(str(theta))
f.close()