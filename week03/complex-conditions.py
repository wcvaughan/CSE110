# Write a program to determine whether to loan money based on the following rules.

# First, ask for a rating from 1–10 on the following:

# How large is the loan?

print('Please answer all questions using whole numbers on a scale from 1-10.')

loan_size = int(input('How large is the loan?'))

# How good is your credit history?

credit_history = int(input('How good is your credit history?'))

# How high is your income?

income = int(input('How high is your income?'))

# How large is your down payment?

down_payment = int(input('How large is your down payment?'))

# First, check if the loan size is at least 5. If it is, use the following rules:
    
# If the credit history and income are both at least 7, then the decision is "yes"

# If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"

# Otherwise (if neither the credit history nor income is at least 7), the decision is "no"

# Otherwise (if the loan is not 5 or greater), use these rules:

# If the credit is less than 4, then the decision is "no"

# Otherwise, check the following:

# If either the income or the down payment is at least 7, the decision is "yes"

# If both the income and the down payment are at least 4, then the answer is "yes"

# Otherwise, the decision is "no"

# Finally, display the decision to the user.
loan_approval = True

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        loan_approval = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            loan_approval = True
        else:
            loan_approval = False
    else:
        loan_approval = False
else:
    if credit_history < 4:
        loan_approval = False
    else:
        if income >= 7 or down_payment >= 7:
            loan_approval = True
        elif income >=4 and down_payment >= 4:
            loan_approval = True
        else:
            loan_approval = False
if loan_approval:
    print('Loan approved!')
else:
    print('Loan denied :(')

# Verify that your program works correctly by following each step in this testing procedure:

# Test your program with these values and ensure you arrive at the decision indicated:

# Loan size: 8, Credit: 7, Income: 8, Down Payment: 1, Decision: "yes"

# Loan size: 5, Credit: 2, Income: 7, Down Payment: 5, Decision: "yes"

# Loan size: 8, Credit: 2, Income: 8, Down Payment: 3, Decision: "no"

# Loan size: 2, Credit: 4, Income: 1, Down Payment: 7, Decision: "yes"

# Loan size: 4, Credit: 5, Income: 5, Down Payment: 3, Decision: "no"