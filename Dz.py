class animals:
    legs = "Four"
    eyes = "Two"
    animal = "Dog"

    def __init__(self, name="Barsik", age="7", color="black"):
        self.name = name
        self.age = age
        self.color = color

st1 = animals("Barsik1", 11, "Black-white")
st2 = animals("Barsik2", 3, "White-grey")
st3 = animals("Barsik3", 5, "White")
st4 = animals("Barsik4", 7, "Grey")

print(animals.legs)
print(st1.color)
print(st2.color)
print(st3.color)
print(st4.color)
print(st1.age)
print(st2.age)
print(st3.age)
print(st4.age)
print(st1.name)
print(st2.name)
print(st3.name)
print(st4.name)
