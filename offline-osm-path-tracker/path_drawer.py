import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class PathDrawer:
    def __init__(self, bounds, start_pos):
        self.minx, self.miny, self.maxx, self.maxy = bounds
        self.current_pos = np.array(start_pos)
        self.path = [self.current_pos.copy()]

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'r-', linewidth=2, label='Path')
        self.dot, = self.ax.plot([], [], 'bo', label='Current Position')

        self.ax.set_xlim(self.minx, self.maxx)
        self.ax.set_ylim(self.miny, self.maxy)
        self.ax.set_title("2D Path Tracking on OSM Map (Offline)")
        self.ax.set_xlabel("Longitude")
        self.ax.set_ylabel("Latitude")
        self.ax.legend()

    def simulate_move(self):
        delta = np.random.uniform(-0.0001, 0.0001, size=2)
        self.current_pos += delta
        self.path.append(self.current_pos.copy())

    def update(self, frame):
        self.simulate_move()
        path_array = np.array(self.path)
        self.line.set_data(path_array[:, 0], path_array[:, 1])
        self.dot.set_data(self.current_pos[0], self.current_pos[1])
        return self.line, self.dot

    def start(self):
        ani = animation.FuncAnimation(self.fig, self.update, interval=500)
        plt.show()
