# Logs Analysis Project

A simple internal reporting tool about the users’ activity of an example newspaper’s site.

This program requires Python 3. The program runs from the command line. It does not take any input from the user. It simply connects to the database, uses SQL queries to analyze the data and prints out the answers to some questions in a plain text file.

## Usage

##### Command line

`python newsdata.py`

## Expected Output

The output text file answers the following three questions:

- What are the most popular three articles of all times?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests (to the web server) lead to errors?

Answers can be found in **answers.txt** file in the same directory.

## Sources

The following online sources were used in writing the program:

- https://stackoverflow.com/questions/13750846/split-out-file-name-from-path-in-postgres
- https://www.guru99.com/reading-and-writing-files-in-python.html
- https://www.postgresql.org/docs/current/tutorial-window.html
