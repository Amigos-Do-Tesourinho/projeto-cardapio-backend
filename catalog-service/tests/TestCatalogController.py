import sys
sys.path.append('../')

import unittest
from controllers.CatalogController import get_all

class TestCatalogController(unittest.TestCase):
    def test_get_all(self):
        payload = get_all()
        self.assertEqual(payload['message'], 'Hello, World!')

if __name__ == '__main__':
    unittest.main()