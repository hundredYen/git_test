# -- coding:utf-8 --
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(8, 8), dpi=80)#创建第一个画板
plt.rcParams['font.sans-serif']=['SimHei']

ax1 = plt.subplot(2, 2, 1)
plt.axis([-1, 5, 46, 52])
plt.bar(['a'], [50.05], alpha=0.5, width=0.6, color='yellow', label='CAGNN-L')
plt.bar(['b'], [49.17], alpha=0.5, width=0.6, color='green', label='CAGNN-AVG')
plt.bar(['c'], [50.63], alpha=0.5, width=0.6, color='cyan', label='CAGNN-ATT')
plt.bar(['d'], [50.37], alpha=0.5, width=0.6, color='orange', label='CAGNN-L-ATT')
plt.bar(['e'], [51.08], alpha=0.5, width=0.6, color='blue', label='CAGNN')
plt.xticks([])
plt.legend(loc='upper left')
plt.ylabel('Precision@20', fontsize=12)
ax1.set_title("Diginetica2")

ax2 = plt.subplot(2, 2, 2)
plt.axis([-1, 5, 46, 58])
plt.bar(['a'], [51.08], alpha=0.5, width=0.6, color='yellow', label='CAGNN-L')
plt.bar(['b'], [49.83], alpha=0.5, width=0.6, color='green', label='CAGNN-AVG')
plt.bar(['c'], [50.50], alpha=0.5, width=0.6, color='cyan', label='CAGNN-ATT')
plt.bar(['d'], [51.37], alpha=0.5, width=0.6, color='orange', label='CAGNN-L-ATT')
plt.bar(['e'], [56.41], alpha=0.5, width=0.6, color='blue', label='CAGNN')
plt.xticks([])
plt.legend(loc='upper left')
plt.ylabel('Precision@20', fontsize=12)
ax2.set_title("The user behavior dataset")

ax3 = plt.subplot(2, 2, 3)
plt.axis([-1, 5, 15, 18])
plt.bar(['a'], [17.07], alpha=0.5, width=0.6, color='yellow', label='CAGNN-L')
plt.bar(['b'], [16.32], alpha=0.5, width=0.6, color='green', label='CAGNN-AVG')
plt.bar(['c'], [16.98], alpha=0.5, width=0.6, color='cyan', label='CAGNN-ATT')
plt.bar(['d'], [17.59], alpha=0.5, width=0.6, color='orange', label='CAGNN-L-ATT')
plt.bar(['e'], [17.73], alpha=0.5, width=0.6, color='blue', label='CAGNN')
plt.xticks([])
plt.legend(loc='upper left')
plt.ylabel('Mrr@20', fontsize=13)
ax3.set_title("Diginetica2")

ax4 = plt.subplot(2, 2, 4)
plt.axis([-1, 5, 13, 20])
plt.bar(['a'], [17.34], alpha=0.5, width=0.6, color='yellow', label='CAGNN-L')
plt.bar(['b'], [16.21], alpha=0.5, width=0.6, color='green', label='CAGNN-AVG')
plt.bar(['c'], [17.08], alpha=0.5, width=0.6, color='cyan', label='CAGNN-ATT')
plt.bar(['d'], [17.89], alpha=0.5, width=0.6, color='orange', label='CAGNN-L-ATT')
plt.bar(['e'], [19.83], alpha=0.5, width=0.6, color='blue', label='CAGNN')
plt.xticks([])
plt.legend(loc='upper left')
plt.ylabel('Mrr@20', fontsize=13)
ax4.set_title("The user behavior dataset")


plt.tight_layout()
plt.savefig('Studies1.png',dpi = 600)
plt.show()
plt.close()
