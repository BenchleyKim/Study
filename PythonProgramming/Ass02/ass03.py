from collections import deque

class Car :
    def __init__(self, max_fuel : int, fuel_economy : int, max_passengers : int, state : str ) -> None:
        """ 
        max_fuel : 최대 연료량
        fuel_economy : 연비
        max_passengers : 최대 탑승량 
        state : 신차인지 중고차인지
        passenger : 현재 탑승자 
        fuel_economy_100 : 100km 주행 간 연비 
        """
        self.max_fuel = max_fuel
        self.fuel_economy = fuel_economy
        self.max_passengers = max_passengers
        self.passenger = 0
        self.fuel_economy_100 = deque()
        """
        mileage : 현재 마일리지( 중고차일때는 50_000부터 시작)
        fuel : 현재 연료량 (신차는 가득, 중고차는 30%로 시작)
        
        """
        if state == 'new' :
            self.mileage = 0
            self.fuel = self.max_fuel
        elif state == 'old' :
            self.mileage = 50_000
            self.fuel = self.max_fuel * 0.3
        else :
            raise TypeError()
    def show_dash(self) :
        print(self.mileage, self.fuel,self.get_range(), sum(self.fuel_economy_100)/len(self.fuel_economy_100), self.passenger)
    
    def fill_up(self) :
        self.fuel = self.max_fuel
    
    def fill(self, x) :
        self.fuel = min(self.max_fuel, self.fuel + x )
    
    def ride(self, x) :
        self.passenger = min(self.max_passengers, self.passenger + x )
    
    def current_fuel_economy(self) :
        return self.fuel_economy - self.fuel_economy * 0.1 * self.passenger / self.max_passengers


    def get_range(self) :
        return self.fuel * self.current_fuel_economy()

    def move(self, x) :
        if x > self.get_range() :
            print("갈 수 없는 거리입니다. ")
            mileage = self.get_range() 

            for i in range(int(mileage)) :
                self.fuel_economy_100.append(self.current_fuel_economy())
            while len(self.fuel_economy_100) > 100 :
                self.fuel_economy_100.popleft()

            self.mileage += self.get_range() 
            self.fuel = 0 
        else : 
            
            for i in range(x) :
                self.fuel_economy_100.append(self.current_fuel_economy())
            while len(self.fuel_economy_100) > 100 :
                self.fuel_economy_100.popleft()

            self.mileage += x
            self.fuel -= x / self.current_fuel_economy()



    def get_milleage(self) :
        return self.mileage

class Sonata(Car) :
    def __init__(self, state: str) -> None:
        super().__init__(55, 12, 4, state)

class  Tucson(Car) :
    def __init__(self, state: str) -> None:
        super().__init__(60, 10, 5, state)

class Bongo(Car) :
    def __init__(self, state: str) -> None:
        super().__init__(55, 11, 700 , state)

class Tesla_S(Car) :
    def __init__(self, state: str) -> None:
        super().__init__(450, 1, 5, state)


# sonata = Sonata("new")
# sonata.ride(1)
# sonata.move(50)
# sonata.ride(2)
# sonata.move(450)
# sonata.show_dash()
# sonata.fill(35)
# sonata.move(140)
# sonata.ride(-1)
# sonata.move(100)
# sonata.show_dash()
    