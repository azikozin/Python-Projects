class Greeting:
    def __init__(self, message):
        self.message = message
    
    def display_greeting(self):
        print(self.message)

# Create variables
name = "World"
greeting_text = f"Hello, {name}!"

# Create an instance of the Greeting class
my_greeting = Greeting(greeting_text)

# Display the greeting
my_greeting.display_greeting()