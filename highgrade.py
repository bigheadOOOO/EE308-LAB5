import random


garde = int(input('Please enter your grade?'))
num = int(input('Please enter the number of questions?'))


def highGrade(num):
    result = []
    counter_for_wrong = []
    counter_for_right = []
    for i in range(0, num):
        progress = random.randint(0, 4)
        a = round(random.uniform(0, 100), 2)
        b = round(random.uniform(0, 100), 2)

        # print output question
        if (progress == 0):
            print('Output:', a, '+', b, '=?')
            result.append(a+b)
        elif (progress == 1):
            print('Output:', a, '-', b, '=?')
            result.append(a - b)
        elif (progress == 2):
            print('Output:', a, '*', b, '=?')
            result.append(a * b)
        else:
            print('Output:', a, '/', b, '=?')
            result.append(a / b)

        c = input('Input:')

        if (c == result[i]):
            counter_for_right.append(i)
        else:
            counter_for_wrong.append(i)

    if counter_for_wrong != 0:
        print('end! Wrong question, your score is ', 100*len(counter_for_right)/num, ', which is ')
        for j in counter_for_wrong:
            print(j+1)
    else:
        print('end! All right, that\'s great! Your score is 100.')


highGrade(num, progress)
