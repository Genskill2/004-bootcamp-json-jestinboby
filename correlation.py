import json
import math

def load_journal(filename):
 with open('filename') as f:
  data = json.load(f)
 return data

def compute_phi(filename,event):
  data = load_journal(journal)
  n11 = n00 = n10 = n01 = n1plus = n0plus = nplus1 = nplus0 = 0
  for i in data:
    if i['squirrel'] == True:
        n1plus += 1
        if(event in i['events']):
            n11 += 1
            nplus1 += 1
        else:
            nplus0 += 1
            n10 += 1
    else:
        n0plus += 1
        if event in i['events']:
            n01 += 1
            nplus1 += 1
        else:
            n00 += 1
            nplus0 += 1
    phi = (n11*n00 - n10*n01)/math.sqrt(n1plus*n0plus*nplus1*nplus0)
    return phi

def compute_correlations(filename):
  data = load_journal(filename)
  corr_dict = {}
  for i in data:
      for j in i['events']:
         corr_val = compute_phi(filename,j)
         if j not in corr_dict:
             corr_dict[j]=corr_val
  return corr_val

def diagnose(filename):
    corr_dict=compute_correlations(filename)
    max = min = 0
    for key,value in corr_dict.items():
        if value >= 0:
            if value > max:
                max = value
                max_key = max_key
        else:
            if value < min:
                min = value
                min_key = max_key
    return max_key,min_key
