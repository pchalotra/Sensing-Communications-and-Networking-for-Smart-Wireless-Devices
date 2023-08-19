# Question 1

### (a)  Find the frequencies of POS tags of words


# Here we import parse to parsing the conllu file 
from conllu import parse

#open the conllu file
with open('hi_hdtb-ud-train.conllu', "r", encoding="utf-8") as file:
    data_file = file.read()
sentences = parse(data_file)

#finding the pos_tag of words
pos_tag_freq={}
for words in sentences:
    for word in words:
        if  (word['upos']) not in  pos_tag_freq.keys():
            pos_tag_freq[word['upos']]=1
        else:
            pos_tag_freq[word['upos']]+=1
            
            
pos_tag_freq = sorted(pos_tag_freq.items(), key=lambda x:x[1],reverse=True)
print(pos_tag_freq)

"""### (b) list the 50 most frequent words corresponding to each POS tag"""

#import counter for counting
#finding the dictionary contain the pos tag with corresponding words
from collections import Counter
lemma = {}
for words in sentences:
    for word in words:
        list1 = lemma.get(word['upos'], [])
        list1.append(word['form'])
        lemma[word['upos']]= list1

#Here sort the lemma dict and save into another dict lemma2
lemma2 = {}
for k,v in lemma.items():
    temp1 = dict(Counter(v))
    marklist = sorted(temp1.items(), key=lambda x:x[1],reverse=True)
    lemma2[k] = marklist

# finding most frequent words corresponding to each pos_tag
for p,q in lemma2.items():
    lemma2[p]=q[:50]
lemma2

"""### (c) Find the frequencies of gender, case and number of words separately"""

dict1={}
for words in sentences:
    for word in words:
        dict1[word['form']]=word['feats']

# finding the gender_freq
gender_freq={}
for key,value in dict1.items():
    if value is not None:
        for x,y in value.items():
            if x=='Gender':
                    if y in gender_freq:
                        gender_freq[y]+=1
                    else:
                        gender_freq[y]=1
            else:
                continue

gender_freq

#finding the case freq
case_freq={}
for key,value in dict1.items():
    if value is not None:
        for x,y in value.items():
            if x=='Case':
                    if y in case_freq:
                        case_freq[y]+=1
                    else:
                        case_freq[y]=1
            else:
                continue

case_freq

number_freq={}
for key,value in dict1.items():
     if value is not None:
        for x,y in value.items():
            if x=='Number':
                    if y in number_freq:
                        number_freq[y]+=1
                    else:
                        number_freq[y]=1
            else:
                continue

number_freq

"""### (d)  List the 50 most frequent combinations of gender, case and number as a 3-tuple."""

#Here find the dict with combinations of gender,case,number 
G_C_N={}
for key,value in dict1.items():
    if value is not None :
        if(value.keys() >= { "Case","Gender","Number"}):
            
            if (value['Gender'],value['Case'],value['Number']) not in G_C_N.keys():
                G_C_N[(value['Gender'],value['Case'],value['Number'])]=1
            else:
                G_C_N[(value['Gender'],value['Case'],value['Number'])]= G_C_N[(value['Gender'],value['Case'],value['Number'])]+1

        else:
            continue

G_C_N= sorted(G_C_N.items(), key=lambda x:x[1],reverse=True)
G_C_N

"""### (e)  Find the frequencies of POS tags corresponding to only head words."""

# here finding the dict contain pos tag with corresponding head_word
head_word={}
for words in sentences:
    for word in words:
        list2=head_word.get(word['upos'],[])
        y=(word['misc'])['ChunkType']
        if(y=='head'):
                list2.append(word['form'])
                head_word[word['upos']]=list2
        else:
                continue

# sort the dict and calculate freq of pos tag
m1={}
freq_pos_head={}
for k,v in head_word.items():
    t1 =len(v)
    m1[k] = t1
    freq_pos_head = sorted(m1.items(), key=lambda x:x[1],reverse=True)
freq_pos_head

"""### (f)  Find the directed POS tag tuples (ti,tj),for each such 2-tuple, list the frequencies separately for each relation             R as well as total"""

#dict contain the tuple of tag and corresponding relation by finding the value of head word with which we find the relation of words
Rel_dict={}
for words in sentences:
    for word in words:
        p=word['head']
        list3=Rel_dict.get((word['upos'],(words[p-1])['upos']),[])
        list3.append(word['deprel'])
        Rel_dict[(word['upos'],(words[p-1])['upos'])]=list3

# here we sort the dict
Rel_dict2 = {}
for k,v in Rel_dict.items():
    t2= dict(Counter(v))
    marklist = sorted(t2.items(), key=lambda x:x[1],reverse=True)
    Rel_dict2[k] = marklist
print(Rel_dict2)

#use the Rel_dict2 and calculate the total no of frequency of relation correponding to each tuple
y=0
freq_rel={}
for k,v in Rel_dict2.items():
    for i in range(len(v)):
        y+=(((Rel_dict2[k])[i])[1])

    freq_rel[k]=y
                
                
        
freq_rel=sorted(freq_rel.items(), key=lambda x:x[1], reverse=True)  
freq_rel

"""### (g) For each dependency relation R, list the frequencies separately for each 2-tuple (ti,tj)  as well as total."""

#we use head word and find the pair which contain the relation and make dict contain the relation and corresponding tuple
Rel_dict3={}

for words in sentences:
    for word in words:
        p=word['head']
        list4=Rel_dict3.get(word['deprel'],[])
        list4.append((word['upos'],(words[p-1])['upos']))
        Rel_dict3[word['deprel']]=list4

Rel_dict3

# here we sort the dictionary 
Rel_dict4 = {}
for k,v in Rel_dict3.items():
    t2= dict(Counter(v))
    marklist = sorted(t2.items(), key=lambda x:x[1],reverse=True)
    Rel_dict4[k] = marklist
print(Rel_dict4)

#use the Rel_dict4 and calculate the total no of frequency of tuple correponding to each relation
y=0
freq_rel2={}
for k,v in Rel_dict4.items():
    for i in range(len(v)):
        y+=(((Rel_dict4[k])[i])[1])

    freq_rel2[k]=y
                
freq_rel2=sorted(freq_rel2.items(), key=lambda x:x[1], reverse=True)  
freq_rel2



