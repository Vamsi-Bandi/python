import random
numberOfStreaks = 0
streak = 0
for experimentNumber in range(10000):
    toss = []
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            value = ['H']
            toss = toss + value
        else:
            value = ['T']
            toss = toss + value
    for index, item in enumerate(toss):
        if index == 0:
            pass
        elif toss[index] == toss[index - 1]:
            streak += 1
        else:
            streak = 0
        
        if streak == 6:
            numberOfStreaks += 1
print('chance of Streak : ' + str(numberOfStreaks/100) + '%')
