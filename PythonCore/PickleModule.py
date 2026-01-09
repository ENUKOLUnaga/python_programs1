import pickle
with open("Data.text","wb") as f1:
    n=1
    f=10.5
    lst=[1,2,3,4]
    tup=(4,5,6)
    dict={1:"java",2:"c",3:"Python"}

    pickle.dump(n,f1)
    pickle.dump(f,f1)
    pickle.dump(lst,f1)
    pickle.dump(tup,f1)
    pickle.dump(dict,f1)
f1.close()

with open("Data.text","rb") as f1:
    i=pickle.load(f1)
    j=pickle.load(f1)
    k=pickle.load(f1)
    l=pickle.load(f1)
    m=pickle.load(f1)

    print(i)
    print(j)
    print(k)
    print(l)
    print(m)
    
