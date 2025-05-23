# --- Bank Specific Calculator CLI App ---

def format_inr(amount):
    """
    Formats a number with commas in Indian style (e.g., 1,23,456.78)
    and adds the Rupee symbol (₹) at the beginning for currency display.
    """
    s = f"{amount:,.2f}"
    parts = s.split(".")
    integer_part = parts[0].replace(",", "")

    # Apply Indian numbering system rules for placing commas
    if len(integer_part) > 3:
        last_three = integer_part[-3:]
        rest = integer_part[:-3]
        rest_with_commas = ""
        while len(rest) > 2:
            rest_with_commas = "," + rest[-2:] + rest_with_commas
            rest = rest[:-2]
        integer_part = rest + rest_with_commas + "," + last_three
    
    return "₹" + integer_part + "." + parts[1]

# --- ORIGINAL Loan Calculation Function (now provides summary) ---

def calculate_loan_summary():
    """
    Calculates loan amortization using the reducing balance method and provides a summary.
    This is the original loan calculation behavior.
    """
    print("\n--- Loan Calculator (Reducing Balance Method Summary) ---")
    
    while True:
        try:
            loan_amount_str = input("Enter Loan Amount (e.g., 500000): ")
            loan_amount = float(loan_amount_str.replace(',', ''))
            if loan_amount <= 0:
                raise ValueError("Loan amount must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number.")

    while True:
        try:
            term_months_str = input("Enter Loan Term in Months (e.g., 60): ")
            term_months = int(term_months_str)
            if term_months <= 0:
                raise ValueError("Term must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive whole number.")

    while True:
        try:
            annual_rate_str = input("Enter Annual Interest Rate in % (e.g., 9.5): ")
            annual_rate = float(annual_rate_str)
            if annual_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative number.")

    principal_per_month = loan_amount / term_months
    current_balance = loan_amount
    monthly_rate = annual_rate / 100 / 12

    total_interest_paid = 0
    total_principal_paid = 0
    total_payments = 0

    # This part is primarily for calculating totals without printing a full table
    for i in range(1, term_months + 1):
        interest_this_month = current_balance * monthly_rate
        emi_this_month = principal_per_month + interest_this_month
        
        current_balance -= principal_per_month
        if current_balance < 0.01:
            current_balance = 0.0

        total_interest_paid += interest_this_month
        total_principal_paid += principal_per_month
        total_payments += emi_this_month
    
    print("-" * 30)
    print(f"\nSummary for Loan:")
    print(f"Loan Amount: {format_inr(loan_amount)}")
    print(f"Loan Term: {term_months} months")
    print(f"Annual Interest Rate: {annual_rate}%")
    print(f"Fixed Principal per month: {format_inr(principal_per_month)}")
    print(f"Total Interest Paid: {format_inr(total_interest_paid)}")
    print(f"Total Amount Paid (Principal + Interest): {format_inr(total_payments)}")
    print("-" * 30)

# --- NEW Loan Repayment Table Function (Your Provided Code) ---

def calculate_loan_repayment_table():
    """
    Calculates loan amortization and prints a detailed monthly repayment schedule.
    This function uses the reducing balance method with fixed principal per installment.
    """
    print("\n--- Loan Repayment Schedule Table ---")

    while True:
        try:
            loan_amount_str = input("Enter Loan Amount: ")
            loan_amount = float(loan_amount_str.replace(',', ''))
            if loan_amount <= 0:
                raise ValueError("Loan amount must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number.")

    while True:
        try:
            term_months_str = input("Enter Term (months): ")
            term_months = int(term_months_str)
            if term_months <= 0:
                raise ValueError("Term must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive whole number.")

    while True:
        try:
            annual_rate_str = input("Enter Annual Interest Rate (%): ")
            annual_rate = float(annual_rate_str)
            if annual_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative number.")

    principal_per_installment = loan_amount / term_months
    balance = loan_amount
    monthly_rate = annual_rate / 100 / 12

    print("\n--- Monthly Repayment Details ---")
    print(f"{'Month':<7}{'Principal':>16}{'Interest':>15}{'Total EMI':>15}{'Balance':>16}")
    print("-" * 69)

    total_principal_paid = 0
    total_interest_paid = 0
    total_payment_made = 0

    for i in range(1, term_months + 1):
        interest = balance * monthly_rate
        total = principal_per_installment + interest
        balance -= principal_per_installment
        
        if balance < 0.01: # Use a small epsilon for floating point comparison
            balance = 0.0

        principal_rounded = round(principal_per_installment, 2)
        interest_rounded = round(interest, 2)
        total_rounded = round(total, 2)
        balance_rounded = round(balance, 2)

        print(f"{i:<7}{format_inr(principal_rounded):>16}{format_inr(interest_rounded):>15}{format_inr(total_rounded):>15}{format_inr(balance_rounded):>16}")

        total_principal_paid += principal_rounded
        total_interest_paid += interest_rounded
        total_payment_made += total_rounded

    print("-" * 69)
    print(f"{'Total':<7}{format_inr(total_principal_paid):>16}{format_inr(total_interest_paid):>15}{format_inr(total_payment_made):>15}{'':>16}")
    print("---------------------------------\n")


