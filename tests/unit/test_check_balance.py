import unittest
from shopping.shoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    # 測試檢查餘額功能是否是否如同預期執行
    def test_check_balance(self):
        cart = ShoppingCart()  # 建立 ShoppingCart 實例
        self.assertEqual(cart.checkBalance(100, 50), "餘額不足")  # 測試不足的餘額
        self.assertEqual(cart.checkBalance(100, 150), 50)        # 測試足夠的餘額
        self.assertEqual(cart.checkBalance(200, 200), 0)         # 測試剛好支付的情況

if __name__ == '__main__':
    unittest.main()