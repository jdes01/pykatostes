from sqlite3 import Date
from typing import List
import unittest
from kata import Bank, InMemoryRepository, Transaction

class Test(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2,2)

    #def test_bank_class_should_have_methods_defined(self):
    #    self.assertRaises(TypeError, lambda: Bank())

    def test_deposit_should_return_none(self):
        repository = InMemoryRepository()
        bank = Bank(repository)
        self.assertEqual(bank.deposit(3), None)
    
    def test_deposit_should_receive_a_number(self):
        repository = InMemoryRepository()
        bank = Bank(repository)
        self.assertRaises(TypeError, lambda: bank.deposit())

    def test_deposit_should_be_a_number(self):
        repository = InMemoryRepository()
        bank = Bank(repository)
        self.assertRaises(Exception, lambda: bank.deposit('not an integer'))

    def test_InMemoryRepository_works_fine(self):
        repository = InMemoryRepository()
        self.assertEqual(repository.getMoney(), 0)

        repository.save(8)
        repository.save(3)
        self.assertEqual(repository.getMoney(), 11)

        repository.remove(5)
        self.assertEqual(repository.getMoney(), 6)

        repository.remove(7)
        self.assertEqual(repository.getMoney(), -1)

    def test_bank_deposit_method_stores_money_in_repository(self):
        repository = InMemoryRepository()
        bank = Bank(repository)
        bank.deposit(8)
        self.assertEqual(repository.getMoney(), 8)

    def test_withdraw_method_works_fine(self):
        repository = InMemoryRepository(10)
        bank = Bank(repository)
        bank.withdraw(8)
        self.assertEqual(repository.getMoney(), 2)

    def test_printStatement_method_works_fine(self):
        repository = InMemoryRepository()
        bank = Bank(repository)
        
        bank.deposit(3)
        firstTransaction = Transaction(Date.today(), 3, 3)

        bank.deposit(1)
        secondTransaction = Transaction(Date.today(), 1, 4)

        bank.withdraw(2)
        thirdTransaction = Transaction(Date.today(), 2, 2)

        listOfTransactions: List[Transaction] = bank.printStatement()

        self.assertEqual(listOfTransactions[0].date, firstTransaction.date)
        self.assertEqual(listOfTransactions[1].amount, secondTransaction.amount)
        self.assertEqual(listOfTransactions[2].balance, thirdTransaction.balance)