import matplotlib.pyplot as plt
#
# x=[1,2.25,3]
# y=[2,4,1]
#
# plt.plot(x, y)
#
# plt.xlabel('x - axis')
#
# plt.ylabel('y - axis')
#
# plt.title('My first graph!')
#
# plt.show()
# ****************************************************
x1=[1,2,3]
y1=[2,4,1]

plt.plot(x1, y1, label='line 1', color='green', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='red', markersize=10)

x2=[1,2.1,3.20]
y2=[4,1,3]

plt.plot(x2, y2, label='line 2', linewidth=4, marker='1', markerfacecolor='red',
         markersize=25)

x3=[1,3,1]
y3=[1,3,2]
plt.plot(x3, y3, label='line 3', color='blue', linestyle='dotted', linewidth=2)

plt.xlabel('x ')
plt.ylabel('y - axis')

plt.title('Multiple line in python!')
plt.legend()
plt.show()