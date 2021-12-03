# pin_code = int(input("What is your pin code?\n"))
# ------
import unittest


def withdrawal():
    account_balance = 100
    try:
        withdrawal = int(input("How much money would you like to withdraw?\n"))
    except:
        withdrawal = 0
        print("Wrong input, you should only input integer.")

    if withdrawal < account_balance:
        account_balance -= withdrawal
        return f"Your total remaining amount is {account_balance}."

    else:
        return "You do not have enough money in your account to make this transaction."
# #
# # def must start with test always
# can only do unit tests with something that is a return
# In the assertEqual must be the exact same statement as seen in the function above
class Testing(unittest.TestCase):

    def test_correct_withdrawal(self):
        a = withdrawal()
        self.assertEqual(a,"Your total remaining amount is 20.")

    def test_incorrect_withdrawal(self):
        a = withdrawal()
        self.assertEqual(a,"You do not have enough money in your account to make this transaction.")

unittest.main()


# def pin(correct_pin):
#
#     count = 0
#
#     while count < 3:
#         try:
#             pin_code = int(input("What is your pin code?\n"))
#         except:
#             pin_code = 0
#             print("Wrong input, you should only input integer.")
#         #     the except contains the error so pin_code is no longer defined
#
#         if pin_code != correct_pin:
#             print("Wrong input, try again.")
#             count += 1
#
#         if pin_code == correct_pin:
#             print("This is the correct pin.\n")
#             return correct_pin
#
#         if count == 3:
#             return "You have entered your pin incorrectly too many times. Please try again later.\n"
# #
# class TestingPin(unittest.TestCase):
#
#     def test_correct_pin(self):
#         """
#         testing what happens when the pin has been correctly inputed
#         :return:
#         """
#         a = pin(78153)
#         self.assertEqual(a, 78153)
#
#     def test_incorrect_pin(self):
#         """
#         testing what happens when the pin has been incorrectly inputed three times
#         :return:
#         """
#         a = pin(78153)
#         self.assertEqual(a,"You have entered your pin incorrectly too many times. Please try again later.\n")
#
#     def test_incorrect_pin_2(self):
#         """
#         testing what happens when the pin has been inputed as a string of letters instead of numbers
#         :return:
#         """
#         a = pin(78153)
#         self.assertEqual(a,"You have entered your pin incorrectly too many times. Please try again later.\n")
#
# unittest.main()


# def atm(correct_pin):
#     pin_num = pin(correct_pin)
#     if pin_num == correct_pin:
#         print(withdrawal())
#
# atm(78153)
# class Testing(unittest.TestCase):
#     def correct_withdrawal(self):
#         a = atm()
#
# unittest.main()

# unit test - create a function then create a class to test if the function will test all bthe things you are looking for in the function

# def number(num):
#     if num % 2 == 0:
#        return num + 2
#     else:
#       return  num - 2
#
# class Testing(unittest.TestCase):
#     def test_odd(self):
#         a = number(7)
#         self.assertEqual(a, 5)
#
#     def test_even(self):
#         a = number(6)
#         self.assertEqual(a, 8)
#
# unittest.main()