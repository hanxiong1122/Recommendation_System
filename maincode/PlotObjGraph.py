# Written by Hanxiong Wang on 10/18/2016
# This code is used to build a funtion to generate the objective graph and its edges by adjacent list

from BuildClass import *
from NodeClassFun import *
import copy

def PlotObjGraph(num_user,data_user,data_review,data_business,gamma =5,alpha= 1,beta =1,theta =0.5):
    numNode = 0 # used to record the number of node 
    ObjNode_list = []
    ObjGraph_list = [[]]
    # For zeroth layer: root node (input user )
    TempN = NodeA()
    TempN.BuildNodeA(data_user[num_user])
    TempN.FindReview_listA(data_review)
    ObjNode_list.append(copy.deepcopy(TempN))
    ObjGraph_list[0].append([numNode,-1])
    Zero_layer_set = set()
    Zero_layer_set.add(TempN.id)
    numNode += 1
    del TempN
###########################################################
# For the first layer: nodes to represent business shop
    First_layer_set= set()

    for k in ObjNode_list[0].review_list.keys():
        if k in First_layer_set:
            i = FindIndex(k,ObjNode_list)
            ObjGraph_list[0].append([i,-1])
            del i
        else:
            First_layer_set.add(k)
            business_info = Findinfo(k,data_business)
            TempN = NodeB()
            TempN.BuildNodeB(business_info)
            TempN.FindReview_listB(data_review)
           # print(TempN.name)
            ObjNode_list.append(copy.deepcopy(TempN))
            ObjGraph_list[0].append([numNode,-1])
            ObjGraph_list.append([[numNode,-1]])
            numNode +=1
            del TempN
    Num_First_layer = len(First_layer_set)
# Write the edge bw zeroth layer to the first layer
    for edge in ObjGraph_list[0]:
        if  edge[0] == ObjGraph_list[0][0][0]:
            continue
        else:
            person = ObjNode_list[ObjGraph_list[0][0][0]]
            bussShop = ObjNode_list[edge[0]]
            if person.averstar==0:
                edge[1] = gamma * person.review_list[bussShop.id]/0.5
            else:
                edge[1] = gamma * person.review_list[bussShop.id]/person.averstar
    print('Num_First_layer ',Num_First_layer,'\n')
###########################################################
# For the second layer: nodes to represent users
    Second_layer_set = set()

    for SE in range(1,Num_First_layer+1):
        for k in ObjNode_list[SE].review_list.keys():
            if k in Second_layer_set:
                i = FindIndex(k,ObjNode_list)
                ObjGraph_list[SE].append([i,-1])
                del i
            else:
                userinfo = Findinfo(k,data_user)
                TempN = NodeA()
                TempN.BuildNodeA(userinfo)
                TempN.FindReview_listA(data_review)  
                if TempN.review_count > 100 or (TempN.id == ObjNode_list[0].id):
                    del TempN
                    continue
                else:
                    Second_layer_set.add(k)
                    ObjNode_list.append(copy.deepcopy(TempN))
                    ObjGraph_list[SE].append([numNode,-1])
                    ObjGraph_list.append([[numNode,-1]])
                    numNode +=1                
                    del TempN          
    Num_Second_layer = len(Second_layer_set)           
# Write the edge bw first layer to the second layer
    for SE in range(1,Num_First_layer+1):
        for edge in ObjGraph_list[SE]:
            if edge[0] == ObjGraph_list[SE][0][0]:
                continue
            else:
                person = ObjNode_list[edge[0]]
                bussShop = ObjNode_list[SE]
                if person.averstar==0:
                    edge[1] = alpha*person.review_list[bussShop.id]/0.5
                else:
                    edge[1] = alpha*person.review_list[bussShop.id]/person.averstar
    print('Num_Second_layer ',Num_Second_layer,'\n')
################################################################
# For the third layer: nodes to represent final recommandation business shop
    Third_layer_set = set()

    for TE in range(Num_First_layer+1, Num_First_layer+Num_Second_layer+1):
        for k in ObjNode_list[TE].review_list.keys():
            if k in Third_layer_set:
                i = FindIndex(k,ObjNode_list)
                ObjGraph_list[TE].append([i,-1])
                del i
            else:
                Third_layer_set.add(k)
                bussinfo = Findinfo(k,data_business)
                TempN = NodeB()
                TempN.BuildNodeB(bussinfo)
                TempN.FindReview_listB(data_review)
                ObjNode_list.append(copy.deepcopy(TempN))
                ObjGraph_list[TE].append([numNode,-1])
                ObjGraph_list.append([[numNode,-1]])
                numNode +=1
                del TempN   
    Num_Third_layer = len(Third_layer_set)
# Write the edge bw the second layer to the third layer
    CateDis_First_layer = CateDisCal(ObjNode_list[0],data_business)
    for TE in range(Num_First_layer+1, Num_First_layer+Num_Second_layer+1):
        for edge in ObjGraph_list[TE]:
            if edge[0] == ObjGraph_list[TE][0][0]:
                continue
            else:
                person = ObjNode_list[TE]
                #print(type(person),'\n')
                bussShop = ObjNode_list[edge[0]]
                #print(type(ObjNode_list[edge[0]]),'\n')
                if person.averstar == 0:
                    edge[1] = alpha*person.review_list[bussShop.id]/0.5
                else:
                    edge[1] = alpha*person.review_list[bussShop.id]/person.averstar
                modedge1 = ModCateEdge(bussShop,CateDis_First_layer)
                modedge2 = ModAttrEdge(bussShop,ObjNode_list[1:Num_First_layer+1])
                if modedge1 ==0:
                    edge[1] = -100 + edge[1]
                else:
                    edge[1] = edge[1] + beta*modedge1 + beta*theta*modedge2
    print('Num_Third_layer ',Num_Third_layer,'\n')
    return ObjGraph_list,ObjNode_list,Num_First_layer,Num_Second_layer





