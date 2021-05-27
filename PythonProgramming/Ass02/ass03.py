class car :
    def __init__(self, max_fuel, fuel_economy, max_passengers, state) -> None:
        self.max_fuel = max_fuel
        self.fuel_economy = fuel_economy
        self.max_passengers = max_passengers
        self.passenger = 0
        if state == 'new' :
            self.mileage = 0
            self.fuel = self.max_fuel
        else :
            self.mileage = 50_000
            self.fuel = self.max_fuel * 0.3
    
    def show_dash(self) :
        print(self.mileage)
        print(self.fuel)
        print(self.fuel / self.max_fuel)
        print(self.fuel_economy )
        
    def fill_up(self) :
        self.fuel = self.max_fuel
    
    def fill(self,x) :
        self.fuel += x
        self.fuel = min(self.fuel, self.max_fuel)
    
    def ride(self , x):
        self.passenger += x
        self.passenger = min(self.passenger, self.max_passengers)
    def get_range(self) :
        return (self.fuel_economy - (self.passenger / self.max_passengers * self.fuel_economy * 0.1 )) * self.fuel
    
    def move(self, x) :
        if self.get_range() > x :
            self.fuel -= 
    