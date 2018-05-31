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
precision.insert(0, 1.0)
recall.insert(0, 0)
precision.extend([0, 0, 0])
recall.extend([0.9, 0.95, 1.0])
plt.xlim([0, 1.0])
plt.ylim([0, 1.0])
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.plot(recall, precision, lw=3)
plt.show()

# print(fp)
# print(fn)
# print(tp)
# print(precision)
# print(recall)

s = 0
j = 0
for i in range(len(recall)):
    if recall[i] == j / 10:
        s += precision[i]
        j = j + 1

ave_precision = s / 11
print("11-point Ave Precision = ", ave_precision)
r_precision = size_tp / len(fp)
print("R-Precision = ", r_precision)
