import csv
from six.moves import cPickle as pickle
import numpy as np


def main(path_pickle,path_csv):
    ''' data = {
        "status" = 12,
        "user_firstName = 12,
        "id" = 12,
        "username" = 122
        }'''

    x = []
    with open(path_pickle,'rb') as pickle_file:
        x = pickle.load(pickle_file)
        with open(path_csv,'w') as csv_file:
            writer = csv.writer(csv_file)
            for k, v in x.items():
                i=0
                for m in v:
                    i=i+1
                    a=bytes(str(m.user.id),encoding='utf8')
                    b=bytes(str(m.user.first_name),encoding='utf8')
                    csv_file.write ("{}, {},\n".format (a, i))
                    #print("{}, {}".format(a, i ))
                    #csv_file.write ("{}, {},\n".format (k, a))
                    
        
        
        #print(f)

    '''with open(path_csv,'w') as f:
        writer = csv.writer(f)
        for line in x:
            #writer.writerows(line)
            print(lne)'''
main("members.pkl","file.csv")
