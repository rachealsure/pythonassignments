class Superhero:
    """
    A class representing a superhero.
    """

    def __init__(self, name, alias, power_level, universe):
        """
        Initialize a superhero with basic attributes.
        """
        self.name = name
        self.alias = alias
        self.power_level = power_level
        self.universe = universe

    def introduce(self):
        """
        Introduce the superhero.
        """
        return f"I'm {self.alias}, also known as {self.name}, from the {self.universe} universe!"

    def use_power(self):
        """
        Display the superhero's power usage.
        """
        return f"{self.alias} is using their powers at a level of {self.power_level}!"

    def train(self, hours):
        """
        Increase the power level based on training hours.
        """
        self.power_level += hours * 10
        return f"{self.alias} trained for {hours} hours. Power level is now {self.power_level}."


# Subclass: FlyingHero
class FlyingHero(Superhero):
    """
    A subclass representing superheroes with flying abilities.
    """

    def __init__(self, name, alias, power_level, universe, flight_speed):
        super().__init__(name, alias, power_level, universe)
        self.flight_speed = flight_speed

    def use_power(self):
        """
        Override: Display the flying superhero's power usage.
        """
        return f"{self.alias} is flying at {self.flight_speed} km/h with a power level of {self.power_level}!"

    def upgrade_flight(self, speed_increase):
        """
        Upgrade flight speed.
        """
        self.flight_speed += speed_increase
        return f"{self.alias} upgraded their flight speed to {self.flight_speed} km/h!"


# Subclass: StrengthHero
class StrengthHero(Superhero):
    """
    A subclass representing superheroes with super strength.
    """

    def __init__(self, name, alias, power_level, universe, max_weight):
        super().__init__(name, alias, power_level, universe)
        self.max_weight = max_weight

    def use_power(self):
        """
        Override: Display the strong superhero's power usage.
        """
        return f"{self.alias} is lifting {self.max_weight} tons with a power level of {self.power_level}!"

    def train(self, hours):
        """
        Override: Increase strength through training.
        """
        self.power_level += hours * 15
        self.max_weight += hours * 0.5
        return f"{self.alias} trained for {hours} hours. Power level is now {self.power_level}, and max weight lifted is {self.max_weight} tons."


# Example Usage
if __name__ == "__main__":
    # Create objects
    general_hero = Superhero("Kara Danvers", "Supergirl", 100, "DC")
    flying_hero = FlyingHero("Peter Parker", "Spider-Man", 85, "Marvel", 200)
    strength_hero = StrengthHero("Diana Prince", "Wonder Woman", 120, "DC", 50)

    # General superhero
    print(general_hero.introduce())
    print(general_hero.use_power())
    print(general_hero.train(3))
    print()

    # Flying superhero
    print(flying_hero.introduce())
    print(flying_hero.use_power())
    print(flying_hero.upgrade_flight(50))
    print()

    # Strong superhero
    print(strength_hero.introduce())
    print(strength_hero.use_power())
    print(strength_hero.train(4))
