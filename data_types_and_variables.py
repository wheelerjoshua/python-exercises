# movies = {'movie': ['The Little Mermaid', 'Brother Bear', 'Hercules'], 'days rented': [3, 5, 1]}
# rent = 0
# for n in movies['days rented'] rent + n * 3 
# print(rent)
movie_a = 3
movie_b = 5
movie_c = 1
price = 3
total_rent = (movie_a + movie_b + movie_c) * price
print(total_rent)

#################################################################################

time_sheet = {'Company': ['Google', 'Amazon', 'Facebook'], 'Rate': [400, 380, 350], 'Hours Worked': [10, 6, 4]}
print(time_sheet)
co_a_rate = 400
co_b_rate = 380
co_c_rate = 350
hours_worked_a = 10
hours_worked_b = 6
hours_worked_c = 4
week_income = co_a_rate * hours_worked_a + co_b_rate * hours_worked_b + co_c_rate + hours_worked_c
print(week_income)

#################################################################################

can_student_enroll = False
class_full = False
is_schedule_conflicted = False
if class_full == False and is_schedule_conflicted == False:
    can_student_enroll = True
print(can_student_enroll)

#################################################################################

offer_applied = False
offer_expired = False
total_items = 1
premium_member = True
if offer_expired == False and total_items > 2 or premium_member == True:
    offer_applied = True
print(offer_applied)

#################################################################################

username = ' codeup'
password = ' notastrongpassword'


# Bonus
if username[0] == ' ':
    username = username.strip()
    print('Username cannot contain spaces')
if password[0] == ' ':
    password = password.strip()
    print('Password cannot contain spaces')
#

password_min = False
if len(password) >= 5:
    password_min = True
username_max = False
if len(username) <= 20:
    username_max = True
password_unique = False
if password != username:
    password_unique = True

password_security = [password_min, username_max, password_unique]
print(password_security)

if all(password_security) == True:
    print("Your username and password follow the rules")

