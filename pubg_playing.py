#%%
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as numpy
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
#%%
train=pd.read_csv('train_V2.csv')
#%%
train.info()
#%%
#train.head()
#%% [markdown]
# # The killers
train.head(5)
print("The average person kills {:.4f} players, 99% of people have {} kills or less, while the most kills ever recorded is {}.".format(train['kills'].mean(),train['kills'].quantile(0.99), train['kills'].max()))
#%% [markdown]
# ## Let's plot the Kill Counts
data=train.copy()
data.loc[data['kills']>data['kills'].quantile(0.99)]='10+'
plt.figure(figsize=(15,10))
sns.countplot(data['kills'].astype('str').sort_values())
plt.title("Kill Count",fontsize=15)
plt.show()
#%% [markdown]
# ## Most people were not able to make a single kill. Must they made the damage?

data=train.copy()
data=data[data['kills']==0]
plt.figure(figsize=(15,10))
plt.title("Damage Dealt by 0 killers",fontsize=15)
sns.distplot(data['damageDealt'])
plt.show()

#%% [markdown]
# ## Well most of them don't investigate the exceptions

sns.jointplot(x="winPlacePerc",y="kills",data=train,height=10,color='r')
plt.show()

#%% [markdown]
# # The runners 
print("The average person walks for {:.1f}m, 99% of people have walked {}m or less, while the marathoner champion walked for {}m.".format(train['walkDistance'].mean(), train['walkDistance'].quantile(0.99), train['walkDistance'].max()))
data=data[data['walkDistance']<train['walkDistance'].quantile(0.99)]
plt.figure(figsize=(15,10))
plt.title("Walking Distance Distribution",fontsize=15)
sns.distplot(data['walkDistance'])
plt.show()

#%% [markdown]
# # The Drivers
print("The average person drives for {:.1f}m, 99% of people have drived {}m or less, while the formula 1 champion drived for {}m.".format(train['rideDistance'].mean(), train['rideDistance'].quantile(0.99), train['rideDistance'].max()))

data=data[data['rideDistance']<train['rideDistance'].quantile(0.9)]
plt.figure(figsize=(15,10))
plt.title("Ride Distance Distribution",fontsize=15)
sns.distplot(data['rideDistance'])
plt.show()
#%% [markdown]
# ## Making the world the better place to live in as it will be going to prove to the entire battalion is cl
