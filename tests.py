import surfshop
import unittest

class ShoppingCartTests(unittest.TestCase):

  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards_one(self):
    self.assertEqual(self.cart.add_surfboards(), 'Successfully added 1 surfboard to cart!')
  
  def test_add_surfboards_multiple(self):
    for num in range(2, 5):
      with self.subTest(num):
        message = self.cart.add_surfboards(num)
        self.assertEqual(message, f'Successfully added {num} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()

  @unittest.skip('Store\'s shopping cart no longer needs to enforce the 4 surfboards per customer rule during the off-season.')
  def test_too_many_boards_error(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  # commented out - test should not fail at end of project
  # @unittest.expectedFailure
  def test_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()
    






