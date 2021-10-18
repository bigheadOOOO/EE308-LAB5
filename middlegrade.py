
import random


def middleGrade(num):
    singleScore=0.00
    count=0
    list1=['+','-','*','/'];
    list2=[];
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
            if result==int(a+b):
                score=score+singleScore
                list2.append(1)
            else:
                list2.append(0)
        elif c==1: #subtraction
            #print(result, a - b)
            if result==int(a-b):
                score=score+singleScore
                list2.append(1)
            else:
                list2.append(0)
        elif c==2: #multiplication
            #print(result, a * b)
            if result==int(a*b):
                score=score+singleScore
                list2.append(1)
            else:
                list2.append(0)
        elif c==3: #division
            #print(result, a / b)
            if result==int(round((a/b),2)):
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
middleGrade(4)
