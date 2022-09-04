# Decision procedure for Presburger Logic

Instructions to run the code:

First the user needs to define the variables that are used in the z3 expression and store them in list x[]. (because it seems that z3 variable needs to be defined prior to expressing the z3 formula)

Example :

if z3 formula is 

f=Not(Not(x1+2*x2+(-3)*x3<=5))

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

Ex:  f=And(x1+x2<=2,x1+x2==5) will show the desired Output 

but f=And(x3+x4<=2,x1+x2==5) will not.


## Test Cases:

### sample Input 1:

val=[10]

x1=Int('x1')

x=[x1]

f=x1<=2


### Output:

Table for  x1 <= 2
+-------+-----+-----+

| State | [0] | [1] |

+-------+-----+-----+

|   2   |  1  |  0  |

|   1   |  0  |  0  |

|   0   |  0  |  -1 |

|   -1  |  -1 |  -1 |

+-------+-----+-----+

Initial State:  2

Final State:  [2, 1, 0]

For:

{x1: 10}
x1 = 10

x1 <= 2 is False


### sample Input 2:

val=[1]
x1=Int('x1')
x=[x1]
f=x1<=2

### Output:
Table for  x1 <= 2
+-------+-----+-----+

| State | [0] | [1] |

+-------+-----+-----+

|   2   |  1  |  0  |

|   1   |  0  |  0  |

|   0   |  0  |  -1 |

|   -1  |  -1 |  -1 |

+-------+-----+-----+

Initial State:  2

Final State:  [2, 1, 0]

For:
{x1: 1}
x1 = 1

x1 <= 2 is True


### sample Input 2:

val=[2,1]

x1=Int('x1')

x2=Int('x2')


x=[x1,x2]

f=x1+x2<=5

### Output:
Table for  x1 + x2 <= 5

+-------+--------+--------+--------+--------+

| State | [0, 0] | [0, 1] | [1, 0] | [1, 1] |

+-------+--------+--------+--------+--------+

|   5   |   2    |   2    |   2    |   1    |

|   2   |   1    |   0    |   0    |   0    |

|   1   |   0    |   0    |   0    |   -1   |

|   0   |   0    |   -1   |   -1   |   -1   |

|   -1  |   -1   |   -1   |   -1   |   -2   |

|   -2  |   -1   |   -2   |   -2   |   -2   |

+-------+--------+--------+--------+--------+

Initial State:  5

Final State:  [5, 2, 1, 0]
For:
{x1: 2, x2: 1}
x1 = 2
x2 = 1
x1 + x2 <= 5 is True


### sample Input 3:

val=[2,1,0]

x1=Int('x1')

x2=Int('x2')

x3=Int('x3')

x=[x1,x2,x3]
f=x1+2*x2+(-3)*x3==1
### Output:
Table for  x1 + 2*x2 + -3*x3 == 1

+-------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

| State | [0, 0, 0] | [0, 0, 1] | [0, 1, 0] | [0, 1, 1] | [1, 0, 0] | [1, 0, 1] | [1, 1, 0] | [1, 1, 1] |

+-------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

|   1   |    Err    |     2     |    Err    |     1     |     0     |    Err    |     -1    |    Err    |

|   2   |     1     |    Err    |     0     |    Err    |    Err    |     2     |    Err    |     1     |

|   0   |     0     |    Err    |     -1    |    Err    |    Err    |     1     |    Err    |     0     |

|   -1  |    Err    |     1     |    Err    |     0     |     -1    |    Err    |     -2    |    Err    |

|   -2  |     -1    |    Err    |     -2    |    Err    |    Err    |     0     |    Err    |     -1    |

|  Err  |    Err    |    Err    |    Err    |    Err    |    Err    |    Err    |    Err    |    Err    |

+-------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

Initial State:  1

Final State: 0

For:
{x1: 2, x2: 1, x3: 0}
x1 + 2*x2 + -3*x3 == 1 is False

### sample Input 4:

val=[2,1,0]

x1=Int('x1')

x2=Int('x2')

x3=Int('x3')

x=[x1,x2,x3]

