# car1_milage = 20
# car1_cc = 1200
# car1_wheels =4
# car1_airbags = 5
# car1_cam = 2

# def acc():
#     print("Car1 Moves")
# def breaks():
#     print("car1 Stopss")


# car2_milage = 20
# car2_cc = 1200
# car2_wheels =4
# car2_airbags = 5
# car2_cam = 2

# def acc():
#     print("Car2 Moves")
# def breaks():
#     print("car2 Stopss")



class Cars:
    car_milage = 0
    car_cc = 0
    car_wheels =4
    car_airbags = 5
    car_cam = 2
    car_Name = "Honda"

    def acc(self,name):
        self.name = name
        print(f"{name} Moves")
    def breaks(self):
        print("car Stopss")
    

c1 = Cars()
c2 = Cars()

print(c1.car_milage)
c1.car_milage=25
print(c1.car_milage)
print(c2.car_milage)
c2.car_milage=20
print(c2.car_milage)
c1.acc("BMW")
c2.acc("Benz")