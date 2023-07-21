# 三门问题代码模拟

"""三门问题：

在一个电视节目中，参赛者需要在三扇关闭的门之间选择一扇门，其中一扇门后面有大奖，另外两扇门后面什么也没有。
在参赛者选择一扇门之后，主持人可以打开其中一扇没有大奖的门。这时候参赛者可以保留当前选择，或者更换为另外一扇门。
如果参赛者做出了换门选择，那么获奖概率会如何变化？

当参赛者第一次选择的时候，获奖概率是1/3，这个很容易理解。注意题干中，主持人会故意打开一扇没有大奖的门，
这相当于主持人帮参赛者排除了一个错误答案。所以如果这时候参赛者选择换门，那么不中奖的情况等同于一开始就
选择了正确的门，即1/3，那么中奖的概率自然就是2/3了。
"""


def three_door_question(times: int):
    import random

    win_if_not_swap = 0
    win_if_swap = 0
    for _ in range(times):
        # 设3是大奖
        doors = [1, 2, 3]
        random.shuffle(doors)
        first_choice = doors.pop()
        # first_choice = random.choice(doors)
        # doors.remove(first_choice)
        # 如果大奖在剩下的里面，由主持人排除一个错误答案，剩下大奖
        if 3 in doors:
            doors = [3]
        # 如果大奖已经被选了，主持人随机排除一个答案，剩下一个错误答案
        else:
            doors = [random.choice((1, 2))]
            # doors.remove(random.choice((1, 2)))
        if first_choice == 3:
            win_if_not_swap = win_if_not_swap + 1
        if doors[0] == 3:
            win_if_swap = win_if_swap + 1

    print(
        f"Total times:{times:10d}, p if not swapping is {win_if_not_swap / times :10f}, p if swapping is {win_if_swap / times:10f}"
    )


if __name__ == "__main__":
    three_door_question(10000)
    three_door_question(100000)
    three_door_question(1000000)
