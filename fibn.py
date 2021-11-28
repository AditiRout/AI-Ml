#use of command line interface creation
#-h is already inbuilt
#no need to use the run code command here
import argparse

def fib(n):
    a,b=0,1
    
    for i in range(n-1):
        
        a,b=b,a+b

    return a


pars=argparse.ArgumentParser()
    #this is positional arguement which is important
pars.add_argument("num",help="The fibonacci number you wish",type=int)
    #this is optional arguement
pars.add_argument("-o","--output",help="output is here",action="store_true")
args=pars.parse_args()
result= fib(args.num)
print("the answer is "+str(result))
if args.output:
    f=open("fibo.txt","a")
    f.write(str(result)) 
    

