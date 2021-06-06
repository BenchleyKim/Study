import unittest
import ass03 

def custom_function() :
    pass


class CustomTests(unittest.TestCase) :
    def setUp(self) -> None:
        self.new_sonata  = Car.Sonata("new")
        self.old_sonata = Car.Sonata("old")
    def test_setUp(self) :
        "테스트 실행"
        assert self.new_sonata.max_fuel == 55
        assert self.new_sonata.max_passengers == 4 
        assert self.new_sonata.fuel == self.new_sonata.max_fuel
        self.assertEqual(self.new_sonata.fuel_economy , 12)
        assert self.old_sonata.max_fuel == 55
        assert self.old_sonata.max_passengers == 4 
        assert self.old_sonata.fuel == self.old_sonata.max_fuel* 0.3
        self.assertEqual(self.old_sonata.fuel_economy , 12)
    
    def test_fillUp(self) :
        self.new_sonata.fuel = 0 
        self.new_sonata.fill_up()
        self.assertEqual(self.new_sonata.fuel , self.new_sonata.max_fuel)
        self.new_sonata.fuel = self.new_sonata.max_fuel
        self.new_sonata.fill_up()
        self.assertEqual(self.new_sonata.fuel , self.new_sonata.max_fuel)
        self.old_sonata.fuel = 0 
        self.old_sonata.fill_up()
        self.assertEqual(self.old_sonata.fuel , self.old_sonata.max_fuel)
        self.old_sonata.fuel = self.old_sonata.max_fuel
        self.old_sonata.fill_up()
        self.assertEqual(self.old_sonata.fuel , self.old_sonata.max_fuel)
    def test_fill(self) :
        self.new_sonata.fuel = 0
        self.new_sonata.fill(550) 
        self.assertEqual(self.new_sonata.fuel, self.old_sonata.max_fuel)
        self.new_sonata.fuel = 0
        self.new_sonata.fill(-50)
        self.assertEqual(self.new_sonata.fuel, 0)

        




if __name__ == '__main__' :
    unittest.main()

