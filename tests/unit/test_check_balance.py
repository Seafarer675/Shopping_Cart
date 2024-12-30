import unittest
from shopping.shoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    # 測試檢查餘額功能是否是否如同預期執行
<<<<<<< HEAD
    def test_check_balance(self):
         cart = self.cart
         self.assertEqual(cart.check_balance(100, 50), 50)
         self.assertEqual(cart.check_balance(200, 100), 100)
         self.assertEqual(cart.check_balance(50, 100), "餘額不足")
=======
    # def test_check_balance(self):
    #     cart = self.cart
    #     self.assertEqual(cart.check_balance(100, 50), 50)
    #     self.assertEqual(cart.check_balance(200, 100), 100)
    #     self.assertEqual(cart.check_balance(50, 100), "餘額不足")
>>>>>>> 01357fc5cf6b48797f28868fe5533d4ca4fbebe6

if __name__ == '__main__':
    unittest.main()