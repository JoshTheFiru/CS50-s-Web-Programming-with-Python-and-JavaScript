# CHAPTER 2 - PYTHON

## Generalities on Python

Python is a multipurpose programming language, which makes it easy to build web pages and applications quickly.
It's documents have the .py extension

    nameFile.py

To run Python, you need to run a program in your terminal that also happens to be called Python. Python is what you might call an interpreted language, meaning we run a program called Python which is an interpreter that is going to read our .py file line by line. So for running a Python file, in your terminal:

    python nameFile.py

## Variables

Unlike other languages like C or Java, where you have to specify the type of every variable you create, Python does not require you to tell what the types of each of the variables actually are. So some examples of declaration and initialization of variables could be:

    a = 28
    b = 1.5
    c = "Hello!"
    d = True
    e = None

So Python by itself is able to infer what the types of any of these values happen to be without specifying it. **Values have types**, you just don't need to explicitly tell Python. Types of the above values would be:

    a = 28              //int
    b = 1.5             //float
    c = "Hello!"        //str
    d = True            //bool
    e = None            //NoneType

The NoneType is a special type in Python which only has one possible value. None is a value we use when we want to represent the lack of a value somewhere. There are more types of variables than these. This [link](https://www.w3schools.com/python/python_datatypes.asp) from W3Schools goes in deep in this subject.

## [Conditions](conditions.py)

Conditions, as in many other languages, consist of if control structures that allow programmers to execute blocks of code depending on an condition that will evaluate at the beggining of the structure.

So, if we would like to create a condition structure:

    if condition: 
        code to execute
    elif condition:             //else-if condition in Python
        code to execute
    else: 
        code to execute

The difference with other languages like C or Java, is that the condition to evaluate is not between parenthesis (), and there are no curly brackets to limit the blocks of code, all we need to do is to put a semicolon :, to indicate that the condition is the one untill that point, and then indent the code to execute under that codition. With that indentation, Python determines the block of code to execute.

## [Sequences](sequences.py)

One of the most powerful features of Python is its various different types of sequences, which are data types that store values in some sort of sequence or some collection of values altogether.

There are a number of different types of sequences that all obey similar properties. One of these is the type string. This means if I have something like:

    name = "Harry"

This sequence allows me to access to every individual element inside the sequence. It works similar to arrays in other languages.

Another type of sequence is the **tuple**. Often used if you have a couple of values that aren't going to change but you need to store them, won't necesarily be two of them, can be more.

**list** are another type of sequence data structure. Lists are sequences of mutable values. Mutable meaning we can change elements in the list, I can add something to the end of the list, I can delete something from the list, or I can modify the values inside the list.

**tuple** as we have seen, are sequences of unmutable values. Meaning I won't be able to change the elements in that data structure.

**set** is a collection of unique values, stored in no particular order. Every value appears exactly once in this data structure.

**dict** A collection of key-value pairs, kind of a dictionary like structure. The syntax of the dictionary will be:

    nameOfDictionary = {Key:Value, Key:Value}

Then to refer to some of the keys to get its value, you can do:

    print(nameOfDictionary[Key])

## [Loops](loops.py)

Loops enable us to loop through any type of sequence. Its syntax is slightly different from other languages like C or Java, as it adapts to Python style:

    for i in sequenceToIterate:
        print(i)

As happened with the conditionals and with almost every structure in Python, we don't have curly brackets {} to delimite the code blocks, and this goes through the identation, and the semicolon :, which marks the start.
