'''
Give proper brackets
example: ((a|b)*) , (((a.b).c)|a)
I have used 'e' to represent epsilon
and don't use variable names starting from 't'
since i have used it to store temporary states
'''

re = input()
reoo=re
tk=1
k=0
def get():
    global re,tk
    r=re
    i1=r.find(')')
    if(i1==-1):
        return 'end'
    r1=r[i1::-1]
    i2=r1.find('(')
    i2=len(r1)-i2
    s=re[i2:i1]
    re=re[:i2-1]+'t'+str(tk) +re[i1+1:]
    tk=tk+1
    return s

dic={}

def cr(s):
    global k
    if(s in dic):
        dic[s].append([k,k+1])
    else:
        dic[s]=[[k,k+1]]
    k=k+2
    return [k-2,k-1]

def cre(c,n):
    if('e'in dic):
        x=[c,n]
        dic['e'].append(x)
    else:
        dic['e']=[[c,n]]

def crt(a,b):
    x = 't' + str(tk - 1)
    dic[x]=[[a,b]]

def orr(s):
    global k
    i=s.index('|')
    fi=s[:i]
    se=s[i+1:]
    if(fi[0]=='t'):
        k1=dic[fi][0][0]
        k2=dic[fi][0][1]
    else:
        l=cr(fi)
        k1=l[0]
        k2=l[1]

    if(se[0] == 't'):
        k11 = dic[se][0][0]
        k22 = dic[se][0][1]
    else:
        l = cr(se)
        k11 = l[0]
        k22 = l[1]
    cre(k,k1)
    cre(k,k11)
    cre(k2,k+1)
    cre(k22,k+1)
    x = 't' + str(tk - 1)
    cr(x)

def dot(s):
    global k
    i=s.find('.')
    fi = s[:i]
    se = s[i + 1:]
    if(fi[0]=='t'):
        l=dic[fi][0]
    else:
        l=cr(fi)
    if(se[0]=='t'):
        l1=dic[se][0]
        cre(l[1],l1[0])
    else:
        l1=cr(se)
        cre(l[1],l1[0])
    crt(l[0],l1[1])

def st(s):
    i=s.find('*')
    fi=s[:i]
    if(fi not in dic):
        cr(fi)
    l=dic[fi][0]
    cre(l[1],l[0])
    cre(k, l[0])
    cre(l[1], k+1)
    cre(k,k+1)
    x = 't' + str(tk - 1)
    cr(x)



s=get()
while(s!='end'):
    if(s.find('|')!=-1):
        orr(s)

    elif(s.find('.')!=-1):
        dot(s)

    elif(s.find('*')!=-1):
        st(s)
    
    s=get()
print("Transition symbol : [transition_from_state , Transition_to_state]")
print(dic)
print()
print("Transition Table")

l=[]
for i in range(0,k):
    a=[]
    for j in range(0,k):
        a.append(' ')
    l.append(a)

for i in dic.keys():
    if(i in reoo):
        for j in dic[i]:
            l[j[0]][j[1]]=i
for i in dic['e']:
    l[i[0]][i[1]]='e'

l1=[]
print("  ",end="")
for i in range(0,k):
    l1.append(str(i))
print(l1)
for i in range(0,k):
    print(i,end=" ")
    print(l[i])
