# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

fn = list(pd.read_csv("assignment18_01_RelDocs.csv"))
fp = list(pd.read_csv("assignment18_01_AnsSet.csv"))

tp = []
precision = []
recall = []
size_fn = len(fn)
size_tp_after = 0
cnt = 0

for tag in fp:
    cnt = cnt + 1
    tp += list(filter(lambda x: x == tag, fn))
    size_tp = len(tp)
    if size_tp_after != size_tp:
        precision.append(size_tp / cnt)
        recall.append(size_tp / size_fn)
        size_tp_after = size_tp
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.plot(recall, precision)
plt.show()

print(fp)
print(fn)
print(tp)
# print(precision)
# print(recall)
