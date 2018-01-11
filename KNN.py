import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn import neighbors,preprocessing
data_table1=np.array(pd.read_csv('e:/Ali_o2o/dataset/table1.csv',header='infer',encoding='utf-8'))
table1_neg=pd.DataFrame([line for line in data_table1 if (line[-1]==-1 and line[2]!=-1)],columns=['User_id','Merchant_id','Coupon_id','Discount_rate','Distance','Date_received','Date'])
table1_normal=pd.DataFrame([line for line in data_table1 if (line[-1]!=-1 and line[2]==-1)])
table1_pos=pd.DataFrame([line for line in data_table1 if (line[-1]!=-1 and line[2]!=-1)])


print(table1_neg[:20])

table1_neg.sort_values(by=['Merchant_id'],ascending=False)

print(table1_neg[:20])



