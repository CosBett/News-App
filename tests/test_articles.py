import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
  '''
  Test class to test behaviour of the article class
  '''
  def setUp(self):
      ''' 
      set up method that will run before every Test
      '''
      self.new_article = Articles( "Gian M. Volpicelli", "Gibraltar Could Launch the World First Crypto Stock Exchange","“The Rock” hopes a new stock exchange will attract crypto millionaires who want to avoid hefty taxes.", "https://www.wired.com/story/gibraltar-crypto-exchange/", "https://media.wired.com/photos/61f0b4bf03f9ae99229f47d4/191:100/w_1280,c_limit/Business_Gibraltar-1208348908.jpg", "2022-01-26T12:00:00Z","British entrepreneur and financier Richard ODell Poulden hopes that his new venture will relieve the plight of an underserved cohort: Bitcoin billionaires who want to buy a house. In October, Poulde… [+3364 chars]")
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Articles))    