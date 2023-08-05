from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    STUDENT_RATE = 1.5
    STUDENT_AMOUNT = 2000

    def __init__(self):
        super().__init__(interest_rate=self.STUDENT_RATE, amount=self.STUDENT_AMOUNT)
        self.loan_type = "StudentLoan"

    def increase_interest_rate(self):
        self.interest_rate += 0.2
