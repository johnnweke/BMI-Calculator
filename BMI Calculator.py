print("Let's calculate your Body Mass Index, shall we?")

height_str = input("Enter your height in feet: ")
weight_str = input('Enter your weight in pounds: ')
height_int = float(height_str)
weight_int = float(weight_str)
body_mass_index_long = weight_int * 703 / ((height_int *12) ** 2)  # This gives a long number. Shorten it.

# I will create a truncate function that will multiply the decimal by 100
# take the integer of that number and divide the result by 100.

def truncate(bmi):
    return (int(bmi * 100) / 100)


body_mass_index = truncate(body_mass_index_long) #Now BMI should be 2 dec places.

print(f'\n Your Body Mass Index is {body_mass_index} \n')

# If Statement for BMI
if body_mass_index < 18.5:
    print("You may be under-weight")
elif (body_mass_index >= 18.5) and (body_mass_index < 24.9):
    print(f'You are at a healthy weight!')
elif (body_mass_index >= 24.9) and (body_mass_index < 29):
    print(f'You may be overweight')
else:
    print(f'You may be obese, and this could affect your health. \n '
          f'You may need to take some necessary steps to get back to a healthy weight.')
