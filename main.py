def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."

def determine_bmi_category(bmi):
    """Determine the BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """Main function to calculate BMI and determine the category."""
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        if isinstance(bmi, str):
            print(bmi)
        else:
            category = determine_bmi_category(bmi)
            print(f"Your BMI is: {bmi}")
            print(f"Your BMI category is: {category}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
