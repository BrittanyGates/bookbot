# BookBot

BookBot is a simple command-line tool for analyzing the text of a book. It provides a report on the number of words and the frequency of each character in the book.

## Usage

To use BookBot, run the `main.py` script with the path to a book file as an argument:

```bash
python3 main.py /path/to/your/book.txt
```

## Features

*   **Word Count:** Counts the total number of words in the book.
*   **Character Count:** Counts the occurrences of each character in the book.
*   **Sorted Report:** Displays a sorted list of character frequencies.

## Modules

### `main.py`

The main script that drives the BookBot program. It takes a book file as a command-line argument, reads the file, and then uses the `stats` module to generate a report.

### `stats.py`

This module contains the functions for analyzing the text of the book.

*   `count_words(text)`: Returns the total number of words in the given text.
*   `count_characters(text)`: Returns a dictionary with the count of each character in the text.
*   `sort_dict(dictionary)`: Sorts the character count dictionary by frequency in descending order.

## Example Output

```
============ BOOKBOT ============

Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------
Found 77986 total words

--------- Character Count -------
e: 46009
t: 32203
a: 28884
o: 27329
n: 25235
h: 22894
i: 22633
s: 22352
r: 21033
d: 15834
l: 14291
u: 10283
m: 9153
c: 8817
w: 8157
f: 7917
g: 6832
y: 6610
p: 6016
b: 5345
v: 3537
k: 2884
j: 687
x: 631
q: 396
z: 209
============= END ===============
```