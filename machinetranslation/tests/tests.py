import unittest
from translator import english_to_french, french_to_english


class TestTranslateFunctions(unittest.TestCase):
    def test_nul(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(french_to_english(None), None)


    def test_space(self):
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(french_to_english(' '), ' ')


    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'),'Hello' )


    def test_new_line(self):
        self.assertEqual(english_to_french(
            "I'm tired today.\nHello"),
            "Je suis fatigué aujourd'hui.\nBonjour"
        )
        self.assertEqual(french_to_english(
            "Je suis fatigué aujourd'hui.\nBonjour"),
            "I'm tired today.\nHello"
        )

    
    def test_untranslatable(self):
        self.assertNotEqual(english_to_french(
            "Глупый тест"),
            None
        )
        self.assertNotEqual(french_to_english(
            "Глупый тест"),
            None
        )
    

if __name__ == '__main__':
    unittest.main()
