import json
import math

def load_journal(journal):
 f = open(journal)
 data = json.load(f)
 return data

def compute_phi(journal,event):
  data = load_journal(journal)
  n11 = n00 = n10 = n01 = n1_ = n0_ = n_1 = n_0 = 0
  for i in data:
    if i['squirrel'] == True:
        n1_ += 1
        if(event in i['events']):
            n11 += 1
            n_1 += 1
        else:
            n_0 += 1
            n10 += 1
    else:
        n0_ += 1
        if event in i['events']:
            n01 += 1
            n_1 += 1
        else:
            n00 += 1
            n_0 += 1
    num = (n11*n00) - (n10*n01)
    den = sqrt(n1_*n0_*n_1*n_0)
    phi = num/den
    return phi

def compute_correlations(journal):
  data = load_journal(journal)
  corr_dict = {}
  for i in data:
      for j in i['events']:
         corr_val = compute_phi(journal,j)
         if j not in corr_dict:
             corr_dict[j]=corr_val
  return corr_val

def diagnose(journal):
    corr_dict=compute_correlations(journal)
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
