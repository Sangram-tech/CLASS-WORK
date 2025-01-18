#LIST COMPRIHENSION
L1=[1,2,3,4,5,6,7,8,9,10]
L2=[i for i in L1 if i%2==0]
print(L2)
#SET COMPRIHENSION
S1={1,2,3,4,5,6,7,8,9,10}
S2={i for i in S1 if i%2==0}
print(S2)
#DICT COMPRIHENSION
D1={1:'A',2:'B',3:'C',4:'D',5:'E'}
D2={k:v for k,v in D1.items() if k%2==0}
print(D2)
