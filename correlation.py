import json
from math import sqrt

def load_journal(journal):
 f = open(journal)
 data = json.load(f)
 return data

def compute_phi(journal,event):
  phi = 0
  data = load_journal(journal)
  var1,var2,var3,var4,var5,var6,var7,var8 = 0,0,0,0,0,0,0,0
  for i in data:
      if event in i['events']:
          var5 += 1
          if i['squirrel']==True:
              var1 += 1
              var7 += 1
          else:
              var3 += 1
              var8 += 1
  else:
          var6 += 1
          if i['squirrel']==True:
                var7 += 1
                var4 += 1
          else:
                var8 += 1
                var2 += 1
  phi = (var1*var2)-(var3*var4)/sqrt(var5*var6*var7*var8)
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
