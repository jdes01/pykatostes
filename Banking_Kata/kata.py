from abc import ABC, abstractmethod
from sqlite3 import Date
import string
from typing import List

class Transaction():
    def __init__(self, date: Date, amount: int, balance: int) -> None:
        self.date = date
        self.amount = amount
        self.balance = balance


class AbstractRepository(ABC):
    @abstractmethod
    def save(money_to_be_saved: int) -> None:
        pass

    @abstractmethod
    def getMoney() -> int:
        pass

    @abstractmethod
    def getTransactions() -> List[Transaction]:
        pass

    @abstractmethod
    def remove(money_to_be_removed: int) -> None:
        pass


class InMemoryRepository(AbstractRepository):
    def __init__(self, initial_amount: int = 0) -> None:
        self.__money_stored: int = initial_amount
        self.__transactions: Transaction = [] 

    def save(self, money_to_be_saved: int) -> None :
        self.__money_stored += money_to_be_saved
        self.__transactions.append(
            Transaction(
                Date.today(),
                money_to_be_saved,
                self.__money_stored
            )
        )

    def getMoney(self) -> int :
        return self.__money_stored
    
    def getTransactions(self) -> List[Transaction] :
        return self.__transactions

    def remove(self, money_to_be_removed: int) -> None :
        self.__money_stored -= money_to_be_removed
        self.__transactions.append(
            Transaction(
                Date.today(),
                money_to_be_removed,
                self.__money_stored
            )
        )


class AbstractBank(ABC):
    @abstractmethod
    def deposit(money_amount: int) -> None:
        pass

    @abstractmethod
    def withdraw(int) -> None:
        pass

    @abstractmethod
    def printStatement(int) -> string:
        pass


class Bank(AbstractBank):

    def __init__(self, repository: AbstractRepository) -> None:
        self.__repository = repository

    def deposit(self, money_amount: int) -> None:
        if type(money_amount) is not int:
            raise Exception('money should be an integer') 
        self.__repository.save(money_amount)

    def withdraw(self, money_amount: int) -> None:
        self.__repository.remove(money_amount)

    def printStatement(self) -> string:
        return self.__repository.getTransactions()
