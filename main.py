#this is the main program of lab5
import random
def grade12(n):
    correct=0
    mistake=0
    i=0
    while(i<n):
        a=random.randint(1,100)
        b=random.randint(1,100)
        progress = random.randint(0, 1)  #0:+,1:-
        if(progress==0):
            cor_ans=a+b
            answer=input("{}+{}=".format(a,b))
            if (int(answer) == cor_ans):
                print("Correct!")
                correct += 1
            else:
                print("Wrong!")
                mistake += 1
            i+=1
        else:
            while(a<b):
                b=random.randint(1,100)
            cor_ans=a-b
            answer=input("{}-{}=".format(a,b))
            if (int(answer) == cor_ans):
                print("Correct!")
                correct += 1
            else:
                print("Wrong!")
                mistake += 1
            i+=1

    score=(correct/n)*100
    print("end! This time you have finished {} questions, your score is {}".format(n, score))
def highGrade(num):
    result = []
    counter_for_wrong = []
    counter_for_right = []
    for i in range(0, num):
        progress = random.randint(0, 4)  # 随机生成过程 ['+', '-', '*', '/']  0: +; 1: -; 2: *; 3: /
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
def middleGrade(num):
    singleScore=0.00
    count=0
    list1=['+','-','*','/']
    list2=[]
    score = 0
    singleScore=100/num
    for i in range(num):
        a = random.randint(0,100)
        b = random.randint(0,100)
        c = random.randint(0,3)
        print(a,list1[c],b,' = ?')
        result=input("Input the result(Keep two decimal places in division） = ")
        if c==0: #addition
            #print(result, a + b)
            if result==str(a+b):
                score=score+singleScore
                list2.append(1)
            else:
                list2.append(0)
        elif c==1: #subtraction
            #print(result, a - b)
            if result==str(a-b):
                score=score+singleScore
                list2.append(1)
            else:
                list2.append(0)
        elif c==2: #multiplication
            #print(result, a * b)
            if result==str(a*b):
                score=score+singleScore
                list2.append(1)
            else:
                list2.append(0)
        elif c==3: #division
            #print(result, a / b)
            if result==str(round((a/b),2)):
                score=score+singleScore
                list2.append(1)
            else:
                list2.append(0)
    count=list2.count(0) #check the number of wrong question
    if count==0: #all the question is right
        print("End! All right, your score is 100.")
    else: #have wrong question
        print("End! Wrong question is ", end=" ")
        for j in range(num):
            if list2[j]==0: #calculate the question number of wrong question
                print(j+1, end=" ")
        print(", your score is ", 100-count*singleScore)
garde = int(input('Please enter your grade?'))
num = int(input('Please enter the number of questions?'))
if (garde<=2):
    grade12(num)
elif(2<garde<=4):
    middleGrade(num)
elif(4<garde<=6):
    highGrade(num)