import membership_fee_calculator

def always_pass():
    assert membership_fee_calculator.calculate_membership_fee(3000, 'month', 'branch_b')


def always_fail():
    assert membership_fee_calculator.calculate_membership_fee(25, 'month', 'branch_d')