# --- Fixed Deposit (FD) Calculation Function ---

def calculate_fd_interest():
    """
    Calculates Fixed Deposit interest based on chosen type:
    1. Interest added with FD on maturity (simple interest).
    2. Monthly interest transferred to savings account.
    """
    print("\n--- Fixed Deposit (FD) Interest Calculator ---")
    
    while True:
        try:
            principal_str = input("Enter FD Principal Amount (e.g., 100000): ")
            principal = float(principal_str.replace(',', ''))
            if principal <= 0:
                raise ValueError("Principal amount must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number.")

    while True:
        try:
            annual_rate_str = input("Enter Annual Interest Rate in % (e.g., 7.0): ")
            annual_rate = float(annual_rate_str)
            if annual_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative number.")

    while True:
        try:
            tenure_months_str = input("Enter FD Tenure in Months (e.g., 36 for 3 years): ")
            tenure_months = int(tenure_months_str)
            if tenure_months <= 0:
                raise ValueError("Tenure must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive whole number.")
            
    while True:
        print("\nSelect FD Type:")
        print("1. Interest added with FD on maturity")
        print("2. Monthly interest transferred to savings account")
        fd_type_choice = input("Enter choice (1/2): ")
        
        if fd_type_choice in ['1', '2']:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

    total_interest_earned = 0
    maturity_amount = 0

    if fd_type_choice == '1':
        print("\n--- Calculating for Interest Added on Maturity ---")
        
        r = annual_rate / 100
        t = tenure_months / 12
        
        total_interest_earned = principal * r * t
        maturity_amount = principal + total_interest_earned

        print(f"\nFD Type: Interest added with FD on maturity")
        print(f"Total Interest Earned (at maturity): {format_inr(total_interest_earned)}")
        print(f"Maturity Amount: {format_inr(maturity_amount)}")

    elif fd_type_choice == '2':
        print("\n--- Calculating for Monthly Interest Payout ---")
        
        monthly_rate = annual_rate / 100 / 12
        
        interest_per_month = principal * monthly_rate
        total_interest_earned = interest_per_month * tenure_months
        maturity_amount = principal

        print(f"\nFD Type: Monthly interest transferred to savings account")
        print(f"Principal Amount: {format_inr(principal)}")
        print(f"Interest Transferred Monthly: {format_inr(interest_per_month)}")
        print(f"Total Interest Earned Over {tenure_months} months: {format_inr(total_interest_earned)}")
        print(f"Amount Received at Maturity (Principal): {format_inr(maturity_amount)}")

    print(f"\nFD Principal Amount: {format_inr(principal)}")
    print(f"Annual Interest Rate: {annual_rate}%")
    print(f"Tenure: {tenure_months} months")
    print("-" * 30)

# --- Main Application Logic ---

def main():
    """
    The main function that runs the Cooperative Bank Calculator application.
    It displays a menu and calls the appropriate calculation function based on user choice.
    """
    while True:
        print("\n--- Welcome to the Cooperative Bank Calculator! ---")
        print("1. Loan Calculator (Summary)")
        print("2. Loan Repayment Schedule Table") # New option for your provided loan function
        print("3. Fixed Deposit (FD) Interest Calculator")
        print("4. Exit") # Exit option shifted to 4
        
        choice = input("Enter your choice: ")

        if choice == '1':
            calculate_loan_summary() # Calls the original loan calculator (now summary)
        elif choice == '2':
            calculate_loan_repayment_table() # Calls your new loan repayment table function
        elif choice == '3':
            calculate_fd_interest()
        elif choice == '4': # Exit is now 4
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.") # Updated range

if __name__ == "__main__":
    main()
