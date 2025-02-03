# Multi-User Health Test >> supports many users checking healthiness with their personal profiles/statuses

import time

patients = []

# patient/user object definition
class Patient():
    """
    Patient object
    """

    def __init__(self, name):
        self.name = name
        self.status = None

    def __repr__(self) -> str:
        return self.name
    
    def is_sick(self):
        self.status = "Sick"
        return self.status
    
    def is_healthy(self):
        self.status = "Healthy"
        return self.status
    
    def is_critically_ill(self):
        self.status = "Critically Ill"
        return self.status

def user_input(prompt : str, user=None):
    """
    Builds on Python's in-built input function to control
    keyword inputs like `options`, `quit` and `status` directly
    """

    txt = input(prompt)
    if txt == "options":
        choice = input("1 - Switch user \n2 - Add new user \n3 - Delete user \n4 - Back \n")
        if choice == "1":
            for x, y in enumerate(patients, start=1):
                print(f"{x} - {y}")
            id = input("Select the user you want to switch to: ")
            patient = patients[int(id)-1]
            home(patient)
        elif choice == "2":
            patient = register_user()
            home(patient)
        elif choice == "3":
            for x, y in enumerate(patients, start=1):
                print(f"{x} - {y}")
            id = input("Select the user you want to delete: ")
            print("deleting user...")
            time.sleep(.7)
            patients.pop(int(id)-1)
            print("done")
            patient = register_user()
            home(patient)

        # 4 or any other button would go back

    elif txt == "status":
        if user:
            if user.status:
                print(f"Your status is: {user.status}")
            else:
                print("You have not taken the test yet.")
        else:
            print("You don't have a profile yet!")

    elif txt == "quit":
        print("Exitting..")
        time.sleep(1)
        exit()
    else:
        return txt

def register_user() -> Patient:
    name = user_input("Tell us your name: ")
    if name:
        patient = Patient(name)
        print("registering user...")
        patients.append(patient)
        time.sleep(1)
        print("done")
        time.sleep(.5)
        return patient
    else:
        return register_user()  # -- recursive func.
    
def home(user : Patient):
    """
    View or interface of a specific user
    """

    print(f"Hello {user.name}")
    print("......................................")
    time.sleep(1)
    if not user.status:
        res = user_input("Take test now? Y - Yes | options | status | quit \n", user)
    else:
        res = user_input("Take test again? Y - Yes | options | status | quit \n", user)

    if res == "Y":
        health_test(user)
    else:
        home(user)

def health_test(user : Patient):
    """
    Compares body data provided by patients or users with
    the average human and computes the health status of patient.
    """

    # BMI would be given 40% impact on overall health and body temperature would be given 60% impact
    # Say Critically ill => -1, Sick => 0, Healthy => 1

    height = float(input("Input your height in metres: "))
    weight = float(input("Input your weight in Kg: "))
    bmi = weight/height**2

    if 17 <= bmi <= 29:
        # Normal weight => Healthy
        status_index = 1*40
    elif bmi < 13 or bmi >= 40:
        # Extremely underweight or severely obese => Critically ill
        status_index = -1*40
    else:
        # Severly undrweight or severely obese => Sick 
        status_index = 0*40
  
    temperature = float(input("Input your body temperature in deg Celsius: "))

    if 35.5 <= temperature <= 37.5:
        # healthy
        status_index = (1*60+status_index)/100
    elif temperature < 32 or temperature > 40:
        # critical
        status_index = (-1*60+status_index)/100
    else:
        # sick
        status_index = (0*60+status_index)/100

    if round(status_index) == -1:
        user.is_critically_ill()
    elif round(status_index) == 0:
        user.is_sick()
    else:
        user.is_healthy()

    print(f"You are {user.status}\nThanks for taking the test")
    time.sleep(1)
    home(user)

# RUNNING STARTS

print("__________________________________________\n")
print("Welcome to the Health Checking Model")
time.sleep(.5)
print("Help: Input 'options' for options, 'status' to check your current status and 'quit' to end the excercise")
time.sleep(1)

user = register_user()

# Home
home(user)