
#project1
# we chose to discuss the difference between a man and a womans wage income
# we are going to show our results on bar-charts 
import matplotlib.pyplot as ply
#age group 15-24
price1 = (11.25 + 12.47)/2
print(price1)
#age group 25-49
price2 = (22.67 + 20.42)/2
print(price2)
#age group 50-64
price3 = (26.28 + 22.61)/2
print(price3)
#age group 65+
price4 = (20 + 19.98)/2
print(price4)

averageprice = [11.86, 21.54, 24.45, 19.990]
age = ["15-24", "25-49", "50-64", "65+"]
difference = [-1.22, 2.25, 3.67, 0.02]

women = [12,47 ,20 ,42, 22.61, 19.98]
men = [11.25, 22.67, 26.28, 20]

n=4
r = np.arange(n)
width = 0.25

ply.bar[r, ]

