from datetime import datetime, timedelta
import calendar  # Added for accurate monthly date increments

# --- Bank Specific Calculator CLI App ---


def format_inr(amount: float) -> str:
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


# --- Loan Calculator (Summary & Optional Repayment Table) ---


def calculate_loan_summary_and_table() -> None:
    """
    Calculates loan amortization using the reducing balance method, provides a summary,
    and optionally prints a detailed monthly repayment schedule.
    """
    print("\n--- Loan Calculator (Reducing Balance Method) ---")

    while True:
        try:
            loan_amount_str = input("Enter Loan Amount: ")  # Removed example
            loan_amount = float(loan_amount_str.replace(",", ""))
            if loan_amount <= 0:
                raise ValueError("Loan amount must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number.")

    while True:
        try:
            term_months_str = input(
                "Enter Loan Term (in months): "
            )  # Simplified prompt
            term_months = int(term_months_str)
            if term_months <= 0:
                raise ValueError("Term must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive whole number.")

    while True:
        try:
            annual_rate_str = input(
                "Enter Annual Interest Rate (%): "
            )  # Simplified prompt
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

    # Ask if user wants to see the detailed repayment schedule
    while True:
        show_table = (
            input(
                "\nDo you want to see the detailed repayment schedule table? (yes/no): "
            )
            .strip()
            .lower()
        )
        if show_table in ["yes", "y"]:
            # Pass the already obtained values to the table function
            calculate_loan_repayment_table(loan_amount, term_months, annual_rate)
            break
        elif show_table in ["no", "n"]:
            print("Repayment schedule not displayed.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


# --- Loan Repayment Table Function (Modified to accept parameters) ---


def calculate_loan_repayment_table(
    loan_amount: float, term_months: int, annual_rate: float
) -> None:
    """
    Calculates loan amortization and prints a detailed monthly repayment schedule.
    This function uses the reducing balance method with fixed principal per installment.
    It now accepts loan details as parameters.
    """
    print("\n--- Detailed Loan Repayment Schedule Table ---")

    principal_per_installment = loan_amount / term_months
    balance = loan_amount
    monthly_rate = annual_rate / 100 / 12

    print("\n--- Monthly Repayment Details ---")
    # Adjusted spacing and removed |
    print(
        f"{'Month':<7}{'Principal':>18}{'Interest':>18}{'Total EMI':>18}{'Balance':>18}"
    )
    print("-" * 79)

    total_principal_paid_table = 0
    total_interest_paid_table = 0
    total_payment_made_table = 0

    for i in range(1, term_months + 1):
        interest = balance * monthly_rate
        total = principal_per_installment + interest
        balance -= principal_per_installment

        if balance < 0.01:
            balance = 0.0

        principal_rounded = round(principal_per_installment, 2)
        interest_rounded = round(interest, 2)
        total_rounded = round(total, 2)
        balance_rounded = round(balance, 2)

        # Adjusted spacing and removed |
        print(
            f"{i:<7}{format_inr(principal_rounded):>18}{format_inr(interest_rounded):>18}{format_inr(total_rounded):>18}{format_inr(balance_rounded):>18}"
        )

        total_principal_paid_table += principal_rounded
        total_interest_paid_table += interest_rounded
        total_payment_made_table += total_rounded

    print("-" * 79)
    # Adjusted spacing and removed |
    print(
        f"{'Total':<7}{format_inr(total_principal_paid_table):>18}{format_inr(total_interest_paid_table):>18}{format_inr(total_payment_made_table):>18}{'':>18}"
    )
    print("---------------------------------\n")


# --- Fixed Deposit (FD) Calculation Function ---


def calculate_fd_interest() -> None:
    """
    Calculates Fixed Deposit interest based on chosen type:
    1. Interest added with FD on maturity (simple interest).
    2. Monthly interest transferred to savings account.
    """
    print("\n--- Fixed Deposit (FD) Interest Calculator ---")

    while True:
        try:
            principal_str = input("Enter FD Principal Amount: ")  # Removed example
            principal = float(principal_str.replace(",", ""))
            if principal <= 0:
                raise ValueError("Principal amount must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number.")

    while True:
        try:
            annual_rate_str = input(
                "Enter Annual Interest Rate (%): "
            )  # Simplified prompt
            annual_rate = float(annual_rate_str)
            if annual_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative number.")

    while True:
        try:
            tenure_months_str = input(
                "Enter FD Tenure (in months): "
            )  # Simplified prompt
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

        if fd_type_choice in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

    total_interest_earned = 0
    maturity_amount = 0

    if fd_type_choice == "1":
        print("\n--- Calculating for Interest Added on Maturity ---")

        r = annual_rate / 100
        t = tenure_months / 12

        total_interest_earned = principal * r * t
        maturity_amount = principal + total_interest_earned

        print(f"\nFD Type: Interest added with FD on maturity")
        print(
            f"Total Interest Earned (at maturity): {format_inr(total_interest_earned)}"
        )
        print(f"Maturity Amount: {format_inr(maturity_amount)}")

    elif fd_type_choice == "2":
        print("\n--- Calculating for Monthly Interest Payout ---")

        monthly_rate = annual_rate / 100 / 12

        interest_per_month = principal * monthly_rate
        total_interest_earned = interest_per_month * tenure_months
        maturity_amount = principal  # At maturity, only principal is returned as interest was paid out

        print(f"\nFD Type: Monthly interest transferred to savings account")
        print(f"Principal Amount: {format_inr(principal)}")
        print(f"Interest Transferred Monthly: {format_inr(interest_per_month)}")
        print(
            f"Total Interest Earned Over {tenure_months} months: {format_inr(total_interest_earned)}"
        )
        print(f"Amount Received at Maturity (Principal): {format_inr(maturity_amount)}")

    print(f"\nFD Principal Amount: {format_inr(principal)}")
    print(f"Annual Interest Rate: {annual_rate}%")
    print(f"Tenure: {tenure_months} months")
    print("-" * 30)


# --- Interest Between Dates Calculator ---


def calculate_interest_between_dates() -> None:
    """
    Calculates the interest accrued between two given dates.
    """
    print("\n--- Interest Between Dates Calculator ---")

    while True:
        try:
            date_format = "%d-%m-%Y"  # Changed to DD-MM-YYYY
            start_date_str = input(
                "Enter the first date (DD-MM-YYYY): "
            )  # Changed prompt
            start_date = datetime.strptime(start_date_str, date_format).date()
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    while True:
        try:
            date_format = "%d-%m-%Y"  # Changed to DD-MM-YYYY
            end_date_str = input(
                "Enter the second date (DD-MM-YYYY): "
            )  # Changed prompt
            end_date = datetime.strptime(end_date_str, date_format).date()
            if end_date < start_date:
                raise ValueError("End date cannot be before the start date.")
            break
        except ValueError as e:
            print(
                f"Invalid date format or date order: {e}. Please use DD-MM-YYYY and ensure the end date is after the start date."
            )

    while True:
        try:
            balance_str = input("Enter the balance: ")  # Removed example
            balance = float(balance_str.replace(",", ""))
            if balance < 0:
                raise ValueError("Balance cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative number.")

    while True:
        try:
            annual_rate_str = input(
                "Enter the annual interest rate (%): "
            )  # Simplified prompt
            annual_rate = float(annual_rate_str)
            if annual_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative number.")

    time_difference = end_date - start_date
    num_days = time_difference.days
    print(
        f"\nNumber of days between {start_date.strftime('%d-%m-%Y')} and {end_date.strftime('%d-%m-%Y')}: {num_days}"
    )  # Formatted dates

    daily_interest_rate = annual_rate / 100 / 365
    interest_per_day = balance * daily_interest_rate
    print(f"Interest per day: {format_inr(interest_per_day)}")

    if num_days > 30:
        # Approximate monthly interest (using 30 days)
        monthly_interest_approx = balance * (annual_rate / 100 / 12)
        print(f"Approximate interest per month: {format_inr(monthly_interest_approx)}")

    interest_between_dates = balance * daily_interest_rate * num_days
    print(
        f"Interest between {start_date.strftime('%d-%m-%Y')} and {end_date.strftime('%d-%m-%Y')}: {format_inr(interest_between_dates)}"
    )
    print("-" * 30)


# --- Daily Deposit Interest Calculator ---
def daily_deposit_interest_calculator() -> None:
    print("\n--- Daily Deposit Interest Calculator ---")
    while True:
        try:
            start_date_str = input(
                "Enter Start Date (DD-MM-YYYY): "
            )  # Changed prompt & format
            start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    while True:
        try:
            collection_amount_str = input("Enter Collection Amount: ")  # Changed prompt
            collection_amount = float(collection_amount_str.replace(",", ""))
            if collection_amount <= 0:
                print("Collection amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    while True:
        frequency = (
            input("Enter Deposit Frequency (Daily/Weekly/Monthly): ").strip().lower()
        )
        if frequency in ["daily", "weekly", "monthly"]:
            break
        else:
            print("Invalid frequency. Please choose 'Daily', 'Weekly', or 'Monthly'.")

    while True:
        try:
            annual_rate_str = input(
                "Enter Annual Interest Rate (%): "
            )  # Simplified prompt
            annual_interest_rate = float(annual_rate_str)
            if annual_interest_rate < 0:
                print("Interest rate cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid interest rate. Please enter a number.")

    while True:
        try:
            period_months_str = input("Enter Period (in months): ")  # Simplified prompt
            period_months = int(period_months_str)
            if period_months <= 0:
                print("Period must be a positive number of months.")
                continue
            break
        except ValueError:
            print("Invalid period. Please enter a whole number of months.")

    end_date = start_date + timedelta(days=period_months * 30.4375)

    print("\n--- Daily Deposit Details ---")
    # Using loan repayment table style (no |)
    header_fmt = "{:<12}{:>18}{:>18}{:>20}"
    row_fmt = "{:<12}{:>18}{:>18}{:>20}"
    print(header_fmt.format("Date", "Amount", "Days Held", "Interest Accrued"))
    print("-" * 70)  # Adjusted width

    total_accrued_interest_display = (
        0  # This will sum up what's *displayed* in the table
    )
    total_principal_deposited = 0  # NEW: To track total principal

    current_iteration_date = start_date
    iteration_counter = 0

    # Determine the step for iteration based on frequency
    if frequency == "daily":
        time_step = timedelta(days=1)
    elif frequency == "weekly":
        time_step = timedelta(weeks=1)
    else:  # monthly
        time_step = None  # Handled separately with calendar module

    while current_iteration_date <= end_date:
        days_held_for_this_deposit = (end_date - current_iteration_date).days
        if days_held_for_this_deposit < 0:
            days_held_for_this_deposit = 0

        interest_for_this_entry = (
            collection_amount
            * (annual_interest_rate / 100 / 365)
            * days_held_for_this_deposit
        )
        total_accrued_interest_display += interest_for_this_entry
        total_principal_deposited += (
            collection_amount  # NEW: Add this deposit to total principal
        )

        print(
            row_fmt.format(
                current_iteration_date.strftime("%d-%m-%Y"),  # Formatted date
                format_inr(collection_amount),
                days_held_for_this_deposit,
                format_inr(interest_for_this_entry),
            )
        )

        # Advance current_iteration_date based on frequency
        if frequency == "monthly":
            current_month = current_iteration_date.month
            current_year = current_iteration_date.year
            next_month = current_month + 1
            next_year = current_year
            if next_month > 12:
                next_month = 1
                next_year += 1

            try:
                current_iteration_date = current_iteration_date.replace(
                    year=next_year, month=next_month, day=start_date.day
                )
            except ValueError:  # Handle cases like Jan 31st to Feb (no Feb 31st)
                last_day = calendar.monthrange(next_year, next_month)[1]
                current_iteration_date = current_iteration_date.replace(
                    year=next_year, month=next_month, day=last_day
                )
        else:
            current_iteration_date += time_step

        iteration_counter += 1
        # Prevent infinite loops in edge cases or very long periods for display purposes
        if (
            iteration_counter
            > (
                period_months
                * (31 if frequency == "daily" else (4 if frequency == "weekly" else 1))
            )
            + 5
        ):  # Generous buffer
            break

    print("-" * 70)
    print(
        f"{'Total':<12}{format_inr(total_principal_deposited):>18}{'':>18}{format_inr(total_accrued_interest_display):>20}"
    )  # MODIFIED: Display total principal
    print("---------------------------------\n")

    # --- Summary Section for Daily Deposit Interest Calculator ---
    print("\n--- Daily Deposit Calculation Summary ---")
    print(
        f"Start Date:              {start_date.strftime('%d-%m-%Y')}"
    )  # Formatted date
    print(f"Approx. End Date:        {end_date.strftime('%d-%m-%Y')}")  # Formatted date
    print(f"Period:                  {period_months} months")
    print(
        f"Collection Amount per deposit: {format_inr(collection_amount)}"
    )  # MODIFIED: Clarified prompt
    print(f"Annual Interest Rate:    {annual_interest_rate:.2f}%")
    print(f"Deposit Frequency:       {frequency.capitalize()}")
    print(
        f"Total Principal Deposited: {format_inr(total_principal_deposited)}"
    )  # NEW: Display total principal from summation
    print(
        f"Total Interest Earned:   {format_inr(total_accrued_interest_display)}"
    )  # Using the accumulated interest
    print(
        f"Maturity Value (Total Principal + Total Interest): {format_inr(total_principal_deposited + total_accrued_interest_display)}"
    )  # MODIFIED: Correct maturity value
    print("--- End of Calculation ---")


# --- Main Application Logic ---


def main() -> None:
    """
    The main function that runs the Bank Calculator application.
    It displays a menu and calls the appropriate calculation function based on user choice.
    """
    while True:
        print("\n--- Welcome to the Bank Calculator! ---")
        print("A simple, user-friendly tool for your banking calculations.")
        print("\nChoose an option:")
        print("1. Loan Calculator (Summary & Optional Repayment Table)")
        print("2. Fixed Deposit (FD) Interest Calculator")
        print("3. Calculate Interest Between Dates")
        print("4. Daily Deposit Interest Calculator")
        print("5. Exit Application")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            calculate_loan_summary_and_table()
        elif choice == "2":
            calculate_fd_interest()
        elif choice == "3":
            calculate_interest_between_dates()
        elif choice == "4":
            daily_deposit_interest_calculator()
        elif choice == "5":
            print("Thank you for using the Cooperative Bank Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
