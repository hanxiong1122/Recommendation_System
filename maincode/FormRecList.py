# Written by Hanxiong Wang on 10/1/2016
# This part of code is used to generate the recomendation list by calculating the longest
# path for each nodes in the third layer

from BuildClass import *
from NodeClassFun import *
import math

def AuxFun(node):
    return node[1]

def FindRecList(num_user,data_user,data_review,data_business,Graph_list, Node_list, NumF, NumS):
    prefer_set = set()
    Temp = NodeA()
    Temp.BuildNodeA(data_user[num_user])
    Temp.FindReview_listA(data_review)
    Graph_list[0][0][1] = 0
    Rec_list=[]
    Rec_Node_list=[]
    # A dynamic programming to calculate the longest path from the root to each nodes in the third layers
    for i in range(len(Graph_list)):
        for j in range(len(Graph_list[i])):
            if j == 0:
                continue
            else:
                Tnode = Graph_list[i][j][0]
                if Graph_list[Tnode][0][1] <Graph_list[i][0][1]+Graph_list[i][j][1]:
                       Graph_list[Tnode][0][1] = Graph_list[i][0][1]+Graph_list[i][j][1]
                       Node_list[Tnode].previsit = i
    for i in range(NumF+NumS+1,len(Graph_list)):
            Rec_list.append(Graph_list[i][0])
    # Sort the node list by length of path           
    Rec_list.sort(key = AuxFun,reverse = True)
    # Give a proper length of node list. Of course we can use the complete list, but that is not necessary
    Rec_size = min(2*len(Temp.review_list),len(Rec_list))
    # Generate the recommendation list, only keep the business id and its name for each node
    for i in range(Rec_size):
        Tnode = Rec_list[i][0]
        Rec_Node_list.append([Node_list[Tnode].id,Node_list[Tnode].name])
    return Rec_Node_list, Rec_list, Graph_list, Node_list
