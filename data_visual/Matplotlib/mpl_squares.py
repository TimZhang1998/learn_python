import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value ,squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

""" x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]

plt.scatter(x_value, y_value, s=200)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14) """

""" x_values = list(range(1, 1001))
y_values = [x_values**2 for x_values in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

plt.axis([0, 1100, 0, 1100000])

# plt.savefig('Square Numbers_cmap.png', bbox_inches='tight') """

plt.show()