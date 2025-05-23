# 💰 Bank Specific Calculator CLI App

A comprehensive, terminal-based financial calculator tailored for Indian banking workflows. This CLI tool helps users compute various interest-related figures and repayment schedules for loans, fixed deposits, and daily deposit schemes with precision and INR formatting.

---

## 📦 Features

- **📉 Loan Calculator**
  - Reducing balance method with fixed principal payments
  - Loan summary and optional detailed amortization schedule

- **🏦 Fixed Deposit Calculator**
  - Interest at maturity
  - Monthly interest payout

- **📆 Interest Between Dates**
  - Calculate per-day interest for a given balance between two dates
  - Useful for overdraft or unpaid balances

- **🗓️ Daily Deposit Interest Calculator**
  - Handles daily, weekly, or monthly collection plans
  - Computes accrued interest per deposit for a specified term

- **💸 INR Formatting**
  - Displays all monetary values using Indian numbering and the ₹ symbol

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8 or newer

### ▶️ How to Run

1. Clone the repository or copy the script.
2. Run the script in your terminal:

```bash
python bank_calculator.py
````

3. Follow the on-screen prompts to navigate the calculators.

---

## 🧮 Example Use Cases

* 📊 **Loan Summary Only:**

  * Enter loan amount, term, and interest rate.
  * View total interest and total payments without detailed EMIs.

* 📋 **Full Loan Amortization Table:**

  * Get month-wise breakdown of principal, interest, EMI, and balance.

* 🏁 **FD Calculation:**

  * Compare maturity value vs monthly payout scenarios.

* 📅 **Interest Between Dates:**

  * See accrued interest from date-to-date on any balance.

* 📆 **Daily Deposits:**

  * Visualize how periodic deposits grow over time with interest.

---

## 📂 File Structure

```
bank_calculator.py     # Main script containing all logic and menus
README.md              # You're here!
```

---

## 🛠️ Functionality Overview

### `format_inr(amount)`

Formats numbers in Indian currency style: ₹1,23,456.78

### `calculate_loan_summary_and_table()`

Loan EMI summary using reducing balance method, with optional schedule.

### `calculate_loan_repayment_table(loan_amount, term_months, annual_rate)`

Detailed EMI schedule printer.

### `calculate_fd_interest()`

Fixed Deposit calculator supporting two interest types.

### `calculate_interest_between_dates()`

Simple interest computation between two given dates.

### `daily_deposit_interest_calculator()`

Accumulates and displays interest from recurring deposits.

---

## 🇮🇳 INR Formatting Example

```
Input: 1234567.89
Output: ₹12,34,567.89
```

---

## 🧾 License

This project is free to use and modify for personal or institutional purposes. Attribution appreciated.

---

## 📬 Feedback

Feel free to open issues or feature requests. Contributions welcome!
