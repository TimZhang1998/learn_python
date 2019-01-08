from random import randint

class Die():
    """表示一个骰子类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """模拟投掷骰子，并显示结果"""
        return randint(1, self.num_sides)