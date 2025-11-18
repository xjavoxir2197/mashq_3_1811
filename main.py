class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subklasslar bu metodni qayta yozishi kerak.")

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Foydalanish
print("\n--- Hayvonlar ovozi (Polimorfizm) ---")
animals = [
    Dog("Katta it"),
    Cat("Kichik mushuk"),
    Cow("Katta sigir"),
    Dog("Kichik it")
]
for animal in animals:
    print(f"🔊 {animal.name} deydi: {animal.speak()}")
