# Python program demonstrating different conditional statements

def weather_advice(temperature, weather):
    print(f"Temperature: {temperature}°C, Weather: {weather}")
    
    # Simple if statement
    if temperature > 30:
        print("It's hot outside! Stay hydrated.")
    
    # If-else statement
    if weather == "rainy":
        print("Take an umbrella!")
    else:
        print("No need for an umbrella today.")
    
    # Elif statement
    if temperature < 10:
        print("It's freezing! Wear a heavy jacket.")
    elif 10 <= temperature < 20:
        print("It's cool. A light jacket should be fine.")
    elif 20 <= temperature < 30:
        print("The weather is pleasant!")
    else:
        print("It's warm outside!")
    
    # Nested if statement
    if weather == "snowy":
        if temperature < 0:
            print("It's snowing and freezing! Stay indoors if possible.")
        else:
            print("Light snow outside. Be cautious!")
    
    # Ternary (conditional) operator
    outfit = "Wear sunglasses!" if weather == "sunny" else "No sunglasses needed."
    print(outfit)

# Test cases
test_cases = [(35, "sunny"), (15, "cloudy"), (5, "rainy"), (-5, "snowy")]
for temp, weather in test_cases:
    print("\n==============================")
    weather_advice(temp, weather)
