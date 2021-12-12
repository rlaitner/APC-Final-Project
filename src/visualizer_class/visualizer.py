import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation



uav = UAV("UAV", (0,0), 1)


sequence = []
U = [1,1]
position = uav.update_dynamics(0,0, U)
sequence.append(position)
for i in range(0, 10):
    position = uav.update_dynamics(position[0], position[1], U)
    sequence.append(position)
    
U = [0,0.5]
for i in range(0, 10):
    position = uav.update_dynamics(position[0], position[1], U)
    sequence.append(position)    

    
U = [1,0.3]
for i in range(0, 10):
    position = uav.update_dynamics(position[0], position[1], U)
    sequence.append(position) 


    
fig, ax = plt.subplots()

ax.set_xlim(0,20)
ax.set_ylim(0,20)
plt.plot(x,y, c="black")
drone = plt.Circle((1, 1), 1, fc='black')


x_line = np.zeros(len(sequence))
y_line = np.zeros(len(sequence))

for i in range(0, len(sequence)):
    x_line[i] = sequence[i][0]
    y_line[i] = sequence[i][1]




def init():
    drone.center = (1,1)
    ax.add_patch(drone)
    return drone

def animate(i):
    x, y = drone.center
    x = sequence[i][0]
    y = sequence[i][1]
    drone.center = (x, y)
    return drone

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=1000, 
                               interval=200,
                               blit=True)

plt.show()

