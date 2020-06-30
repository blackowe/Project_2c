cents = int(input("Please enter an amount in cents less than a dollar.\n")) # userinput stored in 'cents' var.
print("Your change will be:")   # return prompt
print("Q:",cents//25)   # number of whole quarters derived from input value
cents = cents%25        # reassigns cents var to value excluding whole quarter
print("D:",cents//10)   # number of whole dimes derived from new total
cents = cents%10        # reassignment of cents var excluding whole dimes
print("N:",cents//5)    # number of whole nickels derived from new total
cents = cents%5         # reassignment of cents var excluding whole nickels
print("P:",cents//1)    # number of whole pennies derived from new total






