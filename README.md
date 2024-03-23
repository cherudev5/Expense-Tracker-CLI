# EXPENSE TRACKER CLI(Phase 3 project)
    Author :Cheruiyot Kigen David

    Date: 23/03/2024

Expense tracker is a CLI application that allows the user to:
1.Budget by starting with an initial balance.
2.Enter expenses ,stating category and amount.
3.view expenses.
4.Graphical representation of budget and expenses.
5.Edit expenses.

The application uses a database to store the data.The data base has two tables
one for the expenses and the other for users.The user table stores user first name, second name and starting balance.
with the use of a foreign key (user ID )the expense and user table are connected.

# Technologies used 
1.Python 
2.sqlite
Python is the main technology used in developing and running the application.
database management is archived through sqlite.
# TO run the application
 1. install packages that allow for proper functioning of the application
 within the working folder 
 run....pip install matplotlib.This package will allow for plotting of graph.
 make sure pip runs in your system.
 if you get any error running pin install
 follows this:
https://pip.pypa.io/en/stable/installation/
 
from the page choose operating system based on operating system your running.


# MIT License

Copyright (c) 2024 Cheruiyot Kigen David

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.