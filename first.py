import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def refresh(i):
    print("refreshing")
    grdata = open("input.txt", "r").read()
    lines = grdata.split("\n")
    xval = []
    yval = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xval.append(int(x))
            yval.append(int(y))
    ax1.clear()
    ax1.plot(xval, yval)
    print(11111)

ani = animation.FuncAnimation(fig, refresh, interval=1000)
plt.show()
