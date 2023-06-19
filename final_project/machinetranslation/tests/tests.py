import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english


class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertEqual(english_to_french('yes'), 'oui')
        self.assertNotEqual(english_to_french('hello'), 'hello')
        

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertEqual(french_to_english('oui'), 'yes')
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')
        
if __name__ == "__main__":    
    unittest.main()
    