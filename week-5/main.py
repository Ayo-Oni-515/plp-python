# Assignment 1: Design Your Own Class!

class Book:
    def __init__(self, title: str, author: str, genre: str, year: str) -> None:
        self.__title: str = title.lower()
        self.author: str = author.lower()
        self.genre: str = genre.lower()
        self.year: str = year.lower()

    def name(self) -> str:
        return f"The name of this book is {self.__title}"

    def __repr__(self) -> str:
        return (
            f"{self.__title} is "
            f"{"an" if self.genre[0] in ("a", "e", "i", "o", "u") else "a"} "
            f"{self.genre} book written by "
            f"{self.author} in the year {self.year}"
        )


class ActionBook(Book):
    def __init__(self, title: str, author: str, year: str) -> Book:
        super().__init__(title, author, "action", year)


book_sample = ActionBook("Shrek", "William Shakespare", "1970")
print(book_sample)
print(book_sample.name())


# Activity 2: Polymorphism Challenge!
class Animal:
    def __init__(self, name: str, type_of: str = "animal") -> None:
        self.name: str = name
        self.typ_ofe: str = type_of

    def sound(self) -> str:
        return f"{self.name} is sounding :)"

    def __repr__(self) -> str:
        return f"{self.name} is a/an {self.type_of}"


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, "dog")

    def sound(self):
        return f"{self.name} is barking."


dog = Dog("Rex")
print(dog.sound())
