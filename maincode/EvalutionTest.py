# Written by Hanxiong Wang on 10/1/2016

from BuildClass import *
from NodeClassFun import *
from PlotObjGraph import *
from FormRecList import *
import pickle
import copy
import time

# import three datasets
data_user = pickle.load(open("data_user_PA.dat",'rb'))
data_review = pickle.load(open("data_review_PA.dat",'rb'))
data_business = pickle.load(open("data_business_PA.dat",'rb'))

flag = 0
Accur_set = [] # a set for record the corrected prediction rate in the pool
Wrong_set = [] # a set for record the uncorrected prediction rate in the pool
for num_user in range(len(data_user)):
    prefer_set = set()
    dislike_set = set()
    Rec_set = set()
    Top10_list = []
    # build root node for the objective graph
    Temp = NodeA() 
    Temp.BuildNodeA(data_user[num_user])
    Temp.FindReview_listA(data_review)
    # find the prefer set and the dislike set for the root user
    for item in Temp.review_list.keys():
        if Temp.review_list[item]>Temp.averstar:
            prefer_set.add(Findinfo(item, data_business)['name'])
        else:
            dislike_set.add(Findinfo(item, data_business)['name'])

    viewlen = len(prefer_set) # criterion for a eligible user to provide the recommendation list
    if viewlen>5 and viewlen<30:
        flag += 1
        print('flag is ', flag)
        print('The eligible user\'s number is ', num_user)
        
        start = time.clock() # record the start point for one loop
        # build the objective graph
        (Graph_list,Node_list,NumF,NumS)=PlotObjGraph(num_user,data_user, data_review,data_business)
        # build the recommendation list
        (Rec_Node_list, Rec_list,Graph_list,Node_list)=FindRecList(num_user,data_user,data_review,data_business,Graph_list, Node_list, NumF, NumS)
        # give the detail longest path from the root node to the node lies in the third layer
        print(Rec_list[0])
        secondlayernode = Node_list[Rec_list[0][0]].previsit
        print(Graph_list[secondlayernode][0])
        firstlayernode = Node_list[secondlayernode].previsit
        print(Graph_list[firstlayernode][0])
        zerolayernode = Node_list[firstlayernode].previsit
        print(Graph_list[zerolayernode][0],'\n')
        
        # print the  preferred list
        print('prefer list:')
        for k in prefer_set:
            print(k)
        print('\n')
        
        # print the  dislike list
        print('dislike list:')
        for k in dislike_set:
            print(k)
        print('\n')

        # print the recommendation list for the test use and its related evalution
        print('Recommendation list for test use:')
        count = 0
        for item in Rec_Node_list:
            count+=1
            if count <=len(prefer_set): # Define the size of the pool
                Rec_set.add(item[1])
            print(item[1])

        if len(prefer_set)!=0:
            accuracy = len(Rec_set&prefer_set)/len(prefer_set)
            Accur_set.append(accuracy)
            print('\n')
            print('Accuracy is ',accuracy,'\n')
            aver_accur = sum(Accur_set)/len(Accur_set)
            print('Average accuracy is ',aver_accur,'\n')

        
        if len(dislike_set)!=0:
            wrong = len(Rec_set&dislike_set)/len(dislike_set)
            Wrong_set.append(wrong)
            print('Wrong rate is ',wrong,'\n')
            aver_wrong = sum(Wrong_set)/len(Wrong_set)
            print('Average Wrong rate is ',aver_wrong,'\n')


        # print the top ten recommendation list as the final result
        print('Top ten recommendation list:')
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
                   
        # recond the end time for this loop and print the time
        end = time.clock()
        print(end-start)

        # save the evalution
        f = open("Record_Accuracy.dat","wb")
        #f = open("Record_Accuracy_Large_Pool.dat","wb")
        pickle.dump(Accur_set,f,True)
        f.close()
        f = open("Record_Wrong_Rate.dat","wb")
        #f = open("Record_Accuracy_Large_Pool.dat","wb")
        pickle.dump(Wrong_set,f,True)
        f.close()
        if flag < 100:
           continue
        else:
            break

print("Done!")
