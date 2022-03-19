import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

# plt.plot(gas.Year, gas.USA, label="USA", marker='o')
#
# plt.plot(gas.Year, gas.Canada, label="Canada", marker='8')
# plt.title('Gas Prices')
plt.show()

# defining labels
activities = gas.head(0)

# portion covered by each label
slices = [3, 7, 8, 6]

# color for each label
colors = ['r', 'y', 'g', 'b']

# plotting the pie chart
plt.pie(slices, labels=activities, colors=colors,
        startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
        radius=1.2, autopct='%1.1f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()