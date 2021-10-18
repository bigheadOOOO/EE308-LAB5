import random
def grade12(n):
    while(i<n):
        correct=0
         mistake=0
        i=0
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
