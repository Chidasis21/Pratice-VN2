'''
#
from operation import divop 
import kvr 
x=int(input("Enter First Value:")) 
y=int(input("Enter Second Value:")) 
try: 
    result=divop(x,y) 
except kvr.KvDivisionError: 
    print("\nDon't Enter Zero for Den...") 
else: 
    print("\nDiv=",result) 
finally: 
    print("\nI am from finally block")
#
from operation import divop 
import kvr 
x=int(input("Enter First Value:")) 
y=int(input("Enter Second Value:")) 
try: 
    result=divop(x,y) 
except kvr.KvDivisionError:
    print("\nDon't Enter Zero for Den...") 
else: 
    print("\nDiv=",result) 
finally:
    print("\nI am from finally block")'''
#'''
class DepositError(BaseException):pass
class WithdrawError(Exception):pass
class InSufficientFund(Exception):pass
def menu():
    print("-"*40)
    print("\tATM Operation")
    print("_"*40)
    print("\t1.Deposit:")
    print("\t2.Withdraw")
    print("\t.Bal Inq")
    print("\t.Exit")
    print("-"*40)
from atmmenu import menu
from armexcept import DepositError,WithError,InSufficientFundError
from atmoperation import*
while(True):
    menu()
    try:
        ch = int(input("Enter your choice:"))
        match ch:
            case 1:
                try:
                    deposit()
                except ValueError:

                    print("Don't try to deposit strs/symblos/alpha-numeric")
                except DepositError:
                    print("Don't try to deposit -ve/zero values:")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("Don't try to withdraw strs/symblos/aplha-numeric")
                except InSufficientFUndError:
                    print("\nU don't have a sufficienterror:")
            case 3:
                balanq()
from atmexcept import DepositError, WithdrawError, InSufficientFundError
bal = 500.00
def deposit():
    damt = float(input("\n Enter how much amount you want to deposit:"))
    if(damt<=0):
        raise DepositError
    else:
        Global bal
        bal = bal+damt
        print("\nUr Account 20244518221 credeted with INR:{}".format(damt))
        print("Now ur current balance :()".format(bal))
def withdraw:
    Global bal
    wamt= float(input("\n Enter how much amount you want to Withdraw:"))
    if(wamt<=0):
        raise WithdrawError
    else:
        if(wamt+500>bal):
            raise InSufficientFUndError
        else:
            bal = bal-wamt
            print("Now your current balance :{}".format(wamt))
            print("your curent balance :{}".format(bal))
def balanq():
    print("your current balance:{}",format(bal))
case 4:
    print("\n Thanks for using this Application:")
    exit()
    case_:
    print("n\Your selection of operation is wrong:")
    except ValueError:
        print("\n Don't enter strs/symblos/alpha-numeric for your choice:")'''
#
