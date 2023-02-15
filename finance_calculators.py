'''
================================ PSEUDOCODE START =============================================
THIS IS FOR A PROGRAM TO CALCULATE FINANCIAL INTEREST
THE USER IS GIVEN 2 OPTIONS; INVESTMENT OF BOND(UK-'MORTGAGE/UNSECURED HOUSE LOAN')
DEPENDING ON THE USER'S CHOICE OF THE 2 ABOVE OPTIONS, THEN THE PROGRAM GOES INTO 2 DIRECTIONS, PERFORMS CALCULATIONS, OUTPUTS A FIGURE TO USER
FOR THE INVESTMENT CHOICE THERE IS ANOTHER OPTION TO CHOOSE SIMPLE/COMPOUND INTEREST

1. import math
2. create variables for; 'investment' & 'bond', 'simple' & 'compound' interest payment
 
3. create input for the user to choose investment or bond using f-string, based on instructions given, the user types a word to choose: no 'Y/N' selection permitted
4. use lower() to make the input uniform, so output is independent of the user's typed-format
5. if user chooses investment then there needs to be: if/else statement
5.  [i] there needs to be a hurdle for the user to cross to get to the next stage, ... 
            ... a hurdle based on making a valid selection & printing an !alert! if no valid selection is made
    [ii] there needs to be an error message to request the user to restart the program and try again, with care on the type of input
    [iii] else, this breaks out & if user chooses 'investment' then there will be a new f-string input for user to choose 'simple' or 'compound' interest
6. Create 2-major splits in code between INVESTMENT & BOND
7. INVESTMENT comes first since it is more complex, with more options
8. I am unsure how to plan the code. Try it and see....
================================== PSEUDOCODE END =============================================
'''
import math

# THIS CODE BLOCK TAKES IN THE USER'S INPUT TO INITIALLY SPLIT THE PATH IN 2 DIRECTIONS; EITHER 'INVESTMENT' OR 'BOND'
usr_want_inv = ("INVESTMENT")
usr_want_bnd = ("BOND")
usr_choice_inv_or_bnd = input(f"""\nChoose either '{usr_want_inv}' or '{usr_want_bnd}' from the menu below to proceed:\n 
\n  investment - to calculate the amount of interest that you will earn on your investment
\n  bond       - to calculate the amount you will have to pay on you home loan\n
  type in your choice here : """)
usr_choice_inv_or_bnd = usr_choice_inv_or_bnd.lower()

# THIS CODE BLOCK if/elif/else SIEVES THE USER'S INITIAL CHOICE INTO 3 PATHWAYS
if usr_choice_inv_or_bnd == "investment" :
    print("\nThank you choosing the INVESTMENT calculaton")
elif usr_choice_inv_or_bnd == "bond" :
    print("\nThank you choosing the BOND calculaton")
else :
    print("\n!!! ALERT !!! You may have mistyped your selection. Please restart the program and try again. Please check your spelling of INVESTMENT or BOND.")

# THIS CODE TAKES THE USER THROUGH A SERIES OF 'INVESTMENT' OPTIONS. NUMBERS float().
if usr_choice_inv_or_bnd == "investment" :
    
    inv_amount = input("\nHow much money would you like to invest : ")
    inv_amount = float(inv_amount)

    inv_intrst_rate = input("\nHow much interest are you recieving on your investment :  ")
    inv_intrst_rate = float(inv_intrst_rate)
    
    inv_time = input("\nHow many years would you like to invest for : ")
    inv_time = float(inv_time)

# THIS CODE TAKES THE USER'S CHOICE OF 'SIMPLE'/COMPOUND INTEREST
    inv_int_simple = ("SIMPLE")
    inv_int_compound = ("COMPOUND")
    inv_choice_simp_or_comp = input(f"\nWould you like {inv_int_simple} OR {inv_int_compound} interest :  ")
    inv_choice_simp_or_comp = inv_choice_simp_or_comp.lower()
    
# THIS ASSIGNS THE USERS CHOICE OF 'SIMPLE'/'COMPOUND' INTEREST TO A NEW VARIABLE CALLED 'INTEREST' WHICH HAS A SHORTER NAME
    interest = str()
    if inv_choice_simp_or_comp == "simple" :
        interest = "simple"    
    if inv_choice_simp_or_comp == "compound" :
        interest = "compound"

