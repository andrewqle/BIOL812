#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: andrewle
"""
import csv
import pandas as pd
traitdata=pd.read_csv("traits.ind 1.csv")
openfile=csv.reader(traitdata)
print(traitdata)

#To create a dataframe & subset
import pandas as pd
traitdataset=pd.DataFrame(traitdata)
traitdataset
traitdataset1=traitdataset.loc[0:318,'sp':'leg.length'] #Subset the dataframe
traitdataset2=traitdataset1
traitdataset2[['head.width','pronotum.width','mandible.length','scape.length','eye.width','leg.length']]=traitdataset2[['head.width','pronotum.width','mandible.length','scape.length','eye.width','leg.length']].div(traitdataset2['weber.length'].values,axis=0)#Divide columns by Weber Length
traitdataset3 = traitdataset2[['sp','head.width','pronotum.width','mandible.length','scape.length','eye.width','leg.length']]#Subset without Weber Length
traitdataset3

#Remove NA from rows
traitdataset4 = traitdataset3.dropna()
traitdataset4

#PCA
#Normalize data
from sklearn.preprocessing import StandardScaler
x=traitdataset4.loc[:,'head.width':'leg.length']
x=StandardScaler().fit_transform(x)

#Make components
from sklearn.decomposition import PCA
pca_trait = PCA(n_components=2)
principalComponents_traits = pca_trait.fit_transform(x)

#Turn components into a table
principal_trait_Df = pd.DataFrame(data= principalComponents_traits, columns = ['principal component 1','principal component 2'])
principal_trait_Df

#To see how much variance each principal component holds
print('Explained variation per principal component: {}'.format(pca_trait.explained_variance_ratio_))
#Explained variation per principal component: [0.52819108 0.23807306]

#Concatenating Dataframe with Species
finaltraitDf = pd.concat([principal_trait_Df,traitdataset4[['sp']]],axis=1)
finaltraitDf
finaltraitDf1 = finaltraitDf.dropna()
finaltraitDf1


from matplotlib import pyplot as plt
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1 (52.8%)', fontsize = 15)
ax.set_ylabel('Principal Component 2 (23.8%', fontsize = 15)
ax.set_title('2-Component PCA', fontsize = 20)
sps = ['agra', 'bobs', 'care']
colors = ['r','b','g']
for sp, color in zip(sps,colors):
    indicesToKeep = finaltraitDf1['sp'] == sp
    ax.scatter(finaltraitDf1.loc[indicesToKeep, 'principal component 1']
               , finaltraitDf1.loc[indicesToKeep, 'principal component 2']
               , c=color
               , s = 50)
ax.legend(sps)
ax.grid()





#colors = ['aliceblue','aqua','aquamarine1','aquamarine2','aquamarine3','aquamarine4','azure1','azure2','azure3','azure4','cadetblue','cadetblue1','cadetblue2','cadetblue3','cadetblue4','coral','coral1','coral2','coral3','coral4','cyan2','cyan3','cyan4','dodgerblue1']
#Species not used ['cfer','cnic','cobs','cpar','csp1','csp2','cvar','cvit','dsib','esha','mchi','mflo','mpsw','ntay','pdiv','pfer','plon','pnod','ppar','semm','sinv'

#CHECKS:
#Checks shape of Dataframe
traitdataset1.shape

#Check the column names
list(finaltraitDf1.sp)

#color 10, then repeats


