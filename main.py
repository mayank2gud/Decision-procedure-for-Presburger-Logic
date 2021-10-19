import prettytable
from z3 import *
from prettytable import PrettyTable
val=[2,1,3,4]
#global x
visited=set()
map={}
def table_and(variables,table0,rhs0,fs0,vis0,table1,rhs1,fs1,vis1):
    l=[]
    flist=[]
    table=PrettyTable()
    s=len(variables)
    T0={}
    T1={}
    FS=[]
    print("000000000")
    print(table0)
    print(table1)
    
    for row in table0:
        #R=[]
        row.border = False
        row.header = False
        R=row.get_string().strip()
        print("R raw: ",R)
        R=R.split('  ')
        print("R1: ",R)
        elem=R.pop(0)
        T0[elem]=R
    
    for row in table1:
        R=[]
        row.border = False
        row.header = False
        R=row.get_string().strip()
        R=R.split('  ')
        print("R2: ",R)
        elem=R.pop(0)
        T1[elem]=R
    print("tables: ")
    print(T0)
    print(T1)

    a=[None]*s
    for i in range(0,pow(2,s)):
        t=[]
        for j in range(s):
            a[j]=int((i/pow(2,s-1-j))%2)
            t.append(a[j])
        l.append(t)
    l.insert(0,"State")
    table.field_names =l

    visited=[[rhs0,rhs1]]
    flist.append([rhs0,rhs1])

    print("s= ",s)
    while len(flist)!=0:
        head=flist.pop(0)
        print("head: ",head)
        row=[]
        row.append(head)
        for i in range(0,pow(2,s)):
            x1=[]
            tmpx=str(head[0])
            tmplist=T0.get(tmpx)
            print("templist: ",tmplist)
            x1.append(tmplist[i])
            tmpx=str(head[1])
            tmplist=T1.get(tmpx)
            x1.append(tmplist[i])
            print("@@x1: ",x1)
            row.append(x1)
            if x1 not in visited:
                visited.append(x1)
                flist.append(x1)
        table.add_row(row)

    print(table)
    print("Initial State: ",[rhs0,rhs1])
    for i in fs0:
        for j in fs1:
            if [i,j] in visited:
                if [i,j] not in FS:
                    FS.append([i,j])
    print("Final State: ",FS)
    
    return table,[rhs0,rhs1],FS,visited


                

        
            



    #a = arr.array('i')
    #len(a)=s
    ##############
    a=[None]*s
    for i in range(0,pow(2,s)):
        t=[]
        for j in range(s):
            a[j]=int((i/pow(2,s-1-j))%2)
            t.append(a[j])
        l.append(t)
    l.insert(0,"State")
    table1.field_names =l
    visited=[rhs]

    flist.append(rhs)
    #print("list ",flist[0])
    flag=0
    #print("ooooooo")
    while len(flist)!=0:
       # print("!!!!!")
        C=flist.pop(0)
        c=("%s"%(C))
        c=int(c)
        row=[]
        row.append(c)
        
 
        for i in range(0,pow(2,s)):
            sum=0
            for j in range(s):
                a[j]=int((i/pow(2,s-1-j))%2)
                sum=sum+a[j]*ret[j]
           # print("sum",sum)
           # print("c ",c)
           # print("sum mod2",sum%2)
           # print("c mod 2",c%2)
            if sum%2==c%2:
                #print("sda")
                value=(c-sum)//2
                row.append(value)
                if value not in visited:
                    visited.append(value)
                    flist.append(value)

            else :
                flag=1
                row.append("Err")

                #t.append(a[j])
           #row.append(sum)
        table1.add_row(row)
        #print("row : ",row)
    if flag==1:
        row=["Err"]
        for i in range(0,pow(2,s)):
            row.append("Err")

        table1.add_row(row)


    #print("l= ",l)
    print(table1)
    print("Initial State: ",rhs)
    print("Final State: 0")
    fs=[0]
    return table1,rhs,fs,visited
    
#####################

