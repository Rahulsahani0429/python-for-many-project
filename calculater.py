print(
    '''
+ ADDITION
- SUBTRACTION
* MULTIPLICATION
\ DIVISION '''
)
num1=int(input('enter the num1:-'))
num2=int(input('enter the num2:-'))
operater=input('enter the operater:-')
if operater=='+':
   print(num1+num2)
elif operater=='-':
   print(num1-num2)
elif operater=='*':
   print(num1*num2)
elif operater=='/':
   print(num1/num2)
else:
   print('invailied operator')


   

