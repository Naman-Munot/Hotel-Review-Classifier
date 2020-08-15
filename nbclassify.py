# use this file to classify using naive-bayes classifier 
# Expected: generate nboutput.txt

import sys,os,math
import string

positivedeceptivedic=dict()
positivetruthfuldic=dict()
negativetruthfuldic=dict()
negativedeceptivedic=dict()
f_model=open("nboutput.txt",'w')
NegativeDeceptive=float(0)
NegativeTruthful=float(0)
PositiveDeceptive=float(0)
PositiveTruthful=float(0)

    
with open("nbmodel.txt") as f:
    lines=f.readlines()
    NegativeDeceptive=float(lines[0].split(" ")[1])
    NegativeTruthful=float(lines[1].split(" ")[1])
    PositiveDeceptive=float(lines[2].split(" ")[1])
    PositiveTruthful=float(lines[3].split(" ")[1])
    for line in range(4,len(lines)):
        partition=lines[line].split(" ")
        if partition[0]=="NegativeDeceptive":
            negativedeceptivedic[partition[1]] = float(partition[2])
        if partition[0]=="NegativeTruthful":
            negativetruthfuldic[partition[1]] = float(partition[2])
        if partition[0]=="PositiveDeceptive":
            positivedeceptivedic[partition[1]] = float(partition[2])
        if partition[0]=="PositiveTruthful":
            positivetruthfuldic[partition[1]] = float(partition[2])   
        
        
def reduction(a):
    if bool(a):
        a.strip()
        
        if a.isalpha():
            return True,a
    return False,a
        
    
      
def read_file(address,prob_neg_decept,prob_neg_truth,prob_pos_decept,prob_pos_truth):
    with open(address,'r') as v:
        sentence=v.read()
        exclude=set(string.punctuation)
        sentence = ''.join(ch for ch in sentence if ch not in exclude)
        words=sentence.replace('\n',' ').lower().split()
    
    for s in words:
        
        s.strip()
        valid,s=reduction(s)
        
        if valid:
            #print(prob_neg_decept)
            #print(negativedeceptivedic[s])
            if s in negativedeceptivedic:
                prob_neg_decept+=float(negativedeceptivedic[s])
            if s in negativetruthfuldic:
                prob_neg_truth+=negativetruthfuldic[s]
            if s in positivedeceptivedic:
                prob_pos_decept+=positivedeceptivedic[s]
            if s in positivetruthfuldic:
                prob_pos_truth+=positivetruthfuldic[s]
    res=max(prob_neg_decept,prob_neg_truth,prob_pos_decept,prob_pos_truth)
    if res==prob_neg_decept:
        f_model.write("deceptive negative "+name+"\n")
    elif res==prob_neg_truth:
        f_model.write("truthful negative "+name+"\n")
    elif res==prob_pos_decept:
        f_model.write("deceptive positive "+name+"\n")
    elif res==prob_pos_truth:
        f_model.write("truthful positive "+name+"\n")
        
for root, direct, f_name in os.walk(sys.argv[1]):
    for file in f_name:
        name=str(os.path.join(root,file))
        if('readme' not in name.lower() and name.endswith(".txt")):
            
            read_file(name,NegativeDeceptive,NegativeTruthful,PositiveDeceptive,PositiveTruthful)