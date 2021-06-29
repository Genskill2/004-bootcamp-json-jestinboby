import json
import math

def load_journal(filename):
	f=open(filename,)
	data = json.load(f)
	f.close()
	return data

def compute_phi(filename,event):
	data = load_journal(filename)
	n11=n00=n10=n01=n1p=n0p=np1=np0=0
	for i in data:
		if event in i['events']:
			n1p += 1
			if i['squirrel'] == True:
				np1 += 1
				n11 += 1
			else:
				np0 += 1
				n10 += 1
		else:
			n0p += 1
			if i['squirrel'] == True:
				np1 += 1
				n01 += 1
			else:
				np0 += 1
				n00 += 1

	return (n11*n00 - n10*n01) / math.sqrt(n1p*n0p*np1*np0)

def compute_correlations(filename):
	data = load_journal(filename)
	corr_dic = {}
	for i in data:
		for event in i['events']:
			if event not in corr_dic.keys():
				corr_dic[event] = compute_phi(filename,event)
	return corr_dic

def diagnose(filename):
	corr_dic = compute_correlations(filename)
	max_value=max(corr_dic, key=corr_dic.get)
	min_value=min(corr_dic, key=corr_dic.get)
	return max_value,min_value
