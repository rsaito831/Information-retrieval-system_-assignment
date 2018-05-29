# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

s_result = list(pd.read_csv("assignment18_01_RelDocs.csv"))
c_answer = list(pd.read_csv("assignment18_01_AnsSet.csv"))

s_result_set = set(s_result)
c_answer_set = set(c_answer)
match_list = list(s_result_set & c_answer_set)

s_result_size = len(s_result)
c_answer_size = len(c_answer)

N = [i + 1 for i in range(len(match_list))]

precision = []
recall = []
for i in N:
    precision.append(i / s_result_size)
    recall.append(i / c_answer_size)
    print(i)
plt.plot(recall, precision)
plt.show()
print(precision)
print("  ")
print(recall)
