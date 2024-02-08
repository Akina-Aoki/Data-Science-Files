#!/usr/bin/env python
# coding: utf-8

# # Python Functions for Beginners
# 
# 
# ## Objectives
#  
# 1. Describe the function concept and the importance of functions
# 2. Write a function that takes inputs and performs tasks
# 3. Use built-in functions like len(), sum(), and others effectively
# 4. Define and use your functions in Python
# 5. Differentiate between global and local variable scopes
# 6. Use loops within the function
# 7. Modify data structures using functions
# - Function to append an element
# - Function to remove an element
# - Modifying lists
# - Modifying dictionaries
# - Modifying sets
# 
# 
# ### Introduction to functions
# 
# #### Definition
# 
# A function is a fundamental building block that encapsulates specific actions or computations. As in mathematics, where functions take inputs and produce outputs, programming functions perform similarly. They take inputs, execute predefined actions or calculations, and then return an output.
# 
# #### Purpose of functions
# 
# Functions promote code **modularity and reusability.** Imagine you have a task that needs to be performed multiple times within a program. Instead of duplicating the same code at various places, you can define a function once and call it whenever you need that task. This **reduces redundancy** and makes the code easier to manage and maintain.
# 
# #### Benefits of using functions
# 
# **Modularity:** Functions break down complex tasks into manageable components
# **Reusability:** Functions can be used multiple times without rewriting code
# **Readability:** Functions with meaningful names enhance code understanding
# **Debugging:** Isolating functions eases troubleshooting and issue fixing
# **Abstraction:** Functions simplify complex processes behind a user-friendly interface
# **Collaboration:** Team members can work on different functions concurrently
# **Maintenance:** Changes made in a function automatically apply wherever it's used

# Example:
# 
# **Inputs(Parameters)** Inputs are known as parameters or arguments. Parameters provide functions with the necessary information they need to perform their tasks.
# 
# **Tasks**  The purpose of a function determines the tasks it performs. 
# 
# **Producing outputs** The output is the result of the operations carried out within the function. It's the value that the function “returns” to the code that called it. Think of the output as the end product of the function's work.

# In[ ]:


def calculate_total(a,b):      #p arameters: a and b
    total = a + b              # task
    return total              # output: sum of a and b

result = calculate_total(5, 7) # call the functions
print(result)                  # output


# ### Python's built-in functions
# 
# Python has a rich set of built-in functions that provide a wide range of functionalities. These functions are readily available for you to use.
# 
# 
# #### Built-in functions
# 
# To use a built-in function, you simply call the function's name followed by parentheses. Any required arguments or parameters are passed into the function within these parentheses. The function then performs its predefined task and may return an output you can use in your code.
# 
# Python's built-in functions offer a wide array of functionalities, from basic operations like len() and sum() to more specialized tasks.
# 

# In[ ]:


# len() Calculates the length of a sequence or collection
str_len = len("Nice shirt!") # output: 11
int_len = len(1, 2, 3)       # output: 3


# In[ ]:


# sum(): Adds up the elements in an iterable (list, tuple, and so on)
total = sum(100 + 100)    #output: 200


# ### Defining your functions
# 
# 
# #### pass
# 
# A "pass" statement in a programming function is a placeholder or a no-op (no operation) statement. Use it when you want to define a function or a code block syntactically but do not want to specify any functionality or implementation at that moment.

# - **Placeholder:** "pass" acts as a temporary placeholder for future code that you intend to write within a function or a code block.
# 
# - **Syntax Requirement:** In many programming languages like Python, using "pass" is necessary when you define a function or a conditional block. It ensures that the code remains syntactically correct, even if it doesn't do anything yet.
# 
# - **No Operation:** "pass" itself doesn't perform any meaningful action. When the interpreter encounters “pass”, it simply moves on to the next statement without executing any code.

# In[ ]:


# Syntax:
def function_name():
    pass


# #### Parameters
# 
# - Parameters are like inputs for functions
# - They go inside parentheses when defining the function
# - Functions can have multiple parameters
# 
# Example:

# In[ ]:


def greet(name):
    print("Hello, " + name)
    
result = greet("John")
print(result)              # Output: Hello, John


# #### Return statement
# 
# - Return gives back a value from a function
# - Ends the function's execution and sends the result
# - A function can return various types of data
# 
# Example:

# In[ ]:


def add(a, b):
    return a + b

result = add(10, 4)


# ### Scopes and Variables
# 
# Understanding scope is crucial to avoid naming conflicts and to manage variable accessibility effectively. Scope refers to the accessibility of variables, objects, and functions within a program.
# 
# 
# #### Global Scope
# 
# - Variables, objects, and functions defined **outside** of any function or class have global scope.
# - Global variables and functions can be accessed from anywhere in the program, including inside functions and classes.
# - To create a global variable inside a function, you can use the global keyword.

# In[ ]:


# example

x = "Welcome"         # global variable

def greeting():
    print(x)          # access global variable inside a function
    
greeting()


# #### Local Scope
# 
# - Variables, objects, and functions defined **inside** a function or class have local scope.
# 
# - Local variables are accessible only within the function or class where they are defined.
# 
# - Local variables take precedence over global variables with the same name within the same scope.

# In[ ]:


# example

def greeting():
    y = "Hi"         # local variable
    print(y)         # accessing local variable
    
greeting()    

# Trying to access local variable outside its scope will raise NameError
# print(y)  # This will raise NameError: name 'y' is not defined


# In[ ]:


# example

x = 10              # global variable