# THIS IS AN if/elif BLOCK TO 'SWITCH' DIRECTION BETWEEN 'SIMPLE'/'COMPOUND' INTEREST                 
    if interest == "simple" :
       
        inv_int_payout = (inv_amount) * (1 + (inv_intrst_rate) * (inv_time))
        inv_int_payout = float(inv_int_payout)
        inv_int_payout = round(inv_int_payout, 2)
        print(f"\nThis is the amount you should receive at the end of your INVESTMENT : R {inv_int_payout} with SIMPLE interest \n")

    elif interest == "compound" :
        
        inv_int_payout = (inv_amount) * math.pow((1 + inv_intrst_rate), inv_time)
        inv_int_payout = float(inv_int_payout)
        inv_int_payout = round(inv_int_payout, 2)
        print(f"\nThis is the amount you should receive at the end of your INVESTMENT : R {inv_int_payout} with COMPOUND interest \n")

# THIS CODE TAKES THE USER THROUGH A SERIES OF 'BOND' OPTIONS. NUMBERS float().
if usr_choice_inv_or_bnd == "bond" :
            
            bnd_amount = input("\nHow much would you like to borrow for your house : ")
            bnd_amount = float(bnd_amount)       
            
            bnd_intrst_rate = input("\nHow much is the annual interest rate on your bond :  ")
            bnd_intrst_rate = float(bnd_intrst_rate)   

            bnd_term_mnths = input("\nOver how many months do you wish to borrow : ")
            bnd_term_mnths = float(bnd_term_mnths)

# BOND MONTHLY REPAYMENT, VARIABLES REASSIGNED TO ALIGN WITH :(repayment formula) = (i.P)/(1 - (1+i)^(-n))
            P = bnd_amount
            i = ((bnd_intrst_rate/12)/100)
            n = bnd_term_mnths
            e = i + 1     # THIS VARIABLE: (e), WAS CREATED TO USE math.pow(), IT REPLACES: (1+i)

            bnd_repay_pr_month = (i*P) / (1-math.pow(e,-n))

            bnd_repay_pr_month = round(bnd_repay_pr_month, 2)

            print((f"\nThis is the amount you repay per month for the BOND : R {bnd_repay_pr_month} \n"))

#   CODE ENDS    ********************************************************************************************************

'''
================================ START OF TASK INSTRUCTIONS =============================================

For this task, assume that you have been approached by a small financial company and asked to create a program that allows the user to access two
different financial calculators: an investment calculator and a home loan repayment calculator.

    ● Create a new Python file in this folder called finance_calculators.py.
    ● At the top of the file include the line import math
    ● Write the code that will do the following:

        1. The user should be allowed to choose which calculation they want to do. The first output that the user sees when the program runs
            should look like this :



How the user capitalises their selection should not affect how the program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’,
‘Investment’, ‘INVESTMENT’, etc., should all be recognised as valid entries. If the user doesn’t type in a valid input, show an appropriate
error message.

2. If the user selects ‘investment’, do the following:

    ■ Ask the user to input:
        ● The amount of money that they are depositing.
        ● The interest rate (as a percentage). Only the number of the interest rate should be entered — don’t worry
            about having to deal with the added ‘%’, e.g. The user should enter 8 and not 8%.
        ● The number of years they plan on investing.
        ● Then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called
            interest. Depending on whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period,
            at the specified interest rate. Look below for the formula to be used:

    Interest formula:

    The total amount when simple interest is applied is calculated as follows: A = P(1 + r * t)
    
    The Python equivalent is very similar: A =P*(1+r*t)

    The total amount when compound interest is applied is calculated as follows: A = P(1 + r) ^ t

    The Python equivalent is slightly different: A = P* math.pow((1+r),t)

    In the formulae above:
        ● ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
        ● ‘P’ is the amount that the user deposits.
        ● ‘t’ is the number of years that the money is being invested.
        ● ‘A’ is the total amount once the interest has been applied.

    ■ Print out the answer!
    ■ Try entering 20 years and 8 (%) and see what the difference is depending on the type of interest rate!
3. If the user selects ‘bond’, do the following:
    ■ Ask the user to input:
        ● The present value of the house. e.g. 100000
        ● The interest rate. e.g. 7
        ● The number of months they plan to take to repay the bond. e.g. 120

Bond repayment formula:

    The amount that a person will have to be repaid on a home loan each month is calculated as follows: repayment = x = (i.P)/(1 - (1+i)^(-n))

    In the formula above:

        ● ‘P’ is the present value of the house.
        ● ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12.
        ● ‘n’ is the number of months over which the bond will be repaid.

■ Calculate how much money the user will have to repay each month and output the answer.

================================ START OF TASK INSTRUCTIONS =============================================
'''