"""Mini-Profile Generator"""

# 1. Define a Function for the Profile & Calculations

def generate_profile(age):
    """Function to determine user life stage

    - If the age is between 0 and 12, return "Child"
    - If the age is between 13 and 19, return "Teenager"
    - If the age is 20 or older, return "Adult"
    """
    age = int(age)

    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"


# 2. Get user Input

# Greeting the user and asking for a full name
print('Welcome to Mini-Profile Generator! Please enter your full name:')

# Variable for user full name
username = input()

# Asking user for a birth year
print(f'{username}, please enter your birth year:')

# Variable for user birth year
birth_year_str = input()
birth_year = int(birth_year_str)

# User current age calculation
current_year = 2025
current_age = int(current_year - birth_year)

# List for user hobbies
hobbies = []

# Loop for entering a hobbie till the "stop" word is written
while True:
    print("Enter a favorite hobby or type 'stop' to finish:")
    hobby = input()

    if hobby.lower() != "stop": # If case-insensitive "stop" is not entered -> loop continues
        hobbies.append(hobby)
    else:
        break # If "stop" entered -> loop ends


#3. Process and generate the Profile

# Function returns life stage of a user into the variable "life_stage"
life_stage = generate_profile(current_age)

# Dictionary to store all collected information
user_profile = dict(name = username, age = current_age, stage = life_stage, hobbies = hobbies)


#4. Display the output

# Main output
Output = (
    f'---\n'
    f'Profile Summary:\n'
    f'Name: {user_profile['name']}\n'
    f'Age: {user_profile['age']}\n'
    f'Life Stage: {user_profile['stage']}\n'
)


# List of hobbies where each written from new line
hobbies_list = "".join(f'- {hobby}\n' for hobby in user_profile['hobbies'])


# Condition for empty/ not empty hobby list
if not user_profile["hobbies"]:
    Output += "You didn't mention any hobbies.\n---\n" # Output if hobbies list is empty
else:
    Output += (
            f'Favorite hobbies ({len(user_profile["hobbies"])}):\n'
            f'{hobbies_list}'
            f'---\n'
    ) # Output if hobby list is NOT empty


print(Output)