f=Not(x1+2*x2+(-3)*x3==1

### Output:
table for  Not(x1 + 2*x2 + -3*x3 == 1)

+-------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

| State | [0, 0, 0] | [0, 0, 1] | [0, 1, 0] | [0, 1, 1] | [1, 0, 0] | [1, 0, 1] | [1, 1, 0] | [1, 1, 1] |

+-------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

|   1   |    Err    |     2     |    Err    |     1     |     0     |    Err    |     -1    |    Err    |

|   2   |     1     |    Err    |     0     |    Err    |    Err    |     2     |    Err    |     1     |

|   0   |     0     |    Err    |     -1    |    Err    |    Err    |     1     |    Err    |     0     |

|   -1  |    Err    |     1     |    Err    |     0     |     -1    |    Err    |     -2    |    Err    |

|   -2  |     -1    |    Err    |     -2    |    Err    |    Err    |     0     |    Err    |     -1    |

|  Err  |    Err    |    Err    |    Err    |    Err    |    Err    |    Err    |    Err    |    Err    |

+-------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

Initial State:  1

Final State:  [1, 2, -1, -2, 'Err']
For:
{x1: 2, x2: 1, x3: 0}

Not(x1 + 2*x2 + -3*x3 == 1) is True



### sample Input 5:

val=[1,1,0]
x1=Int('x1')
x2=Int('x2')
x=[x1,x2]

f=And((x1+2*x2==4),(x1+x2<=3))

### Output:
Table for  x1 + 2*x2 == 4

+-------+--------+--------+--------+--------+

| State | [0, 0] | [0, 1] | [1, 0] | [1, 1] |

+-------+--------+--------+--------+--------+

|   4   |   2    |   1    |  Err   |  Err   |

|   2   |   1    |   0    |  Err   |  Err   |

|   1   |  Err   |  Err   |   0    |   -1   |

|   0   |   0    |   -1   |  Err   |  Err   |

|   -1  |  Err   |  Err   |   -1   |   -2   |

|   -2  |   -1   |   -2   |  Err   |  Err   |

|  Err  |  Err   |  Err   |  Err   |  Err   |

+-------+--------+--------+--------+--------+
Initial State:  4

Final State: 0

Table for  x1 + x2 <= 3
+-------+--------+--------+--------+--------+

| State | [0, 0] | [0, 1] | [1, 0] | [1, 1] |

+-------+--------+--------+--------+--------+

|   3   |   1    |   1    |   1    |   0    |

|   1   |   0    |   0    |   0    |   -1   |

|   0   |   0    |   -1   |   -1   |   -1   |

|   -1  |   -1   |   -1   |   -1   |   -2   |

|   -2  |   -1   |   -2   |   -2   |   -2   |

+-------+--------+--------+--------+--------+
Initial State:  3

Final State:  [3, 1, 0]

Table for  And(x1 + 2*x2 == 4, x1 + x2 <= 3)

+---------------+---------------+---------------+---------------+---------------+

|     State     |     [0, 0]    |     [0, 1]    |     [1, 0]    |     [1, 1]    |

+---------------+---------------+---------------+---------------+---------------+

|   ['4', '3']  |   ['2', '1']  |   ['1', '1']  |  ['Err', '1'] |  ['Err', '0'] |

|   ['2', '1']  |   ['1', '0']  |   ['0', '0']  |  ['Err', '0'] | ['Err', '-1'] |

|   ['1', '1']  |  ['Err', '0'] |  ['Err', '0'] |   ['0', '0']  |  ['-1', '-1'] |

|  ['Err', '1'] |  ['Err', '0'] |  ['Err', '0'] |  ['Err', '0'] | ['Err', '-1'] |

|  ['Err', '0'] |  ['Err', '0'] | ['Err', '-1'] | ['Err', '-1'] | ['Err', '-1'] |

|   ['1', '0']  |  ['Err', '0'] | ['Err', '-1'] |  ['0', '-1']  |  ['-1', '-1'] |

|   ['0', '0']  |   ['0', '0']  |  ['-1', '-1'] | ['Err', '-1'] | ['Err', '-1'] |

| ['Err', '-1'] | ['Err', '-1'] | ['Err', '-1'] | ['Err', '-1'] | ['Err', '-2'] |

|  ['-1', '-1'] | ['Err', '-1'] | ['Err', '-1'] |  ['-1', '-1'] |  ['-2', '-2'] |

|  ['0', '-1']  |  ['0', '-1']  |  ['-1', '-1'] | ['Err', '-1'] | ['Err', '-2'] |

| ['Err', '-2'] | ['Err', '-1'] | ['Err', '-2'] | ['Err', '-2'] | ['Err', '-2'] |

|  ['-2', '-2'] |  ['-1', '-1'] |  ['-2', '-2'] | ['Err', '-2'] | ['Err', '-2'] |

+---------------+---------------+---------------+---------------+---------------+

Initial State:  ['4', '3']

Final State:  [['0', '0']]
For:
{x1: 1, x2: 1}

And(x1 + 2*x2 == 4, x1 + x2 <= 3) is False
