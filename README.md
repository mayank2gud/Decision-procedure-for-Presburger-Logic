# MayankSati_ATC_2021_Assignment

Instructions to run the code:
First the user needs to define the variables that are used in the z3 expression and store them in list x[]. (because it seems that z3 variable needs to be defined prior to expressing the z3 formula)
Example :

if z3 formula is f=Not(Not(x1+2*x2+(-3)*x3<=5))
then user needs to define:
x1=Int('x1')

x2=Int('x2')

x3=Int('x3')

and the list x[] would contain:

x=[x1,x2,x3]

the values for the z3 variables is to be inserted in list val[]

Example if x1=5,x2=4,x3=0

then val[]=[5,4,0]

Next, the z3 formula itself should be written as: 

f= (z3 formula)

Ex:	f=x1+x2<=5

Note:
To enter negative coeffecients, one needs to explicitly write -1*(z3 variable)
Ex: 
for z3 formula 2*x1-3*x2<=5,
f should be: f=2*x1+(-3)*x2<=5

Due to time constraints and increasing comlexity of the code, it is assumed that in 'and' operator, both the arguments have "all" the z3 variables as common.

Ex:  f=And(x1+x2<=2,x1+x2==5) will show the desired output 

but f=And(x3+x4<=2,x1+x2==5) will not.
