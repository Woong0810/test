from data_unsorted import numbers
# from data_unsorted_a_lot import numbers

from random import randint, seed
from pyvisalgo import BubbleSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
def main():
    print('before:', array)
    count = len(array)
    for end in range(count - 1, 0, -1):     # 아 end 값을 하나씩 줄이기 위해서
        for i in range(end):
            vis.compare(i, i + 1)
            if array[i] > array[i + 1]:
                vis.swap(i, i + 1)
                array[i], array[i + 1] = array[i + 1], array[i]
    print('after :', array)

if __name__ == '__main__':
    seed('Hello')  # 'Hello' 를 seed 로 고정하여 randint 가 항상 같은 결과가 나오게 한다
    vis = Visualizer('Bubble Sort')
    while True:
        count = randint(10, 30)
        array = numbers[:count]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()

        # R key 를 누르면 다음 case 가 실행된다
        again = vis.end()
        if not again: break