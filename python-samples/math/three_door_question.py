# 三门问题代码模拟


def three_door_question(times: int):
    import random
    result_if_not_change = 0
    result_if_change = 0
    for i in range(0, times):
        doors = [1, 2, 3]  # 3是大奖
        random.shuffle(doors)
        first_choice = doors[random.randint(0, 2)]
        doors.remove(first_choice)
        # 如果大奖在剩下的里面，由主持人排除一个错误答案，剩下大奖
        if 3 in doors:
            doors = [3]
        # 如果大奖已经被选了，主持人随机排除剩下一个错误答案
        else:
            doors.remove(random.choice((1, 2)))
        if first_choice == 3:
            result_if_not_change = result_if_not_change + 1
        if doors[0] == 3:
            result_if_change = result_if_change + 1

    print(
        f'Total times:{times}, prob of not change is {result_if_not_change / times}, prob of change is {result_if_change / times}')


three_door_question(10000)
three_door_question(100000)
three_door_question(1000000)
