'''###PATTERN
1
for row in range(1,5):
    for col in range(1,5):
        print(col,end=" ")
    print( )
    
#output:
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 

##2
for  row in range(1,5):
    for col in range(5, 0,-1):
        print(col,end=" ")
    print()

#output:
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1


##3

for i in range(0, 5):
    for j in range(1, i+1):
        print(j, end=' ')
    print("\r")

    
1 

1 2 

1 2 3 

1 2 3 4 


##4



for i in range(0, 7):
    for j in range(0, i+1):
        print(j, end=' ')
        
    print("\r")

#output
0 

0 1 

0 1 2 

0 1 2 3 

0 1 2 3 4 

0 1 2 3 4 5 

0 1 2 3 4 5 6 


##5

for i in range(1, 7):
    for j in range(1,1+i):
        print(i, end=' ')
    print("\r")


1 

2 2 

3 3 3 

4 4 4 4 

5 5 5 5 5 

6 6 6 6 6 6 


##6

for  row in range(1,5):
    for col in range(5,0,-1):
        col+=row
        print('col',end=" ")
    print()



#output:
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 


##7

for  row in range(5,0,-1):
    for col in range(5,0,-1):
        col+=row
        print(row,end=" ")
    print()

5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1 

##8


for  row in range(1,5):
    for col in range(5,0,-1):
        col+=row
        print('*',end=" ")
    print()

* * * * * 
* * * * * 
* * * * * 
* * * * * 


##9

for i in range(1,8):
    for j in range(1,i):
        i+=j
        print(j,end=" ")
    print()

#output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 


##10'''
'''
for i in range(1, 4):
    for j in range(1,11):
        print(i ,'*', j ,'=',i*j)
    print()


#output:




    1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30'''

print("hellow world++++++++++++++++++++++++++")