def table_not(table1,start,final,vis):
    f=[]
    print(table1)
    print("Initial State: ",start)
    for i in vis:
        if i not in final:
            i=("%s"%(i))
            i=int(i)
            f.append(i)
    
    for row in table1[-1]:
        row.border = False
        row.header = False
        if row.get_string(fields=["State"]).strip()=='Err':
            f.append(row.get_string(fields=["State"]).strip())
    if 'Err' in final:
        f.remove('Err')
    print("Final State: ",f)
    return table1,start,f,vis

def table_leq(f,ret,variables,rhs):
    print("Table for ",f)
    l=[]
    flist=[]
    table1=PrettyTable()
    s=len(variables)
    print("s= ",s)
    #a = arr.array('i')
    #len(a)=s
    a=[None]*s
    for i in range(0,pow(2,s)):
        t=[]
        for j in range(s):
            a[j]=int((i/pow(2,s-1-j))%2)
            t.append(a[j])
        l.append(t)
    l.insert(0,"State")
    table1.field_names =l
    visited=[rhs]

    flist.append(rhs)
    #print("list ",flist[0])
    flag=0
    #print("ooooooo")
    while len(flist)!=0:
       # print("!!!!!")
        C=flist.pop(0)
        c=("%s"%(C))
        c=int(c)
        row=[]
        row.append(c)
        
 
        for i in range(0,pow(2,s)):
            sum=0
            for j in range(s):
                a[j]=int((i/pow(2,s-1-j))%2)
                sum=sum+a[j]*ret[j]
           # print("sum",sum)
           # print("c ",c)
           # print("sum mod2",sum%2)
           # print("c mod 2",c%2)
            #if sum%2==c%2:
                #print("sda")
            value=(c-sum)//2
            row.append(value)
            if value not in visited:
                visited.append(value)
                flist.append(value)

           # else :
            #    flag=1
             #   row.append("Err")

                #t.append(a[j])
           #row.append(sum)
        table1.add_row(row)
        #print("row : ",row)
    if flag==1:
        row=["Err"]
        for i in range(0,pow(2,s)):
            row.append("Err")

        table1.add_row(row)


    #print("l= ",l)
    print(table1)
    fs=[]
    print("Initial State: ",rhs)
    for i in visited:
        i=("%s"%(i))
        i=int(i)
        if i>=0:
            fs.append(i)
    print("Final State: ",fs)
    return table1,rhs,fs,visited


def table_eq(f,ret,variables,rhs):
    #print(rhs)
    #print(f)
    #print("ret : ",ret)
    print("Table for ",f)
    l=[]
    flist=[]
    table1=PrettyTable()
    s=len(variables)
    print("s= ",s)
    #a = arr.array('i')
    #len(a)=s
    a=[None]*s
    for i in range(0,pow(2,s)):
        t=[]
        for j in range(s):
            a[j]=int((i/pow(2,s-1-j))%2)
            t.append(a[j])
        l.append(t)
    l.insert(0,"State")
    table1.field_names =l
    visited=[rhs]

    flist.append(rhs)
    #print("list ",flist[0])
    flag=0
    #print("ooooooo")
    while len(flist)!=0:
       # print("!!!!!")
        C=flist.pop(0)
        c=("%s"%(C))
        c=int(c)
        row=[]
        row.append(c)
        
 
        for i in range(0,pow(2,s)):
            sum=0
            for j in range(s):
                a[j]=int((i/pow(2,s-1-j))%2)
                sum=sum+a[j]*ret[j]
           # print("sum",sum)
           # print("c ",c)
           # print("sum mod2",sum%2)
           # print("c mod 2",c%2)
            if sum%2==c%2:
                #print("sda")
                value=(c-sum)//2
                row.append(value)
                if value not in visited:
                    visited.append(value)
                    flist.append(value)

            else :
                flag=1
                row.append("Err")

                #t.append(a[j])
           #row.append(sum)
        table1.add_row(row)
        #print("row : ",row)
    if flag==1:
        row=["Err"]
        for i in range(0,pow(2,s)):
            row.append("Err")

        table1.add_row(row)


    #print("l= ",l)
    print(table1)
    print("Initial State: ",rhs)
    print("Final State: 0")
    fs=[0]
    return table1,rhs,fs,visited

    


##str=input()
##n=int(input())

#for i in range(n):

