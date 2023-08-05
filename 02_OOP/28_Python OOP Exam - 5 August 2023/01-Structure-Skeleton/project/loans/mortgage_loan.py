from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    MORTGAGE_RATE = 3.5
    MORTGAGE_AMOUNT = 50000

    def __init__(self):
        super().__init__(interest_rate=self.MORTGAGE_RATE, amount=self.MORTGAGE_AMOUNT)
        self.loan_type = "MortgageLoan"

    def increase_interest_rate(self):
        self.interest_rate += 0.5