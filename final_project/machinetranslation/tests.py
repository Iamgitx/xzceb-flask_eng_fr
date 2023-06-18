import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english


class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('hello'), 'bonjour') # Hello is given as input the output is Bonjour.
        self.assertEqual(english_to_french('yes'), 'oui')  # Yes is given as input the output is Oui.
        self.assertNotEqual(english_to_french('house'), 'house')  # House is given as input the output is not House.
        

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('bonjour'), 'hello') # Bonjour is given as input the output is Hello.
        self.assertEqual(french_to_english('oui'), 'yes') # Oui is given as input the output is Yes.
        self.assertNotEqual(french_to_english('maison'), 'maison') # Maison is given as input the output is not Maison.
        
if __name__ == "__main__":    
    unittest.main()
    