def greeting():
    x = "Hi"        # local variable, same name as global variable
    print(x)
    
greeting()          # outout: "Hi"
print(x)            # output: 10 (global variable remains unchanged)
    


# ### Using functions with loops
# 
# Functions and loops are often used together to perform repetitive tasks or iterate over collections of data. 
# 
# - Functions group similar actions for easy understanding
# - Looping within functions keeps code clean
# - You can reuse a function to repeat actions

# In[ ]:


# for loop with function

def print_numbers(n):
    for i in range(1, n +1):     # iterate through numbers from 1 to n
        print(i)
        
print(3)  
#Output:
# 1
# 2
# 3


# In[ ]:


def greet(name):
    return "Hello, " + name     # Concatenate the string with the parameter.

for _ in range(3):              # iterate 3 times
    print(greet("John")) 
    
# Output:
# Hello, John
# Hello, John
# Hello, John


# In[1]:


# while loop with function


def countdown(n):
    while n > 0:       # continues as long as 'n' is greater than 0
        print(n)
        n -= 1         # Decrement 'n' by 1 in each iteration.

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1


# In[ ]:


# conditional statements andd functions with loop

def print_even_numbers(n):
    for i in range(1, n +1):      # Iterate through numbers from 1 to n
        if i % 2 ==0:             # use the modulo operator, if divided by 2 and remainder is 0, it's even
            print(i)
            
print_even_numbers(10)
# Output:
# 2
# 4
# 6
# 8
# 10


# In[ ]:


# Function with Loop and List Comprehension

# squares of each number
# Iterate over each number 'num' in the input list 'numbers', calculate its square 'num ** 2', and add it to the new list.

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

numbers = [1, 2, 3, 4, 5]

# Call the 'square_numbers' function with the 'numbers' list as an argument.
squared = square_numbers(numbers)
print(squared)

# Output: [1, 4, 9, 16, 25]


# ### Modify data structures using functions
# 
# Modifying data structures using functions involves defining functions that perform operations on data structures such as lists, dictionaries, sets, etc. These functions can add, remove, update, or perform any desired modification on the data structure.
# 
# 
# #### Define Functions
# ##### Modifying Lists
# 
# **Function to append an element** 
# -add_element- Start by defining functions that encapsulate specific operations to perform. This function takes two parameters.
# 
# -data_structure- This parameter represents the list to which you want to add an element. Data structures can be passed (lists, dictionaries, sets) as arguments to functions.
# 
# -element- This parameter represents the element you want to add to the list.
# 
# - Inside the function, you use the -append- method to add the provided element to the data_structure, which is assumed to be a list.

# In[ ]:


# Function to append an element to the list

def add_element(data_structure, element):
    data_structure.append(element)


# **Function to remove an element**
# -remove_element- define a function that takes two parameters.
# 
# -data_structure- This parameter represents the list to which you want to remove an element.
# 
# -element- This parameter represents the element you want to remove to the list.
# 
# -conditional statements- using the else statement, a string will be printed if the element is not found in the list.

# In[ ]:


# Function to remove an element from the list

def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")


# **Add elements to list**
# Use the -add_element- function to add three elements (10, 20, and 30) to the my_list.

# In[ ]:


# Add elements to the list using the add_element function

add_element(my_list, 10)
add_element(my_list, 20)
add_element(my_list, 30)


# **Remove elements from the list**
# Use the -remove_element- function to remove elements from the my_list. 

# In[ ]:


# Remove an element from the list using the remove_element function

remove_element(my_list, 10)
remove_element(my_list, 50)  # Conditional statement. This will print a message since 50 is not in the list


# ##### Modifying Dictionaries
# 
# **add_to_dict** function takes 3 arguments. **my_dict** the dictionary where key-value pair will be added. **key** the key to be added, and **value** corresponding to key.
# 
# **remove_from_dict** function takes 2 arguments. **my_dict** the dictionary wherein the key to be removed. If the condition is true, the **del** statement is performed which removes the key-value pair from the **my_dict.** If the key is not found, it prints a message indicating that the key was not found.

# In[ ]:


# Function to add a key-value pair to a dictionary
def add_to_dict(my_dict, key, value):
    my_dict[key] = value

# Function to remove a key-value pair from a dictionary
def remove_from_dict(my_dict, key):
    if key in my_dict:
        del my_dict[key]
    else:
        print(f"{key} not found in the dictionary.")

# Example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
add_to_dict(my_dict, 'd', 4)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

remove_from_dict(my_dict, 'b')
print(my_dict)  # Output: {'a': 1, 'c': 3, 'd': 4}


# ##### Modifying Sets
# 
# **add_to_set** function adds an element to the given set using the add method. It takes two parameters: **my_set**, which the element will be added, and **element**, the element to add.
# 
# **remove_from_set** function removes an element from the set if it exists in the set. It checks if the element is present in the set using the **in** operator. If it is, it removes the element using the **remove** method. If the element is not found using the **else** statement, it prints a message indicating that the element was not found in the set.
# 

# In[ ]:


# Function to add an element to a set
def add_to_set(my_set, element):
    my_set.add(element)
    
# Function to remove an element from a set
def remove_from_set(my_set, element):
    if element in my_set:
        my_set.remove(element)
    else:
        print(f'{element} not found in the set.')
        

# Example:
my_set = {1, 2, 3, 4}
add_to_set(my_set, 5, 6)
print(my_set)
# output: {1, 2, 3, 4, 5, 6}

remove_from_set{my_set, 2}
print(my_set)
# output: {1, 3, 4, 5, 6}

