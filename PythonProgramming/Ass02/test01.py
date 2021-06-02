import unittest
import ass03 

def custom_function() :
    pass


class CustomTests(unittest.TestCase) :
    def setUp(self) -> None:
        self.sonata  = ass03.Sonata("new")
    def test_setUp(self) :
        "테스트 실행"
        assert self.sonata.max_fuel == 55
        assert self.sonata.fuel_economy == 12
        assert self.sonata.max_passengers == 4 
        assert self.sonata.fuel == self.sonata.max_fuel




if __name__ == '__main__' :
    unittest.main()

