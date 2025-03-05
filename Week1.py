# 1.⁠ ⁠Display Fibonacci Series upto 10 terms
print("Q1")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    temp = b
    b = a + b
    a = temp

# 2.⁠ ⁠Display numbers at the odd indices of a list
print()
print("Q2")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1, len(numbers), 2):
    print("index", i, numbers[i], end=" ")

# 3.⁠ ⁠⁠string = """
# I have provided this text to provide tips on creating interesting paragraphs.
# First, start with a clear topic sentence that introduces the main idea.
# Then, support the topic sentence with specific details, examples, and evidence.
# Vary the sentence length and structure to keep the reader engaged.
# Finally, end with a strong concluding sentence that summarizes the main points.
# Remember, practice makes perfect!
# """
#Your task is to count the number of different words in this text
print()
print("Q3")
string = """I have provided this text to provide tips on creating interesting paragraphs. 
First, start with a clear topic sentence that introduces the main idea.
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""

words = string.lower().split()
unique_words = set(words)
print(len(unique_words))

# 4.⁠ ⁠Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
print("Q4")
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = "Shreyvyas"
print("Number of vowels:", count_vowels(word))

# 5.⁠ ⁠Iterate through the following list of animals and print each one in all caps.
#animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
print("Q5")
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for i in animals:
    print(i.upper(), end=" ")

# 6.⁠ ⁠Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
print()
print("Q6")
for i in range(1,21):
    if(i%2==0):
        print(i, " even", end=" ")
    else:
        print(i, " odd", end=" ")

# 7.⁠ ⁠Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
print()
print("Q7")
def sum_of_integers(a,b):
    sum = a + b
    return sum

a, b = 5, 10
print("Sum = ", sum_of_integers(a,b))

# Additional problems
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "rating": 4.2
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "rating": 4.9
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "rating": 4.1
    }
]

# 1. Checking Book Ratings
# Write a function check_rating(book) that takes a book dictionary and returns True if the rating is greater than 4.5, 
# and False otherwise. Additionally, modify the function to return 'low' if the rating is less than or equal to 4.0, 
# 'medium' if it's greater than 4.0 but less than or equal to 4.5, and 'high' if it's greater than 4.5.
print("Additional question 1")
def check_rating(book):
    rating = book["rating"]
    if rating > 4.5:
        return "high"
    elif rating > 4.0:
        return "medium"
    else:
        return "low"

for i in books:
    print("Book ",i," rating:",check_rating(i))
    
# 2. Average Rating by Genre
# Write a function average_rating_by_genre(books, genre) that accepts the list of books and a genre, 
# and returns the average rating for that genre. If the genre does not exist in the list, return an appropriate message.
print("Additional question 2")
def average_rating_by_genre(books, genre):
    genre_books = [book["rating"] for book in books if book["genre"].lower() == genre.lower()]
    if not genre_books:
        return f"No books found for the genre: {genre}"
    return sum(genre_books) / len(genre_books)

print(average_rating_by_genre(books, "Fiction"))

# 3. Books by Author
# Write a function books_by_author(books, author) that accepts the book list and an author's name, 
# and returns a list of all the books written by that author. If the author does not exist, raise a custom error.
print("Additional question 3")
def books_by_author(books, author):
    author_books = [book["title"] for book in books if book["author"].lower() == author.lower()]
    if not author_books:
        raise ValueError(f"No books found by author: {author}")
    return author_books

print(books_by_author(books, "J.D. Salinger"))
print(books_by_author(books, "Shrey"))