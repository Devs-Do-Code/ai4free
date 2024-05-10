# Import the generate function from liaobots.py
from t import generate

# Use the generate function
response = generate("What is the weather like today?", system_prompt="Please provide a detailed forecast.")

# Print the response
print(response)