def cal(f):
    print(f)
    variables=set()
    if  f.decl().name()=='and':
        ret=[]
        TABLE1=[]
        RHS=[]
        FS=[]
        VIS=[]
        #print(f.decl().name())
        arg=f.num_args()
        for i in range(arg):
            t,num,table1,rhs,fs,vis=cal(f.arg(i))
            print("fn call table: ",table1)
            TABLE1.append(table1)
            RHS.append(rhs)
            FS.append(fs)
            VIS.append(vis)
            for temp in num:
                ret.append(temp)
            if t is not None:
                for j in t:
                    variables.add(j)
                    print("Table for ",f)
        
        table1,rhs,fs,vis= table_and(variables,TABLE1[0],RHS[0],FS[0],VIS[0],TABLE1[1],RHS[1],FS[1],VIS[1])
        return variables,ret,table1


    elif f.decl().name()=='=':
        ret=[]
        #print(f.decl().name())
        arg=f.num_args()
        for i in range(arg):
            t,num=cal(f.arg(i))
            for temp in num:
                ret.append(temp)
            if t is not None:
                for j in t:
                    variables.add(j)

        #print(f)
        table1,rhs,fs,vis=table_eq(f,ret,variables,f.arg(1))
        return variables,ret,table1,rhs,fs,vis


    elif f.decl().name()=='<=':
        ret=[]
        #print(f.decl().name())
        arg=f.num_args()
        for i in range(arg):
            t,num=cal(f.arg(i))
            for temp in num:
                ret.append(temp)
            if t is not None:
                for j in t:
                    variables.add(j)

        #print(f)
        table1,rhs,fs,vis=table_leq(f,ret,variables,f.arg(1))
        return variables,ret,table1,rhs,fs,vis


    elif f.decl().name()=='not':
        ret=[]
        #tab=[]
        #print(f.decl().name())
        arg=f.num_args()
        for i in range(arg):
            t,num,table1,rhs,fs,vis=cal(f.arg(i))
            #tab.append(table1)
            for temp in num:
                ret.append(temp)
            if t is not None:
                for j in t:
                    variables.add(j)
        print("table for ",f)
        table1,rhs,fs,vis=table_not(table1,rhs,fs,vis)
        return variables,ret,table1,rhs,fs,vis
    

    elif f.decl().name()=='*':
        ret=[]
        arg=f.num_args()
        for i in range(arg):
            t,num=cal(f.arg(i))
            for temp in num:
                ret.append(temp)
            if t is not None:
                for j in t:
                 variables.add(j)
        ret.pop(-1)
        return variables,ret

   
    elif f.decl().name()=='+' or f.decl().name()=='-':
        ret=[]
        arg=f.num_args()
        for i in range(arg):
            t,num=cal(f.arg(i))
            print("+ t: ",t)
            for temp in num:
                ret.append(temp)
            if t is not None:
                for j in t:
                    print("j in t: ",j)
                    variables.add(j)
        print("var from +: ",variables)
        return variables,ret

    elif f.decl().name()=='Int':
        l=[]
        i=("%s"%(f))
        i=int(i)
        l.append(i)
        return None,l
    else:
        #x[i]=Int(f)
        l=[1]
        v=set()
            #print(val[0])
        visited.add(f)
        map[f]=val[0]
        del val[0]
        v.add(f)
        return v,l

        print("decl= %s , val= %s " %(f,map[f]))



x1=Int('x1')
x2=Int('x2')
x3=Int('x3')
x4=Int('x4')
x=[x1,x2,x3,x4]
#f=And(Not(x1 + x2 <= 2), x2 <= 1)
f=Not(Not(x1+2*x2+(-3)*x3<=5))
#f=Not(x1+x2<=5)
f=Not(x1<=2)
f=And(x1+x2<=2,x1+x2==5)
#f=x1+x2<=5
#f=x1<=2
f_t=f
cal(f)

#print("ans: ",simplify(f))
#print(visited)
print("For: ")
for i,j in map.items():
    print("%s = %s" %(i,j))
    f=substitute(f,(i,IntVal(j)))
print("%s is %s" %(f_t,simplify(f)))
#print(simplify(f))
#print(map)
