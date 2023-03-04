#!/usr/bin/env python

#author:Gaoyang Luo, lgyjsnjhit@gmail.com
#requirements: numpy, scipy, scikit-learn, matplotlib, projection-pursuit
#usage: python ppr.py -i <input> -o <output> -l <left range> -r <right range> -t <iterate_times>

#pip install numpy, scipy, scikit-learn, and matplotlib
#pip install projection-pursuit

import os,sys,argparse
import random
import numpy as np
import pandas as pd
from skpp import ProjectionPursuitRegressor

#Parse arguments
parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', required=True,
    dest='input', 
    help='Input files for this program (relative abundance of ARGs tsv file)')
parser.add_argument('-o', '--output', required=True,
    dest='output', 
    help='Output files for this program (relative abundance of ARGs tsv file)')
parser.add_argument('-l', '--lrange', required=True,
    dest='lrange', 
    help='start range')
parser.add_argument('-r', '--rrange', required=True,
    dest='rrange', 
    help='End range')
parser.add_argument('-t', '--times', required=True,
    dest='times', 
    help='How many times you want to iterate')


args=parser.parse_args()

#set dest
input=args.input
output=args.output
lrange=args.lrange
rrange=args.rrange
times=args.times

    
import os,sys
import random
import numpy as np
import pandas as pd
from skpp import ProjectionPursuitRegressor

class ppr_cal(object):
    def __init__(self,lrange,rrange,times,input):
        self.lrange=float(lrange)
        self.rrange=float(rrange)
        self.times=int(times)
        self.input=input
    

    def randFloatGenerate(self):
        random.seed (999)
        #generate n times numbers
        # result2=result.to_numpy()
        simu_x=np.zeros(shape=(self.times,1))
        count=0
        for i in range(0,self.times):
            result = [np.random.uniform(self.lrange,self.rrange)] 
            result=np.array(result,dtype=np.float64)
            simu_x[count]=result
            count+=1
        return simu_x

    def main(self):
        #load data
        df_raw_table=pd.read_csv(self.input,sep="\t",header=0,index_col=0) #"dsr_crossVali/biodMP.txt"
        value_y=[i for i in df_raw_table.iloc[:,-1]]
        df_raw_table_x=df_raw_table.iloc[:,0:int(len(df_raw_table.columns))-1]
        value_x_array=df_raw_table_x.to_numpy()

        #build model
        estimator = ProjectionPursuitRegressor()
        estimator.fit(value_x_array,value_y)

        #predict
        simu_x=self.randFloatGenerate()
        predict=estimator.predict(simu_x)

        predic_df=pd.DataFrame(predict)

        print("The simulated projection values are:\n{}".format(predic_df[0]))
        
        return predic_df

if __name__ == "__main__":
    output=output
    a=ppr_cal(lrange=lrange,rrange=rrange,times=times,input=input) #"dsr_crossVali/biodMP.txt"
    a.main().to_csv(output,index=None,header=None) #"dsr_crossVali/simu_biodMP_projection_values.txt"
    

