#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Defines function with a single parameter that checks if a number or string is 2, returning a boolean value accordingly
def is_two(x):
    # Checks if the passed argument is a 2 while converting any string '2' into an integer.
    if int(x) == 2:
        # If argument is 2 or '2', returns true
        return True
    # If argument is not 2 or '2', returns false
    else:
        return False


is_two(2)
is_two('2')
is_two('3')
is_two(3)


# Passing arguments through this function will return True or False depending on if the argument is equal to 2. The function converts strings temporarily into an integer during this check. Passing 2 and '2' through the function returns a True statement, while anything else, such as 3 or '3', will return False.

# In[7]:


# Defines a function that passes a single string parameter and returns a boolean value.
def is_vowel(x):
    # Temporary sets the argument in lowercase and checks if it is within a list of defined vowels
    if x.lower() in ['a','e','i','o','u']:
        # If the argument is in the list, True is returned
        return True
    # If the argument is not in the list, False is returned
    else:
        return False

    
is_vowel('E')
is_vowel('a')
is_vowel('B')
is_vowel('zed')
is_vowel('Utopia')


# The function takes in a single character string and returns True or False depending on if the argument being passed is within a list of vowels. The argument is temporarily set in lowercase to reduce the size of the list needed to check for potentially capitalized arguments. Multicharacters strings will return False.

# In[8]:


# Defines a function taking in a single string and returns a boolean value.
def is_consonant(x):
    # Utilizes previously defined function is_vowel to check if the argument passed is a vowel. If the argument is
    # not a vowel, False is returned. If False is returned, the argument is a consonant and returns True.
    if is_vowel(x) == False:
        return True
    # If the arguement passed is a vowel, the is_vowel returns True and will return a False statement
    else:
        return False

is_consonant('Y')
is_consonant('x')
is_consonant('')


# This function utilizes the previously defined is_vowel function, passing an argument to it to retrieve a True or False value. A False value from the is_vowel means the argument is a consonant and will return a True value.

# In[10]:


# Defines a function that takes in a string, preferably a single word, and returns a string.
def capitalize_word_starting_consonant(word):
    # This exploratory line of code is to ensure that any leading white space will not interrupt the capitalization
    word = word.strip()
    # The first character in the argument is passed through the is_consonant function and if it is returned True
    # the word is capitalized and returned.
    if is_consonant(word[0]):
        return word.capitalize()

capitalize_word_starting_consonant('python')
capitalize_word_starting_consonant('otis')
capitalize_word_starting_consonant('character')
capitalize_word_starting_consonant('Bear')


# This function utilizes the is_consonant function to check if the first character in the argument is a consonant. If this returns True, the word is capitalized.

# In[1]:


# Defines a function that takes in two numbers, either both float or a float and an integer, and returns a float
def calculate_tip(percentage, bill_total):
    # This checks if the argument passed for percentage is valid, a decimal between 0.0 and 1.0
    if 0 <= percentage <= 1:
        # Calculates the tip by multiplying the bill_total and percentage arguments and adding it to the bill_total
        # this value is then returned. In case of longer decimal values, the total is rounded to the second decimal
        return round((percentage * bill_total), 2)
    
    
calculate_tip(0.20, 20)
calculate_tip(0.15, 30)
calculate_tip(30, 0.15)
calculate_tip(bill_total=30.50, percentage=0.15)


# This function is used to calculate a tip passing two arguments that are the desired percentage and the bill_total. These may both be float values, but the percentage must be a float. The function checks if the percentage passed is a reasonable tip amount between 0 and 1 then multiplies the percentage and the bill_total together and adds it to the bill_total to return the bill and tip totaled together. This number is rounded to the second decimal due to this being used for monetary transactions.

# In[21]:


# Defines function that takes in two numbers, at least one is a float, and returns a float.
def apply_discount(original_price, discount_percent):
    # Returns the value of the discounted price, which is calculated by the 
    # original_price being multiplied by the discount_percent being subtracted from the original_price
    return original_price - (original_price * discount_percent)

apply_discount(100,.25)
apply_discount(50, .10)
apply_discount(.75, 10)


# This function is used to apply a discount, subtracting the discounted price from the original price. The discounted price is calculated by multiplying the discount_percentage and the original_price. The discounted price is returned. Mixing up the discount and the price when passing them to the function results in a negative number.

# In[2]:


# Defines a function that takes in a string and returns an int
def handle_commas(number):
    # Defines a variable that is the passed argument with the commas being replaced by an empty string, removing the commas
    clean_number = number.replace(',','')
    # The clean_number is returned as an float
    return float(clean_number)


# In[ ]:


total = 0


# This function passes a string of a number with commas and removes the commas by replacing the commas with an empty string. The resulting string is returned converted into an integer.

# In[25]:


# Defines function that takes in an integer or float and returns a string
def get_letter_grade(grade):
    # if and elif statements checking the grade and returning the appropriate letter grade as a string.
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

get_letter_grade(70)
get_letter_grade(77)
get_letter_grade(60.5)


# This function takes in a defined number grade, either an int or a float, and returns its corresponding letter grade as a string. It does this by passing the number provided through a series of if statements, returning what letter grade is in the if statement that is True. 

# In[27]:


# Defines a function that takes in a string and returns a string
def remove_vowels(to_remove):
    # defines a new variable with an empty string
    new_string = ''
    # For loop that checks each character in the string
    for character in to_remove:
        # Checks if each character is a vowel using the is_vowel function
        if is_vowel(character) == False:
            # if the character is not a vowel, it is added to the new_string
            new_string += character
    return new_string
        

