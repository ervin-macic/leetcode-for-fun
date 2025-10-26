class Bank:
    n = 0
    balance = []
    def __init__(self, balance: list[int]):
        self.n = len(balance)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._valid_index(account1) and self._valid_index(account2) and self._sufficient_funds(account1, money):
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self._valid_index(account):
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self._valid_index(account) and self._sufficient_funds(account, money):
            self.balance[account-1] -= money
            return True 
        return False
        
    def _valid_index(self, index: int) -> bool:
        return (1 <= index and index <= self.n)
    
    def _sufficient_funds(self, index: int, money: int) -> bool:
        if not self._valid_index(index):
            raise Exception
        return (self.balance[index-1] >= money)

# Your Bank object will be instantiated and called as such:
bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))   # return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                        # Account 3 has $20 - $10 = $10.
print(bank.transfer(5, 1, 20)) # return true, account 5 has a balance of $30, so it is valid to transfer $20.
                        # Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
print(bank.deposit(5, 20))    # return true, it is valid to deposit $20 to account 5.
                        # Account 5 has $10 + $20 = $30.
print(bank.transfer(3, 4, 15)) # return false, the current balance of account 3 is $10,
                        # so it is invalid to transfer $15 from it.
print(bank.withdraw(10, 50))   # return false, it is invalid because account 10 does not exist.