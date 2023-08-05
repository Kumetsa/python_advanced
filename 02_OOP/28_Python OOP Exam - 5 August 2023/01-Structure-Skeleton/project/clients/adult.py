from typing import List

from project.clients.base_client import BaseClient
from project.loans.base_loan import BaseLoan


class Adult(BaseClient):
    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=4.0)
        self.client_type = "Adult"

    def increase_clients_interest(self):
        self.interest += 2.0
