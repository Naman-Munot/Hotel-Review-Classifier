# use this file to learn naive-bayes classifier 
# Expected: generate nbmodel.txt
import os, string, re, sys,collections,math
from string import punctuation
from string import digits

f_model=open('nbmodel.txt','w')

total=set()
tc=0
dc=int(0)
positivetruthfuldocct=0
positivedeceptivedocct=0
negativetruthfuldocct=0
negativedeceptivedocct=0
di=dict()
positivetruthfulct=0
positivedeceptivect=0
negativetruthfulct=0
negativedeceptivect=0

positivetruthfuldic=collections.defaultdict(int)
negativetruthfuldic=collections.defaultdict(int)
positivedeceptivedic=collections.defaultdict(int)
negativedeceptivedic=collections.defaultdict(int)

def reduction(a):
    if bool(a):
        
        if a.isalpha():
            return True,a
    return False,a
        

      
def read_file(address,cat):
    with open(address,'r') as v:
        sentence=v.read()
        exclude=set(string.punctuation)
        sentence = ''.join(ch for ch in sentence if ch not in exclude)
        words=sentence.replace('\n',' ').lower().split()
        
        
        
    
    for s in words:
        s.strip()
        if s in di:
            di[s] = di[s] + 1
        else:
            di[s] = 1
       
        valid,s=reduction(s)
        if valid:
            total.add(s)
    
            
            
    
    
    if(cat=='PositiveTruthful'):
        global positivetruthfulct
        for b in words:
            b.strip()
            valid, b = reduction(b)
            if valid:
                positivetruthfuldic[b]+=1
                positivetruthfulct+=1
    
    
    elif(cat=='PositiveDeceptive'):
        global positivedeceptivect
        for b in words:
            b.strip()
            valid, b=reduction(b)
            if valid:
                positivedeceptivedic[b]+=1
                positivedeceptivect+=1
                    
    
    elif(cat=='NegativeTruthful'):
        global negativetruthfulct
        for b in words:
            b.strip()
            valid, b=reduction(b)
            if valid:
                negativetruthfuldic[b]+=1
                negativetruthfulct+=1
                    
    
    elif(cat=='NegativeDeceptive'):
        global negativedeceptivect
        for b in words:
            b.strip()
            valid, b=reduction(b)
            if valid:
                negativedeceptivedic[b]+=1
                negativedeceptivect+=1



for root, direct, f_name in os.walk(sys.argv[1]):
    for file in f_name:
        name=str(os.path.join(root,file))
        if('readme' not in name.lower() and name.endswith(".txt")):
            dc+=1
            if('positive' in name.lower() and 'truthful' in name.lower()):
                read_file(name,'PositiveTruthful')
                positivetruthfuldocct+=1
            elif('positive' in name.lower() and 'deceptive' in name.lower()):
                read_file(name,'PositiveDeceptive')
                positivedeceptivedocct+=1
            if('negative' in name.lower() and 'truthful' in name.lower()):
                read_file(name,'NegativeTruthful')
                negativetruthfuldocct+=1
            elif('negative' in name.lower() and 'deceptive' in name.lower()):
                read_file(name,'NegativeDeceptive')
                negativedeceptivedocct+=1

tc=len(total)
#print(tc)
        


    

           
Category = {'NegativeDeceptive':(negativedeceptivect,negativedeceptivedic,negativedeceptivedocct),
            'NegativeTruthful':(negativetruthfulct,negativetruthfuldic,negativetruthfuldocct),
            'PositiveDeceptive':(positivedeceptivect,positivedeceptivedic,positivedeceptivedocct),
            'PositiveTruthful':(positivetruthfulct,positivetruthfuldic,positivetruthfuldocct)
           }
priorprob_positive_deceptive= positivedeceptivedocct/dc
priorprob_negative_deceptive= negativedeceptivedocct/dc
priorprob_positive_truthful= positivetruthfuldocct/dc
priorprob_negative_truthful= negativetruthfuldocct/dc

f_model.write("NegativeDeceptive "+str(priorprob_negative_deceptive)+"\n")
f_model.write("NegativeTruthful "+str(priorprob_negative_truthful)+"\n")
f_model.write("PositiveDeceptive "+str(priorprob_positive_deceptive)+"\n")
f_model.write("PositiveTruthful "+str(priorprob_positive_truthful)+"\n")

for Cat_name in Category:
    temp=float(0)
    ct, Dict, wordct=Category[Cat_name]
    for word in total:
        if (di[word]>1):
            
            if word in Dict:
                    temp=math.log((Dict[word]+1))-math.log(float(ct+tc))
            else:
                temp=math.log((1))-math.log(float(ct+tc))
            
            f_model.write(Cat_name+" "+word+" "+str(temp)+"\n")