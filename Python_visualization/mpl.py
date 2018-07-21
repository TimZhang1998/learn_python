import matplotlib.pyplot as plt
import matplotlib as mpl


data = list(range(10))
data = list(map(lambda x:x*x, data))
# print(data)

plt.plot(data)
plt.show()