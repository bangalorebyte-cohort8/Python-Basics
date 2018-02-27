## Python Classes

Submit the following by Thursday, January 26th, 2017 at 6:10pm. 

### Part 1 

In your `README.txt` answer the questions below. Recall that `scope` refers to  which parts of your code can use a given object. For example, global variables can be used by the rest of the code since it is global.

Here is an example of a simple class which stores information about a person:
``` python
import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return(age)
        
person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())
```
Explain what the following variables refer to, and their scope:

1. `Person`
2. `person`
3. `surname`
4. `self`
5. `age` (the function name)
6. `age` (the variable used inside the function)
7. `self.email`
8. `person.email`


Problem 2 : Stock Portfolio Class.

For each company, store the name, ticker
symbol, purchase date, purchase price, and number of shares. Methods include: add
new symbol (new purchase), remove symbol (all shares sold), and YTD or Annual
Return performance for any or all symbols given a current price (and date).
~                                                                                   
