# numeric-matrix-processor-python-developer
A project about a numeric matrix processor (as seen on the JetBrains Academy / Hyperskill Python developer plan)


# About
Here’s a project for devoted matrix enthusiasts: learn to perform a variety of operations on matrices including addition, multiplication, finding the determinant, and dealing with inverse matrices. If you are working on your tech or math major, this project is a good chance for you to learn matrices in action and not just in your notebook.


# Learning outcomes
Apart from learning a whole lot about matrices, you will become familiar with the Math library, recursion, and the many ways of using nested lists in practice.


# Introduction
Matrices have a wide range of applications in programming: they're used for digital image processing, 
graph representation and algorithms on a graph, graphic effects, applied math, statistics, and much more.
Since matrices are tables of numbers, they are usually presented in code as 2D-arrays. 
In this project, you will learn how to read and output matrices, do operations on them, 
and compute the determinant of a square matrix. At first, you will work with matrices with integer elements, 
and later the elements will be floating-point numbers.


# Stage 1/6: Addition
Use nested lists to add matrices.

## Description
Let’s start with matrix addition.
For two matrices to be added, they must have an equal number of rows and columns. 
The sum of matrices AA and BB will be a matrix with the same number of rows and columns as AA or BB. 
The sum of AA and BB, denoted A + BA+B or B + AB+A, is computed by adding the corresponding elements of AA and BB.

## Objectives
In this stage, you should write a program that:
- reads matrix AA from the input.
- reads matrix BB from the input.
- outputs their sum if it is possible to add them; otherwise, it should output the ERROR message.
Each matrix in the input is given in the following way: the first line contains the number of rows nn and the number of columns mm. 
Then nn lines follow, each containing mm integers representing one row of the matrix.
Output the result in the same way but don't print the dimensions of the matrix.

## Examples
### Example 1:
#### Input:
4 5
1 2 3 4 5
3 2 3 2 1
8 0 9 9 1
1 3 4 5 6
4 5
1 1 4 4 5
4 4 5 7 8
1 2 3 9 8
1 0 0 0 1

#### Output:
2 3 7 8 10
7 6 8 9 9
9 2 12 18 9
2 3 4 5 7

### Example 2:
#### Input:
2 3
1 4 5
4 5 5
4 5
0 1 0 4 5
1 7 8 9 4
1 2 3 5 6
1 3 4 3 8

#### Output:
ERROR


# Stage 2/6: Multiplication by number
Learn to multiply a matrix by a number and display the result.

## Description
In this stage, you are going to implement the multiplication of a matrix by a constant. 
To do this, you need to multiply every element of the matrix by that constant.

## Objectives
Write a program that:
1. reads a matrix and a constant,
2. outputs the result of their multiplication.
The first line of the input contains the number of rows and the number of columns of the matrix. The next lines contain rows of the matrix. The last line contains the constant.
The constant and the elements of the matrix are integers.

## Examples
### Example 1:
#### Input:
3 3
1 2 3
4 5 6
7 8 9
3

#### Output:
3 6 9
12 15 18
21 24 27

### Example 2:
#### Input:
2 3
1 2 3
4 5 6
0

#### Output:
0 0 0
0 0 0


# Stage 3/6: Matrix by matrix multiplication
Multiply matrices and create a menu where you can list all the awesome abilities of your matrix processor.

## Description
The next stage is the multiplication of matrices. This operation is a little more complex because it’s not enough to simply multiply the corresponding elements.

Unlike with addition, the sizes of the matrices can be different: the only restriction is that the number of columns in the first matrix should equal the number of rows for the second matrix. 

The resulting matrix has nn rows and kk columns, where every element is a sum of the multiplication of mm elements across the rows of matrix AA by mm elements down the columns of matrix BB.

## Objectives
In this stage, you should write a program that can do all operations on matrices that you've learned.
Write a program that does the following:
1. prints a menu consisting of 4 options. The example shows what the menu should look like.
2. reads the user's choice.
3. reads all data (matrices, constants) needed to perform the chosen operation. The example shows the input format in each case.
4. calculates the result and outputs it. The example shows how your output should look like.
5. repeats all these steps.

The program should keep repeating this until the "Exit" option is chosen.
If some operation cannot be performed, output a warning message.
Also, you should support floating-point numbers.

## Examples
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit

### Example:
#### Input:
Your choice: > 1
Enter size of first matrix: > 4 5
Enter first matrix:
> 1 2 3 4 5
> 3 2 3 2 1
> 8 0 9 9 1
> 1 3 4 5 6
Enter size of second matrix: > 4 5
Enter second matrix:
> 1 1 4 4 5
> 4 4 5 7 8
> 1 2 3 9 8
> 1 0 0 0 1

#### Output:
The result is:
2 3 7 8 10
7 6 8 9 9
9 2 12 18 9
2 3 4 5 7

#### Input:
Your choice: > 2
Enter size of matrix: > 2 2
Enter matrix:
> 1.5 7.0
> 6.0 5.0
Enter constant: > 0.5

#### Output:
The result is:
0.75 3.5
3.0 2.5

#### Input:
Your choice: > 3
Enter size of first matrix: > 3 3
Enter first matrix:
> 1 7 7
> 6 6 4
> 4 2 1
Enter size of second matrix: > 3 3
Enter second matrix:
> 3 2 4
> 5 5 9
> 8 0 10

#### Output:
The result is:
94 37 137
80 42 118
30 18 44

#### Input:
Your choice: > 1
Enter size of first matrix: > 2 2
Enter first matrix:
> 1 2
> 3 2
Enter size of second matrix: > 1 1
Enter second matrix:
> 1

#### Output:
The operation cannot be performed.

#### Input:
Your choice: > 0


# Stage 4/6: Transpose
Add another useful operation to your processor: allow matrix transposition, and then add this option to the menu.

## Description
In this stage, you should implement matrix transposition. Matrix transposition is an operation in linear algebra that replaces rows with columns and returns a new matrix as a result. This is an operation on just a single matrix.

In math, there is only one type of matrix transposition: transposition along the main diagonal. In this stage, you should implement the other three types of transposition to practice your array skills.
These four types are:
- transposition along the main diagonal
- transposition along the side diagonal
- transposition along the vertical line
- transposition along the horizontal line

## Objectives
In this stage, you should add an option to transpose matrices. If the user chooses this option, your program should provide them with 4 types of transposition and ask them to choose one. Then it should read the matrix, transpose it, and output the result. Refer to the example to see the exact format.

Note that your program should still be able to do all operations on matrices that you've implemented in the previous stage.

## Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: > 4

1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: > 1
Enter matrix size: > 3 3
Enter matrix:
> 1 7 7
> 6 6 4
> 4 2 1
The result is:
1 6 4
7 6 2
7 4 1

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: > 0