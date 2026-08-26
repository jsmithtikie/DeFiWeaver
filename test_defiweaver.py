# test_defiweaver.py
"""
Tests for DeFiWeaver module.
"""

import unittest
from defiweaver import DeFiWeaver

class TestDeFiWeaver(unittest.TestCase):
    """Test cases for DeFiWeaver class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeFiWeaver()
        self.assertIsInstance(instance, DeFiWeaver)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeFiWeaver()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
