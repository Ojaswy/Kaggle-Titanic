# coding: utf-8
import pandas as pd
import os
import pylab as plt
#path to datasets, if not in same directory
#os.chdir("Desktop/Titanic")
df=pd.read_csv("train.csv")

females=df[df["Sex"]=="female"].groupby("Pclass")["Survived"].agg(sum)

fig=plt.figure()
ax=fig.add_subplot(111)
rec=ax.bar(females.index.values.tolist(),females,width=0.5,color="yellow")
xmarks=females.index.values.tolist()
ax.set_ylabel("Number of females")
ax.set_xlabel("class")
ax.set_title("Number of females survived VS class")
ax.set_xticks(xmarks)
xtickmarks=ax.set_xticklabels(xmarks)
plt.setp(xtickmarks,fontsize=20)
plt.show()


