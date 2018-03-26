# Written by Hanxiong Wang on 10/1/2016
# This code is used to test the program by each eligible user, main part is almost same as EvalutionTest.py
# Anyone wanna view the notes can go to file valutionTest.py
from BuildClass import *
from NodeClassFun import *
from PlotObjGraph import *
from FormRecList import *
import pickle
import copy
import time

data_user = pickle.load(open("data_user_PA.dat",'rb'))
data_review = pickle.load(open("data_review_PA.dat",'rb'))
data_business = pickle.load(open("data_business_PA.dat",'rb'))

for num_user in range(len(data_user)):
    prefer_set = set()
    dislike_set = set()
    Rec_set = set()
    Top10_list = []

    Temp = NodeA()
    Temp.BuildNodeA(data_user[num_user])
    Temp.FindReview_listA(data_review)

    for item in Temp.review_list.keys():
        if Temp.review_list[item]>Temp.averstar:
            prefer_set.add(Findinfo(item, data_business)['name'])
        else:
            dislike_set.add(Findinfo(item, data_business)['name'])

    viewlen = len(prefer_set)
    if viewlen>5 and viewlen<30:
        print('The eligible user\'s number is ', num_user)
        answer = int(input('Do you wanna test this user? Yes:1, No:0, Quit: Other number\n'))
        if answer ==0:
            continue
        elif answer !=1:
            break
        
        start = time.clock()

        (Graph_list,Node_list,NumF,NumS)=PlotObjGraph(num_user,data_user, data_review,data_business)

        (Rec_Node_list, Rec_list,Graph_list,Node_list)=FindRecList(num_user,data_user,data_review,data_business,Graph_list, Node_list, NumF, NumS)

        print(Rec_list[0])
        secondlayernode = Node_list[Rec_list[0][0]].previsit
        print(Graph_list[secondlayernode][0])
        firstlayernode = Node_list[secondlayernode].previsit
        print(Graph_list[firstlayernode][0])
        zerolayernode = Node_list[firstlayernode].previsit
        print(Graph_list[zerolayernode][0],'\n')
        
        print('prefer list:')
        for k in prefer_set:
            print(k)
        print('\n')
        
        print('dislike list:')
        for k in dislike_set:
            print(k)
        print('\n')


        print('Recommend list for test use:')
        count = 0
        for item in Rec_Node_list:
            count+=1
            if count <=len(prefer_set):
                Rec_set.add(item[1])
            print(item[1])
        if len(prefer_set)!=0:
            accuracy = len(Rec_set&prefer_set)/len(prefer_set)
        if len(dislike_set)!=0:
            wrong = len(Rec_set&dislike_set)/len(dislike_set)
        
        print('\n')
        print('Accuracy is ',accuracy,'\n')
        print('Wrong rate is ',wrong,'\n')
        print('Top ten recommend list:')
        
        count = 0
        for item in Rec_Node_list:
            if item[1] in prefer_set or item[1] in dislike_set:
                continue
            else:
                if count == 10:
                    break
                else:
                   count += 1
                   Top10_list.append(item[1])
                   print(item[1])

        end = time.clock()
        print('\n')
        print('Spending time is ',end-start)

        answer = int(input('If continue asking? Yes:1, No:0\n'))
        if answer ==1:
           continue
        else:
            break
print("Done!")
