import pandas as pd
import numpy as np
import sys
class topsis_class:
    def __init__(self,dataset,weights, impacts,out):
        self.dataset2=pd.read_csv(dataset)
        if(self.dataset2.shape[1]<=2):
            raise Exception('Input data must have columns greater than equal to 3')
        # print(self.dataset2.dtypes[1],type(self.dataset2.dtypes))
        if all([i!='object' for i in list(self.dataset2.dtypes.iloc[1:])])==False:
            raise Exception('All Columns except first must be numeric')
        if len(weights) != len(impacts) or len(weights) != (self.dataset2.shape[1]-1) or (self.dataset2.shape[1]-1) != len(impacts)  : 
            raise Exception('Number of Weights, Impacts or Numerical Columns(excluding the first column) is not equal')
        if not all([(type(i)==int or type(i)==float) for i in weights]):
            raise Exception('All weights must be numeric values separated with commas')
        if not all([(i=="+" or i =="-") for i in impacts]):
            raise Exception('Impacts must be either + or - and separated with commas')
        self.dataset=self.dataset2.drop(columns=self.dataset2.columns[0],axis=1)
        self.weights=np.array(weights)
        self.impacts=impacts
        self.v_pos=[]
        self.v_neg=[]
        self.s_neg=[]
        self.s_pos=[]
        self.score=[]
        self.out=out
    
    def calculate(self):
        for i in range(self.dataset.shape[1]):
            x=pow(np.sum(np.square(self.dataset.iloc[:,i])),0.5)
            self.dataset.iloc[:,i]=np.divide(self.dataset.iloc[:,i],x)
        for i in range(self.dataset.shape[0]):
            for j in range(self.dataset.shape[1]):
                self.dataset.iloc[i,j]=self.dataset.iloc[i,j] * self.weights[j]
        for i in range(self.dataset.shape[1]):
            max=-1*float("inf")
            min=float("inf")
            for j in self.dataset.iloc[:,i]:
                if max<j:
                    max=j
                if min>j:
                    min=j
            if(self.impacts[i]=="+"):
                self.v_pos.append(max)
                self.v_neg.append(min)
            if(self.impacts[i]=="-"):
                self.v_pos.append(min)
                self.v_neg.append(max)
        for i in range(self.dataset.shape[0]):
            count=self.dataset.shape[1]
            val=0
            for j in range(count):
                val+=(self.dataset.iloc[i,j]-self.v_pos[j])**2
            self.s_pos.append(val**0.5)
            val=0
            for j in range(count):
                val+=(self.dataset.iloc[i,j]-self.v_neg[j])**2
            self.s_neg.append(val**0.5)
        for i in range(len(self.s_pos)):
            self.score.append((self.s_neg[i])/(self.s_neg[i]+self.s_pos[i]))
        self.dataset2["Topsis Score"]=self.score    
        self.dataset2["Rank"]=(np.argsort(np.flip(np.argsort(self.score)))+1)
        self.dataset2.to_csv(self.out,index=False)

    def get_score(self):
        return self.score
    def display(self):
        print(self.dataset2)

def topsis():
    try:
        if(len(sys.argv)!=5):
            raise Exception('Please input correct number of parameters')
        q=topsis_class(sys.argv[1] , [eval(i) for i in sys.argv[2].split(",")] ,sys.argv[3].split(","),sys.argv[4])
        q.calculate()
    except NameError:
        print('Exception : Weight must be a numeric Value, integer or float')    
    except FileNotFoundError:
        print('Exception : File Not Found Exception has occurred. Kindly ensure the file exists in the same folder or provide the compete path')
    except Exception as e:
        print('Exception : ', e)
topsis()        