from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    ALLOWED_LOANS = ["StudentLoan", "MortgageLoan"]
    VALID_TYPES_CLIENTS = ["Student", "Adult"]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def _get_client_by_id(self, client_id):
        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
            return client
        except IndexError:
            return None

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.ALLOWED_LOANS:
            raise Exception("Invalid loan type!")

        if loan_type == "StudentLoan":
            loan = StudentLoan()
            self.loans.append(loan)
        elif loan_type == "MortgageLoan":
            loan = MortgageLoan()
            self.loans.append(loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.VALID_TYPES_CLIENTS:
            raise Exception("Invalid client type!")

        if not len(self.clients) < self.capacity:
            return "Not enough bank capacity."

        if client_type == "Student":
            client = Student(client_name, client_id, income)
            self.clients.append(client)
        elif client_type == "Adult":
            client = Adult(client_name, client_id, income)
            self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self._get_client_by_id(client_id)

        loan = [l for l in self.loans if l.loan_type == loan_type][0]

        if loan_type == "StudentLoan" and not client.client_type == "Student":
            raise Exception("Inappropriate loan type!")
        elif loan_type == "MortgageLoan" and not client.client_type == "Adult":
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self._get_client_by_id(client_id)
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for loan in self.loans:
            if loan.loan_type == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):

        total_clients_count = len(self.clients)
        total_clients_income = sum([client.income for client in self.clients])

        loans_count_granted_to_clients = len([loan for client in self.clients for loan in client.loans]) #Shady
        granted_sum = sum(loan.amount for client in self.clients for loan in client.loans)

        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([loan.amount for loan in self.loans])

        avg_client_interest_rate = 0
        if self.clients:
            avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients)

        result_string = (
            f"Active Clients: {total_clients_count}\n"
            f"Total Income: {total_clients_income:.2f}\n"
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
            f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        )

        return result_string
