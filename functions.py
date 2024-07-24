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
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "uormal weight"
    elif 25 <= bmi < 29.9:
        return "overweight"
    else:
        return "obesity"
