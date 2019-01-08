import matplotlib.pyplot as plt 

from random_walk import RandomWalk

def main():
    while True:

        rw = RandomWalk(50000)
        rw.fill_walk()
        
        # 设置窗口大小
        plt.figure(dpi=256, figsize=(100, 60))

        point_numbers = list(range(rw.num_points))
        
        plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
        
        # 隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break

if __name__ == '__main__':
    main()
