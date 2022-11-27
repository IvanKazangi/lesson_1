class car:
    wheels = "Four"
    steeringwheel = "One"
    motor = "Dog"

    def __init__(self, classification="sidan", mileage="100", color="black"):
        self.classification = classification
        self.mileage = mileage
        self.color = color

st1 = car("hatchback", 110, "Blue")
st2 = car("universal", 300, "Red")
st3 = car("sidan", 500, "White")
st4 = car("hatchback", 700, "Grey")

print(car.wheels)
print(st1.color)
print(st2.color)
print(st3.color)
print(st4.color)
print(st1.mileage)
print(st2.mileage)
print(st3.mileage)
print(st4.mileage)
print(st1.classification)
print(st2.classification)
print(st3.classification)
print(st4.classification)