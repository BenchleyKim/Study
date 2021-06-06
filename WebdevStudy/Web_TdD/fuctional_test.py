from selenium import webdriver
import unittest



class NewVisitorTest(unittest.TestCase) :
    def setUp(self) -> None:
        self.brower = webdriver.Chrome(executable_path="C:/Users/bottlechrome/Documents/GitHub/DeepDive/crawling/chromedriver.exe")
        self.brower.implicitly_wait(3)
    
    def tearDown(self) -> None:
        self.brower.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self) :

        self.brower.get('http://localhost:8000')
        self.assertIn('To_Do', self.brower.title )
        self.fail("Finished the test!")

if __name__ == '__main__' :
    unittest.main(warnings='ignore')

