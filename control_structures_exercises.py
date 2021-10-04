################# 1a.
day_of_week = input('Input a day of the week: ')
if day_of_week.lower() == 'monday':
    print('It is Monday.')
else:
    print('It is not Monday.')

################# 1b.
day_of_week = input('Input a day of the week: ')
weekdays = ['monday', 'tuesday', 'wednesday','thursday','friday']

if day_of_week.lower() in weekdays:
    print(day_of_week, 'is a weekday.')
else:
    print(day_of_week, 'is a weekend.')

################# 1c.
hours_in_week = 41
hourly_rate = 15
if hours_in_week > 40:
    overtime = hours_in_week - 40
    overtime_pay = overtime * (hourly_rate * 1.5)
    weekly_paycheck = (hours_in_week - overtime) * hourly_rate + overtime_pay
else:
    weekly_paycheck = hours_in_week * hourly_rate
print(weekly_paycheck)

################# 2a.
i = 5
while i <= 15:
    print(i)
    i += 1

i = 2
while i in range(0,101):
    print(i)
    i += 2

i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i < 100000:
    print(i)
    i = i ** 2

i = 100
while i >= 5:
    print(i)
    i -= 5

################# 2b.
n = int(input('Enter a number: '))
for l in range(0,10):
    print(n, 'x', l, '=', n * l)

n = '1'
for l in range(1,10):
    print(n * l)
    n = int(n)
    n += 1
    n = str(n)


################# 2c.
odd_between_one_and_fifty = input('Enter an odd number between 1 and 50: ')
while odd_between_one_and_fifty.isdigit() == False or int(odd_between_one_and_fifty) > 50 or int(odd_between_one_and_fifty) < 1 or int(odd_between_one_and_fifty) % 2 != 1:
    print('You have entered an invalid number.')
    odd_between_one_and_fifty = input('Enter an odd number between 1 and 50: ')
    if odd_between_one_and_fifty.isdigit() == True and int(odd_between_one_and_fifty) < 50 and int(odd_between_one_and_fifty) > 0 and int(odd_between_one_and_fifty) % 2 == 1: 
        odd_between_one_and_fifty = int(odd_between_one_and_fifty)
        break

odd_between_one_and_fifty = int(odd_between_one_and_fifty)
#type(odd_between_one_and_fifty)
print('Number to skip is: ', odd_between_one_and_fifty)
for odd_number in range(1,50):
    if odd_number == odd_between_one_and_fifty:
        print('Yikes! Skipping number: ', odd_number)
 #       continue
 #   if odd_number % 2 == 1:
  #          if odd_number != odd_between_one_and_fifty:
   #             print('Here is an odd number: ', odd_number)
    else:
        print('Here is an odd number: ', odd_number)
    

################# 2c.
count_to = input('Enter a positive number to count to: ')
while count_to.isdigit == False or int(count_to) < 1:
    count_to = input('Please enter a positive number: ')
    

################# 2d.    
count_to = int(count_to)
for number in range(0,count_to + 1):
    print(number)
    if number == count_to:
        break

################# 2e.
positive_integer = input('Enter a positive integer: ')
while positive_integer.isdigit == False:
    positive_integer = input('Please enter a positive integer: ')
positive_integer = int(positive_integer)
for number in range(positive_integer, 0, -1):
    print(number)

################# 3. Fizzbuzz
for number in range(1,101):
    if number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')


################# 4. 
user_continue = True
while user_continue == True:
    user_integer = int(input('What number would you like to go up to? '))
    print('Here is your table!')
    print('number | squared | cubed \n------ | ------- | -----')
    for number in range(1, user_integer + 1):
        print('%-7i| %-8i| %-7i' % (number, number ** 2, number ** 3))
    user_continue = input('Would you like to continue? Enter y or n: ')
    if user_continue.lower() == 'y' or user_continue.lower() == 'yes':
        user_continue = True
    else:
        print('Thanks for playing!')
        user_continue = False

################# 5.
user_continue = True
while user_continue == True:
    user_grade = int(input('Enter grade from 0 - 100: '))
    if 88 <= user_grade <= 100:
        if 99 <= user_grade <= 100:
            print('Your grade is an A+')
        elif 88<= user_grade <= 89:
            print('Your grade is an A-')
        else:
            print('Your grade is an A')

    elif 80 <= user_grade <= 87:
        if 86 <= user_grade <= 87:
            print('Your grade is a B+')
        elif 80<= user_grade <= 81:
            print('Your grade is a B-')
        else:
            print('Your grade is a B')

    elif 67 <= user_grade <= 79:
        if 78 <= user_grade <= 79:
            print('Your grade is a C+')
        elif 67<= user_grade <= 68:
            print('Your grade is a C-')
        else:
            print('Your grade is a C')
    elif 60 <= user_grade <= 66:
        if 65 <= user_grade <= 66:
            print('Your grade is a D+')
        elif 60<= user_grade <= 61:
            print('Your grade is a D-')
        else:
            print('Your grade is a D')
    else:
        print('Your grade is an F')
    user_continue = input('Would you like to continue? Enter y or n: ')
    if user_continue.lower() == 'y' or user_continue.lower() == 'yes':
        user_continue = True
    else:
        print('Thanks for playing!')
        user_continue = False


###################### BONUS
books_ive_read = [
    {
        'Title': 'Metamorphosis',
        'Author': 'Franz Kafka',
        'Genre': 'Thriller'
    },
    {
        'Title': 'House of Leaves',
        'Author': 'Mark Z. Danielewski',
        'Genre': 'Horror'
    },
    {
        'Title': 'Frankenstein',
        'Author': 'Mary Shelley',
        'Genre': 'Horror'
    },
    {
        'Title': 'Things Fall Apart',
        'Author': 'Chinhua Achube',
        'Genre': 'Historical Fiction'
    },
    {
        'Title': 'The Lord of the Rings',
        'Author': 'J.R.R. Tokien',
        'Genre': 'Fantasy'
    },
    {
        'Title': 'Scott Pilgrim',
        'Author': 'Brian Lee O\'Malley',
        'Genre': 'Action'
    }
]

for book in books_ive_read:
    print(book['Title'],'by',  book['Author'], 'is a',book['Genre'], 'book.')
    
user_genre = input('Please enter a genre: ').capitalize()
for book in books_ive_read:
    if book['Genre'] == user_genre:
        print(book['Title'],'by',  book['Author'], 'is a',book['Genre'], 'book.')
