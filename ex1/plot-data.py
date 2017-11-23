import matplotlib.pyplot as plt

def assign():
    theta=[]
    s=open('result.txt').read().split("\n")
    theta.append(float(s[0]))
    theta.append(float(s[1]))
    i=open("ex1data1.txt").read()
    l=i.split("\n")
    population=[]
    profit=[]
    for x in l:
            a=x.split(",")
            population.append(float(a[0]))
            profit.append(float(a[1]))
    return population,profit,theta

population,profit,theta=assign()
plt.scatter(population,profit),plt.plot([theta[0]+theta[1]*x for x in range(30)])
plt.show()
