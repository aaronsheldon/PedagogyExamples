# This is a single line comment.
# Comments are not executed.
# They have no effect on the runtime.

"""
The previous comment should have
used the multi-line comment syntax
"""

# This will be our salutation, assigned to a variable called
# salutation. Assigning to a variable is also called "binding"
# to a "name" or "identifier"
paragraph = """This is a long set of sentences.
We can enter multiple lines of string by using\n the triples of double quotes.
This is helpful for hardcoding things like HTML."""
thisisanumber = 5.12
print("First value assigned.")
print(f"thisisanumber: {thisisanumber}")
thisisanumber = "six point five"
print("Change of value assigned.")
print(f"thisisanumber: {thisisanumber}")

"""
Our little program will prompt for a name and then
acknowledge the person.
"""
greeting = "Hello. What is you name? "

# Input displays the prompt and awaits a typed
# response.
guest = input(greeting)

# Builds the response
acknowledge = f"Pleasure to meet you {guest}. My favorite number is {thisisanumber}."
print(acknowledge)