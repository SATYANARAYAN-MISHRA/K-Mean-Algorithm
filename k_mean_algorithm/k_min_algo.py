import sys
import math 
import random


def checkUniqunessOfList(centroid_index):
    
    n = len(centroid_index)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if centroid_index[i] == centroid_index[j]:
                return False
    return True
        
def equatingCentroid(old_centroid,new_centroid):

    n = len(old_centroid)
    for i in range(0,n):
        a = old_centroid[i][0]
        b = old_centroid[i][1]
        c = new_centroid[i][0]
        d = new_centroid[i][1]
        if(abs(a-c) > 0.001 or abs(b-d) > 0.001):
            return False
    return True
        
    
def distanceCalculation(x_1,y_1,x_2,y_2):
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)

def findCentroid(temp_list):
    centroid_x = 0
    centroid_y = 0
    
    n = len(temp_list)


    for j in range(0,n):
        centroid_x = centroid_x + temp_list[j][0]
        centroid_y = centroid_y + temp_list[j][1]
    centroid_x = centroid_x /n 
    centroid_y = centroid_y/n
    centroid = (centroid_x,centroid_y)
    return centroid




def initialClusterPartion(input_data,k_value):
    n = len(input_data)
    centroid_index = []
    for i in range(0,k_value):
        centroid_index.append(random.randint(0, (n-1)))
    if checkUniqunessOfList(centroid_index) == True:
        clustered_centroid = []
        for i in centroid_index:
            a = input_data[i][0]
            b = input_data[i][1]
            
            clustered_centroid.append((a,b))
        return clustered_centroid
    if checkUniqunessOfList(centroid_index) == False:
        return initialClusterPartion(input_data,k_value)


def clusterReshaping(input_data,cluster_centroid_old,cluster_centroid_new,k_value):
#    print "old cluster_centroid is",cluster_centroid_old
#    print "\n"
#    print " new cluster_centroid is",cluster_centroid_new
#    print "\n"
     
    if equatingCentroid(cluster_centroid_old,cluster_centroid_new) == True:
       return cluster_centroid_new
       
    if equatingCentroid(cluster_centroid_old,cluster_centroid_new) == False:
        new_clustered_list = [[]]*k_value
        new_clustered_centroid = []
        tmp_list = []
        for i in input_data:
            distence_cal_list = []
            for j in cluster_centroid_new:

                d = distanceCalculation(i[0],i[1],j[0],j[1])
                distence_cal_list.append(d)

            indxx = distence_cal_list.index(min(distence_cal_list))
            
            new_clustered_list[indxx] = new_clustered_list[indxx] + [i]
        cnt = new_clustered_list.count([])
        for i in new_clustered_list:
                new_clustered_centroid.append(findCentroid(i))
 
        return clusterReshaping(input_data,cluster_centroid_new,new_clustered_centroid,k_value)
       
    

    
if __name__ =="__main__":
    k_value = int(sys.argv[1])
    input_path = sys.argv[2]

    fp = open(input_path,"r")
    input_data = fp.readlines()
    input_data = map(lambda x : (x.strip('\n')).split(' '), input_data)
    input_data = map(lambda l : [float(l[0])] + [float(l[1])] , input_data)
    fp.close()
    old_cls = [(0,0)]*k_value
    cls = initialClusterPartion(input_data,k_value)
    

    final_cluster_centroid = clusterReshaping(input_data,old_cls,cls,k_value)
    print "final cluster centroid is",final_cluster_centroid

