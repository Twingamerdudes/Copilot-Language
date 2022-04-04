# Copilot Language
## Introduction
I thought it was a good idea to get github copilot to make a programming language, lol.
Basiclly, I put some rules on myself on what I could modify in this language, here they are:
I can only edit if
1. It is for debugging
2. It's super minor (liking changing [2] to [1]).
Well that's it. Time to provide Documentation I guess now.
## Documentation
### Making your first program
So first make a file and make it's file extension .cpl
Inside the file, type on the first line ` func main(){ `
Now instead the main function put :
``` ."Hello"
print -> .
spc
."World"
print -> .
```
When you run it (instructions on that below) it should print "Hello World"!
### Running your program
Just run the python file called language.py and input the path to your program
### Variable rules
In this language, there are only two variable, temp, and tempArray.
Temp is for strings while tempArray is for arrays.
To assign to temp do this:
`.(string)`. To assign to tempArray, do this:
`array = [(stuff, seprate with a comma)]`
Then to print a value of the array you must do:
`.array[(index)]`
### String rules
So, when your assigning a string to a variable, there are a few requirments.
1. It can not contains any spaces, use the `spc` function to use them.
2. You cannot do new lines, you must use the `nl` function.
3. It must have qoutes around it
Well, that's it for variables and strings.
### Calling functions
Fun fact: you can call other functions.
So to use other functions, make another function below your func main function and type `func (name)`
Now inside your main function type in `call (name)`
It's as easy as that.
### Using math
So, math is necessary for any language, so let's use it!
First make sure your temp var is a number like 2
Next, type in `math + 5' `
This will add 5 to temp!
Now print temp. You should get 7 if you made temp 2
You can also use these operators `- * / %`
### Importing other files
So, your friend made a function for you to use in your program.
What if you just don't want to import that function in your main code.
Well, imports have come to the rescue!
In your main function, type `import (file path).cpl`
Now just call one of the functions from that file, and if you don't get any errors, and get a output, it works!
### Flow control
The only flow control functions you have are if and else.
To use these, go to your main function and type `if 2 == 2 true`
This well check if 2 is 2 and if it is, it calls the function true.
You can also use temp by using a dot.
for else statments, add `else false` onto your if statment. 
Also keep in mind, this is one line, and it is the only way use them.
### Using the file system
