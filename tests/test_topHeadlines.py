import unittest
from app.models import  TopHeadlines

class TopHeadlinesTest(unittest.TestCase):
  '''
  Test class to test behaviour of the source class
  '''
  def setUp(self):
      ''' 
      set up method that will run before every Test
      '''
      self.new_article = TopHeadlines( 'null', "KFSN-TV", "Jessica Harrington, Nic Garcia", "Stockton fire captain dies after being shot while battling fire, police say - KFSN-TV", "Authorities say a Stockton fire captain died after being shot while battling a fire on Monday morning.", "https://abc30.com/stockton-firefighter-shot-fireman-fire/11525858/", "https://cdn.abcotvs.com/dip/images/11526515_maxfortuna.JPG?w=1600", "2022-02-01T06:33:45Z", "STOCKTON, Calif. -- Hundreds of North Valley firefighters and officers paid their respects after a fire captain was shot and killed on the job Monday.An investigation is underway and 67-year-old Robe… [+2530 chars]")
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, TopHeadlines))    