import unittest

from kata import Game


WORDS: list = ['joder', 'adios']


class TestKata(unittest.TestCase):
    def test_imput_word_match_all_letters(self):
        #Arrange:
        seed = 0
        game = Game(words=WORDS, seed=seed)
        
        #Act:
        returned_value = game.evaluate("joder")
        
        #Assert:
        assert returned_value == "joder"
        
    def test_imput_word_match_one_letter(self):
        #Arrange:
        seed = 0
        game = Game(words=['joder', 'jaaaa'], seed=seed)

        #Act:
        returned_value = game.evaluate("jaaaa")
        
        #Assert:
        assert returned_value == "j----"
        
    def test_imput_word_match_one_letter_in_different_position(self):
        #Arrange:
        seed = 0
        game = Game(words=['joder', 'ajaaa'], seed=seed)
        
        #Act:
        returned_value = game.evaluate("ajaaa")
        
        #Assert:
        assert returned_value == "-+---"

    
    def test_only_mark_as_wrong_placed_the_first_appearance(self):
        #Arrange:
        seed = 0
        game = Game(words=['joder', 'ajjaa'], seed=seed)

        #Act:
        returned_value = game.evaluate("ajjaa")
        
        #Assert:
        assert returned_value == "-+---"


    def test_if_two_appearances_of_only_one_correct_letter_marks_one_as_correct(self):
        #Arrange:
        seed = 0
        game = Game(words=['joder', 'rxxxr'], seed=seed)

        #Act:
        returned_value = game.evaluate("rxxxr")
        
        #Assert:
        assert returned_value == "----r"

        
    def test_assert_maximum_six_attempts(self):
        #Arrange:
        seed = 0
        game = Game(words=['joder', 'rxxxr'], seed=seed)

        #Act:
        game.evaluate("rxxxr")
        game.evaluate("rxxxr")
        game.evaluate("rxxxr")
        game.evaluate("rxxxr")
        game.evaluate("rxxxr")
        game.evaluate("rxxxr")
        
        failed_attempt = game.evaluate("rxxxr")
        
        #Assert:
        assert failed_attempt == "a txuparla"
