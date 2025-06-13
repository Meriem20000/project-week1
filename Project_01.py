from datetime import datetime
print(" PERSONAL INFORMATION COLLECTOR")
first_name = input(" Enter your first name: ")
last_name = input(" Enter your last name: ")
age = input(" Enter your age: ")
city = input(" Enter your city: ")
hobby = input(" Enter your favorite hobby: ")
current_year = datetime.now().year
Birth_year = current_year - int(age)
days_lived =  int(age) * 365
next_age =  int(age) + 1

print("\n YOUR PROFILE \n")
print("Name: " + first_name + " " + last_name)
print("Age: " + age + " years old ")
print("Location: " + city )
print("Hobby: " + hobby )
print("Birth Year: " + str(Birth_year))
print("Days Lived: " + str(days_lived)+" days" )
print("Next Birthday: You'll be " +str(next_age) + "! \n " )

print(" Welcome to Python programming, Alice!")


