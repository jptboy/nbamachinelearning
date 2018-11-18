#!/home/user/anaconda3/bin/python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sklearn as sk



# In[2]:


ogdata = pd.read_csv('nbaNew.csv')


# In[3]:


ogdata.head(10)


# In[4]:


data2000plus = ogdata[ogdata["SeasonStart"] >= 2000]
realplayers = data2000plus[data2000plus["MP"] >= 1000]


# In[5]:


realplayers.head(10)


# In[6]:


realplayers.keys()


# In[7]:



neededData =  {
    "Name": realplayers["PlayerName"],
    "Points": realplayers["PTS"]/(realplayers["MP"]*1000),
    "Assists": realplayers["AST"]/(realplayers["MP"]*1000),
    "OffensiveRebounds": realplayers["ORB"]/(realplayers["MP"]*1000),
    "Position": realplayers["Pos"],
    "Season": realplayers["SeasonStart"]
}


# In[8]:


neededDf = pd.DataFrame(neededData)


# In[9]:


neededDf.head(10)


# In[10]:


#neededDf.to_csv('cleantData.csv')


# In[11]:


df = neededDf


# In[12]:


PFdf = neededDf[neededDf["Position"]=="PF"]


# In[13]:


PFdf.head(10)


# In[14]:


import sklearn.preprocessing as prepro


# In[15]:


def normalize(arr):
    maxv = max(arr)
    minv = min(arr)
    diff = maxv-minv
    for index,num in enumerate(arr):
        arr[index] = (num - minv)/(diff)
    return arr


# In[16]:


normalizedp = normalize(np.array(PFdf["Points"]))
normalizedr = normalize(np.array(PFdf["OffensiveRebounds"]))
normalizeda = normalize(np.array(PFdf["Assists"]))


# In[17]:


PFdf = PFdf.assign(Points = normalizedp)
PFdf = PFdf.assign(OffensiveRebounds = normalizedr)
PFdf = PFdf.assign(Assists = normalizeda)


# In[18]:


PFdf.head(10)


# In[19]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[22]:


X = [x for x in PFdf["Points"]]
Y = [x for x in PFdf["OffensiveRebounds"]]
Z = [x for x in PFdf["Assists"]]


fig = plt.figure()
ax = Axes3D(fig)



ax.scatter(X, Y, Z)
ax.set_xlabel("Points")
ax.set_ylabel("Offensive Rebounds")
ax.set_zlabel("Assists")
ax.set_title("Stats of PF's after 2000 that played\n real minutes (values normalized between 0 and 1)")

for X,Y,Z,name in zip(X,Y,Z,PFdf["Name"]):
    ax.text(X,Y,Z,name)

plt.show()


# In[ ]:




