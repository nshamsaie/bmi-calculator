from functions import *
def main():
    """Main function to calculate BMI and determine the category."""
    try:
        weight = float(input("Enter your weight in kgs: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        if isinstance(bmi, str):
            print(bmi)
        else:
            category = determine_bmi_category(bmi)
            print(f"Your BMI category is: {category}")
            print(f"Your BMI is: {bmi}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
