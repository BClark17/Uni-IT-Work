"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = 1
while float(sales) >=0:
    sales = float(input("Enter Sales Figure: $"))
    if sales >= 1000:
        bonus = sales*0.15
        print ("Your Bonus off Sales figures is: $",bonus)
    elif sales < 1000 and sales > 0:
        bonus = sales * 0.1
        print ("Your Bonus off Sales figures is: $",bonus)
    else:
        print ("Please Enter a Valid Number")