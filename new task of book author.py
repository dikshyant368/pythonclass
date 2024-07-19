#import requests
# from bs4 import BeautifulSoup

# url ='https://offtheshelf.com/2020/01/authors-to-read-this-year/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content,'html.parser')

# # extract the information 
# book_titles = soup.find_all('div',class_='book-title')
# book_authors = soup.find_all('div',class_='book-author')
# book_descriptions = soup.find_all('div',class_='book-description')

# #print the extracted information 
# for title , author,description in zip(book_titles,book_authors,book_descriptions):
#     print(f'Book Titles: {title.text}')
#     print(f'Book Author: {author.text}')
#     print(f'Book Description: {description.text}')
# print()
import sqlite3
import requests
from bs4 import BeautifulSoup

# connect sqlite to the table or create a new if not exists
conn = sqlite3.connect('details.db')

c = conn.cursor()

# Creating a table 
c.execute('''CREATE TABLE IF NOT  EXISTS details(id INTEGER PRIMARY KEY,Title TEXT,Book_Author TEXT,Description TEXT)''')

url ='https://offtheshelf.com/2020/01/authors-to-read-this-year/'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

#Extract the information 
book_titles = soup.find_all('div',class_='book-title')
book_authors = soup.find_all('div',class_='book-author')
book_descriptions = soup.find_all('div',class_='book-description')

#insert the extracted information into the table
for title , author,description in zip(book_titles,book_authors,book_descriptions):
    title_text = title.text.strip()
    author_text = author.text.strip()
    description_text = description.text.strip()
    print(title_text,author_text,description_text)
    c.execute('''INSERT INTO details(Title,Book_Author,Description)VALUES(?,?,?)''',(title_text,author_text,description_text))

# commit the  change and close the operation
conn.commit()
conn.close()
