import pytest
from project import amortizing_loan, annuity_loan, bullet_loan, get_annuity_factor

def test_amortizing_loan():
    principal = 1000.0
    interest_rate = 0.05
    term = 5

    # Expected output
    time_periods = [1, 2, 3, 4, 5]
    repayments = [principal / term] * term
    remaining_balances = [principal - sum(repayments[:i]) for i in range(term)]
    interests = [remaining_balance * interest_rate for remaining_balance in remaining_balances]
    installments = [repayment + interest for repayment, interest in zip(repayments, interests)]
    expected = [time_periods, remaining_balances, interests, repayments, installments]

    # Actual output
    result = amortizing_loan(principal, interest_rate, term, raw=True)
    assert result == expected

def test_annuity_loan():
    principal = 1000.0
    interest_rate = 0.05
    term = 5

    # Calculate annuity
    annuity = principal * get_annuity_factor(interest_rate, term)
    time_periods = [1, 2, 3, 4, 5]
    installments = [annuity] * term
    repayments = [(annuity - principal * interest_rate) * pow(1 + interest_rate, i) for i in range(term)]
    interests = [annuity - repayment for repayment in repayments]
    remaining_balances = [principal - sum(repayments[:i]) for i in range(term)]
    expected = [time_periods, remaining_balances, interests, repayments, installments]

    # Actual output
    result = annuity_loan(principal, interest_rate, term, raw=True)
    assert result == expected

def test_bullet_loan():
    principal = 1000.0
    interest_rate = 0.05
    term = 5

    # Expected output
    time_periods = [1, 2, 3, 4, 5]
    interests = [principal * interest_rate] * term
    installments = interests[:]
    installments[-1] += principal
    repayments = [0] * (term - 1) + [principal]
    remaining_balances = [principal] * term
    expected = [time_periods, remaining_balances, interests, repayments, installments]

    # Actual output
    result = bullet_loan(principal, interest_rate, term, raw=True)
    assert result == expected
