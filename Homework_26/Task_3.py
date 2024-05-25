# გააფართოვეთ სტანდარტულ ბიბლიოთეკაში არსებული მონაცემთა სტრუქტურა list. დაამატეთ მას ორი მეთოდი min და max, რომლებიც დააბრუნებენ მინიმალურ და მაქსიმალურ მნიშვნელობას შესაბამისად. შექმენით კლასის რამდენიმე ობიექტი და აჩვენეთ, რომ მოთხოვნილი ფუნქციონალი გამართულად მუშაობს. გამოიყენეთ მემკვიდრეობა.
class ExtendedList(list):
    # A subclass of the built-in list class with additional methods to find the minimum and maximum values in the list.
    def __init__(self, lst: list):
        super().__init__(lst)
    
    def min(self):
        try:
            if len(self) == 0:
                raise ValueError("The list is empty.")
            return min(self)
        # If there are mixed strings and numbers in the list
        except TypeError as e:
            return f"Error: {e}"
    
    def max(self):
        try:
            if len(self) == 0:
                raise ValueError("The list is empty.")
            return max(self)
        # If there are mixed strings and numbers in the list
        except TypeError as e:
            return f"Error: {e}"

class InitList(ExtendedList):
    def __init__(self, lst: list):
        super().__init__(lst)
    
class StringList(ExtendedList):
    def __init__(self, lst: list):
        super().__init__(lst)           

def main():
    my_list1 = ExtendedList([5, 2, 8, 1, 9])
    my_list2 = ExtendedList([])  
    my_list3 = InitList([-3, 7, 0, 4])
    my_list4 = StringList(["TBC", "Academy", "Python", "Intro"])
    my_list5 = ExtendedList(["TBC", "Academy", "Python", "Intro"])
    my_list6 = ExtendedList(["10", 12, 17, "23"])
    
    print(my_list1.min()) # 1
    # print(my_list2.max()) # Output: Raises a ValueError
    print(my_list3.min()) # -3
    print(my_list4.max()) # Academy
    print(my_list4.min()) # TBC
    print(my_list5.min()) # Academy
    print(my_list5.max()) # TBC
    print(my_list6.min()) # Error: '<' not supported between instances of 'int' and 'str'

if __name__ == "__main__":
    main()
    