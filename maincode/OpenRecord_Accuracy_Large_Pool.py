# Written by Hanxiong Wang on 10/18/2016
# Evalution on the algorithm in the a larger pool
import pickle
Accur = pickle.load(open("Record_Accuracy_Large_Pool.dat",'rb'))
Wrong = pickle.load(open("Record_Wrong_Rate_Large_Pool.dat",'rb'))
print(sum(Accur)/len(Accur),'\n')
print(Accur)
print(sum(Wrong)/len(Wrong),'\n')
print(Wrong)
