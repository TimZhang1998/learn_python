from random import choice

class RandomWalk():
    """生成随机漫步数据"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self._num_points = num_points

        self._x_values = [0]
        self._y_values = [0]

    @property
    def x_values(self):
        return self._x_values
    
    @property
    def y_values(self):
        return self._y_values

    @property
    def num_points(self):
        return self._num_points

    def get_step(self):

        # 决定前进的方向以及该方向前进的距离
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        while len(self._x_values) < self._num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self._x_values[-1] + x_step
            next_y = self._y_values[-1] + y_step

            self._x_values.append(next_x)
            self._y_values.append(next_y)
