###################### Function to create the table in the database ######################

# Create a function that calculates the letter grade
def calculate_grade(number_grade):
    if number_grade >= 90:
        letter_grade = "A"
    elif number_grade >= 80:
        letter_grade = "B"
    elif number_grade >= 70:
        letter_grade = "C"
    elif number_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


def calculate_number_of_payments(term_years):
    """
    Calculate the total number of monthly payments based on the loan term in years.

    Parameters:
        term_years (int): The loan term in years.

    Returns:
        int: The total number of monthly payments.
    """
    return term_years * 12


def calculate_monthly_payment(loan_amount, interest_rate, term_years):
    """
    Calculate the monthly payment for a loan using the amortization formula.

    Parameters:
        loan_amount (float): The total loan amount.
        interest_rate (float): The annual interest rate as a percentage (e.g., 5.0 for 5%).
        term_years (int): The loan term in years.

    Returns:
        float: The monthly payment amount.
    """
    loan_term_months = calculate_number_of_payments(term_years)
    monthly_interest_rate = interest_rate / 12 / 100

    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term_months))
    else:
        monthly_payment = loan_amount / loan_term_months  # Handle the no-interest case

    return monthly_payment


def generate_amortization_schedule(loan_amount, interest_rate, term_years):
    """
    Generate a loan amortization schedule.

    Parameters:
        loan_amount (float): The total loan amount.
        interest_rate (float): The annual interest rate as a percentage.
        term_years (int): The loan term in years.

    Returns:
        list of dict: A list of dictionaries, each representing the details for one month.
    """
    loan_term_months = calculate_number_of_payments(term_years)
    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, term_years)
    monthly_interest_rate = interest_rate / 12 / 100
    loan_amortization_list = []

    for month in range(1, loan_term_months + 1):
        interest_paid = loan_amount * monthly_interest_rate
        principal_paid = monthly_payment - interest_paid
        remaining_balance = loan_amount - principal_paid

        loan_amortization_list.append({
            'month': month,
            'starting_balance': loan_amount,
            'interest_paid': round(interest_paid, 2),
            'principal_paid': round(principal_paid, 2),
            'monthly_payment': round(monthly_payment, 2),
            'remaining_balance': round(remaining_balance, 2)
        })

        loan_amount = remaining_balance  # Update loan balance for next month

    return loan_amortization_list
