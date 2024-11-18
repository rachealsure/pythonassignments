def greet_user():
    # Ask for user's name and favorite color
    name = input("What is your name? ")
    color = input("What is your favorite color? ")
    
    # Print personalized greeting
    print(f"Hello, {name}! Your favorite color, {color}, is awesome!")

# Run the greeting function
greet_user()