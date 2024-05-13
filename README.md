# Python Fundamentals!


### Commenting in your IDE
You can create comments in your code 
in two ways:<br>
Using `# (This is a comment)`<br>
or <br>
Using `""" (Your comment goes here) """`

--------
### Data Types
There are three main data types in Python: 
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <br> 
1) **Numbers** (This is broken down into two subcategories)<br>
   1) **Integers**- which are whole numbers, `eg. 10 or 67` (Use **int()** to cast data to integer)<br> 
   2) **Floats**- which handle decimal numbers, `eg. 13.4 or 91.25` (Use **float()** to cast data to float)<br>
2) **Strings**- characters or text `←That can be string- and so can this!` (Use **str()** to cast data to string)<br>
3) **Boolean**- representing a value that is either `True` or `False`.<br>

Python will detect the data type of data you have inputted and 'class' them <br>
as the detected type. You can also view what data type python has assigned to your data using the 'type' function. <br>
Here's an example:<br>
![Data Types example]( https://drive.google.com/file/d/1_54AaPA7eaQw0ZtvATuMxzXpqYTZxTHf/view?usp=drive_link "Data types screenshot")


--------
### Numbers & Math Operators
Most programming languages have the same math operators:

Operator:&nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; Function:&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; |  &nbsp; &nbsp; &nbsp; Example:<br>
&nbsp; &nbsp; &nbsp;  +  &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Add &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |   &nbsp; &nbsp; &nbsp; 10 + 10 (20)<br>
&nbsp; &nbsp; &nbsp;  -  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; Subtract&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;|  &nbsp; &nbsp; &nbsp; 20 - 10 (10)<br>
&nbsp; &nbsp; &nbsp;  * &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; Multiply&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;|   &nbsp; &nbsp; &nbsp; 10 * 10 (100)<br> 
&nbsp; &nbsp; &nbsp;  / &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Divide&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;  &nbsp; &nbsp;|  &nbsp; &nbsp; &nbsp; 100 / 20 (5)<br>
&nbsp; &nbsp; &nbsp;  % &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Modulo&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|  &nbsp; &nbsp; &nbsp; 20 % 6 (2)<br>

<i class="fas fa-lightbulb"></i>
<i class="fas fa-lightbulb" style="color: yellow; font-size: 24px;"></i>
Modulo calculates the remainder of a division operation. So in the example above, 6 goes into 20 three times, and leaves 2 remaining. Thus, the example above returns 2.<br>


### Strings & Python Characters
#### Indexing
The python interpreter does not see words, sentences or characters. It sees the data we input as unicode characters within quotes. <br>
Since a python string is interpreted as a list of characters, we are able to use indexing to access them.<br>
Here's an example:<br>
`print("This is a string"[6]) ` This will return: ` s`<br>
In the example, we use the square brackets to indicate the index of the character we would like to be returned. This is true for all indexing. <br>
Indexing always begins at 0, so if we wanted to return the first character of the string, we would use: `print("This is a string"[0]) ` This will return: ` T`<br>
You can also index backwards! If we wanted to return the last letter of our string, we would use: `print("This is a string"[-1]) ` This will return: ` g`

We can also access the length of the string using the 'len()' function. This is a built-in function (like 'print()' or 'type()') and it allows to get the length of a particular object.
Here's an example:<br>
`print(len("This is a string")) ` This will return: ` 16`<br>
<br>
### Boolean Values
A boolean value can only be `True` or `False` (Note: boolean values are capitalised) <br>
With boolean, 0 equates to False, and 1 equates to True.<br> 
But any value other than 0 will equate to True.

Boolean values are also generated from equality operators. Equality operators are operators that validate an argument, and return True, or False.

Most programming languages have the same equality operators:

Operator: &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Function:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|  &nbsp; &nbsp; &nbsp; Example:<br>
&nbsp; &nbsp; &nbsp;  == &nbsp; &nbsp;&nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Equal to&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|   &nbsp; &nbsp; &nbsp; 10 == 10 (True)<br>
&nbsp; &nbsp; &nbsp;  != &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Not equal to &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|  &nbsp; &nbsp; &nbsp; 20 != 10 (True)<br>
&nbsp; &nbsp; &nbsp;  > &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Greater than&nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; |   &nbsp; &nbsp; &nbsp; 20 > 10 (True)<br> 
&nbsp; &nbsp; &nbsp;  < &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Less than&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |  &nbsp; &nbsp; &nbsp; 100 < 20 (False)<br>
&nbsp; &nbsp; &nbsp;  >= &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; Greater than or equal to&nbsp; &nbsp; &nbsp; |  &nbsp; &nbsp; &nbsp; 20 >= 6 (True)<br>
&nbsp; &nbsp; &nbsp;  <= &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Less than or equal to &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|  &nbsp; &nbsp; &nbsp; 20 <= 6 (False)<br>

-------

### Variables

A variable is a reserved memory location that allows us to store datatypes and objects. <br>
They are mutable, so they can be changed and/or overwritten.
#### Variable names
The names of variables are very important. Here are few stand-out rules:<br>
+ It should describe the data it is storing
+ If your variable is more than one word, it should use snake-casing: `this_is_snake_casing`
+ It should not start with a literal (our core datatypes, eg. a number; 10, a string "like this" etc. )<br>

Here's the PEP8 style guide for Python code: [PEP8 Style Guide](https://peps.python.org/pep-0008/)

-----

### Concatenation

To concatenate is to join strings together to form a new string.
To do this, we use the `+` operator.
Here's an example:<br>
Here are two variables:<br>
`first_name = "John"`<br>
`last_name = "Doe"`<br>
Now let's concatenate them to form a variable called 'full_name':<br>
`full_name = first_name + last_name`<br>
Now let's print this:`print(full_name)`<br>
This will return: `JohnDoe`<br>
If we want to print this with a space between the first and last name, we add an empty string between them:<br>
`full_name = first_name + " " + last_name`<br>
`print(full_name)`<br>
This will print: `John Doe`

-----
### Collections

Collections allow us to store large amounts of data. There are two main formats of collections in Python; Lists and Dictionaries.<br>
#### Lists<br>
Lists(arrays) are index-based



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>



