import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
  '''
  Test class to test behaviour of the source class
  '''
  def setUp(self):
      ''' 
      set up method that will run before every Test
      '''
      self.new_article = Source( "al-jazeera-english", "Al Jazeera English", "News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.", "http://www.aljazeera.com", "general", "en", "us")
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Source))    