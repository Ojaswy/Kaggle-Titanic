import pandas as pd
import numpy as np
import os
import pylab as plt
#os.chdir("mention path here")
df=pd.read_csv("train.csv")
survivors=df.groupby("Pclass")["Survived"].aggregate(sum)
fig=plt.figure()
ax=fig.add_subplot(111)
rect=ax.bar(survivors.index.values.tolist(),survivors,color="pink",width=0.3)
xmarks = survivors.index.values.tolist()
ax.set_ylabel("Number of survivors")
ax.set_xlabel("Class type")
ax.set_title("Total number of survivors based on class")
ax.set_xticks(xmarks)
xtickmarks=ax.set_xticklabels(xmarks)
plt.setp(xtickmarks,fontsize=20)
plt.show()