remove_vowels('alphabet soup')
remove_vowels('aaaaa')
remove_vowels('bbbbb')


# This function takes in a string and returns a string with the vowels removed. This is accomplished by creating a new_string variable with an empty string and a for loop that checks if each character in the argument is a vowel using the is_vowel function. If the character is not a vowel, it is added to the new_string. The new_string is returned. A string of vowels returns an empty string.

# In[1]:


# List to define the alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Defines function that takes in a string and returns a string
def normalize_name(name):
    # While loop ensures first character is a letter
    while name[0].isalpha() == False:
        name = name[1:]
    # Defines a variable with an empty string
    new_name = ''
    # Loop that will pass each character in the original string
    for character in name:
        # if the character is in the alphabet or a space, it is added to the new string.
        if character.lower() in alphabet or character == ' ':
            new_name += character.lower()
    # Strips the new_name string of any trailing white spaces
    new_name = new_name.strip()
    # Loop that checks each character in the new_string
    for character in new_name:
        # If the character in the new_string is a space, it is replaced with an underscore
        if character == ' ':
            new_name = new_name.replace(' ','_')
    # the new_name string is returned    
    return new_name

normalize_name('Name')
normalize_name('First Name')
normalize_name('% Completed')
normalize_name('13_this is A VALID python IDenTiFIER')
normalize_name('True')


# This function normalizes names, passing a string and returning a string. Each character in the argument is checked to see if they are in the alphabet or a space and is added to an empty new_string variable. This variable is then stripped of leading or trailing white spaces and passed through another for loop to check each character for any remaining spaces. These are then replaced with an underscore and the new_name string is returned.

# In[28]:


# Defines function that takes in a list and returns a list.
def cumulative_sum(numbers):
    # Creates a new empty list
    new_numbers = []
    # Defines a total to track, starting from 0
    total = 0
    # for loop that passes each number in the list
    for n in numbers:
        # adds each number to the total
        total += n
        # appends the total to the empty list new_numbers
        new_numbers.append(total)
    # returns the new list with a cumulative sum of the numbers in the list passed as the argument    
    return new_numbers

cumulative_sum([1,1,1])
cumulative_sum([1,2,3,4])


# This function takes in a list and returns a list. The function adds up numbers in a list, creating a list of the cumulative sums, giving the total for each number in the list.

# ### Bonus

# In[71]:


# Define function that takes in a string and returns a string
def twelveto24(time):
    # Defines variable with empty string
    converted = ''
    # for loop that checks each character in argument
    for char in time:
        # if the character is a number it is added to the variable converted
        if char.isnumeric():
            converted += char
        # if the character is a p (for 'pm'), 1200 is added to the time
        elif char == 'p':
            # 1200 is added to the time by converting the string into 
            # an integer then adding 1200 and then converting back into
            # a string.
            converted = str(int(converted) + 1200)
    # Checks if the time is a (for 'am') and less than 10:00am (1000 converted)
    if time[-2] == 'a' and int(converted) < 1000:
        #adds a leading 0 to fulfill the 24 hour format 0123 in the first 9 hours
        converted = '0' + converted
    # Checks if time has reached the next day, converting '24' into '00'
    if converted[:2] == '24':
        converted = converted.replace('24','00')
    converted = converted[:2]+':'+converted[2:]
    # returns completed converted time in 24hr format
    return converted
    
    
twelveto24('10:45pm')
twelveto24('12:00pm')
twelveto24('1:00am')
twelveto24('10:45am')
        


# In[69]:


# Defines function that passes a string and returns a string
def twentyfourtotwelve(time):
    # Stores argument into an integer
    time_int = int(time)
    # creates an empty string
    converted = ''
    # for use in future if statement to convert between am/pm
    is_pm = False
    # If time is after noon, subtract 1200 to give the correct 12hr hour
    # changes is_pm to True
    if time_int > 1200:
        time_int = time_int - 1200
        is_pm = True
    # for loop to add every character of the altered time into the string
    for char in str(time_int):
        converted += char
    # If it is in the afternoon, add 'pm'
    if is_pm == True:
        converted += 'pm'
    # If it is in the morning, add 'am'
    else:
        converted += 'am'
    # If it is a time between 1-9, adds the colon in the proper place
    if len(converted) == 5:
        converted = converted[:1] + ':' + converted[1:]
    # If it is a time between 10-12, adds colon in proper place
    else:
        converted = converted[:2] + ':' + converted[2:]
    # return converted time in 12hr format
    return converted
    
twentyfourtotwelve('0100')
twentyfourtotwelve('1400')
twentyfourtotwelve('2345')


# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

# In[83]:


# Defines function that passes a string and returns an int
def col_index(column):
    # Define variable for the number
    number = 0
    # Checks each character in the argument passed
    for char in column:
        # Makes sure the character is a letter
        if char.isalpha():
            # Calculates the difference in unicode characters and adds 1 (spreadsheet base is 1)
            # Loop ensures multiple characters in argument get multiplied by the previous result as
            # the alphabet has been looped through that many times.
            number = number * 26 + (ord(char.upper()) - ord('A')) + 1
    return number

col_index('A')
col_index('B')
col_index('AA')
col_index('AAA')


# In[ ]:





# In[ ]:




