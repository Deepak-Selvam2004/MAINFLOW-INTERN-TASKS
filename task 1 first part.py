#IMPLEMENTATION OF FIRST HALF PART OF THE TASK-1
class MainFlow():
#IMPLEMENTATION OF ARITHMETIC OPERATIONS
    def calculate(self,x,y):
        sum=x+y
        print("SUM : ",sum)
        diff=x-y
        print("DIFFERENCE : ",diff)
        mul=x*y
        print("MULTIPLIED : ",mul)
        div=x/y
        print("DIVIDED : ",div)
        print("----------------------------------------------------")
#IMPLEMENTATION OF CONDITIONAL STATEMENTS        
    def check(self,num):
        if num%2==0:
            print(num,"IS AN EVEN NUMBER")
        else:
            print(num,"IS AN ODD NUMBER")
        print("----------------------------------------------------")
#IMPLEMENTATION OF STRING MANIPULATION
    def palindrome(self,pali):
        s2=''
        index=-1
        for i in pali:
            s2+=pali[index]
            index-=1
        print('THE GIVEN STRING : {}\nTHE REVERSED STRING : {}'.format(pali,s2))
        if(pali==s2):
            print("THE GIVEN STRING IS A PALINDROME!!!")
        else:
            print("THE GIVEN STRING IS NOT A PALINDROME!!!")
        print("----------------------------------------------------")
#DISPLAY OF ALL INPUTS & OUTPUTS
mf=MainFlow()
print("\t","\t","***  ARITHMETIC CALCULATOR   ***", "\t","\t")
print("-------------------------------------------------------")
x=int(input("ENTER THE FIRST NUMBER : "))
y=int(input("ENTER THE SECOND NUMBER : "))
mf.calculate(x,y)
print("\t","\t","***  ODD/EVEN NUMBER CHECKER   ***", "\t","\t")
print("-------------------------------------------------------")
num=int(input("ENTER A NUMBER TO CHECK FOR ITS TYPE : "))
mf.check(num)
print("\t","\t","***  PALINDROME DISPLAY   ***", "\t","\t")
print("-------------------------------------------------------")
pali=input("ENTER A STRING TO CHECK FOR PALINDROME : ")
mf.palindrome(pali)