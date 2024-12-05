class Animal:
    """
    Base class for all animals.
    """

    def __init__(self, name):
        self.name = name

    def move(self):
        """
        Define a generic move action (to be overridden by subclasses).
        """
        raise NotImplementedError("Subclasses must override move()!")


class Cow(Animal):
    """
    Cow class representing a cow's movement.
    """

    def move(self):
        return f"{self.name} is walking slowly in the field."


class Eagle(Animal):
    """
    Eagle class representing an eagle's movement.
    """

    def move(self):
        return f"{self.name} is soaring high in the sky."


class Fish(Animal):
    """
    Fish class representing a fish's movement.
    """

    def move(self):
        return f"{self.name} is swimming gracefully in the water."


class Snake(Animal):
    """
    Snake class representing a snake's movement.
    """

    def move(self):
        return f"{self.name} is slithering silently across the ground."


# Example Usage
if __name__ == "__main__":
    # Create instances of animals
    cow = Cow("Bessie the Cow")
    eagle = Eagle("Eddie the Eagle")
    fish = Fish("Nemo the Fish")
    snake = Snake("Slytherin the Snake")

    # Store animals in a list
    animals = [cow, eagle, fish, snake]

    # Call the move() method on each animal
    for animal in animals:
        print(animal.move())
