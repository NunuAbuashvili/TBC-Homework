# შექმენით კლასი Inset, რომელსაც ექნება კონსტრუქტორი. კონსტრუქტორში უნდა შეიქმნას ცარიელი სია. შექმენით მეთოდი insert, რომელიც სიაში ჩაამატებს გადაცემულ ელემენტს. insert მეთოდით უნდა დაემატოს მხოლოდ უნიკალური ელემენტები. შექმენით მეთოდი member, რომელიც იღებს ერთ არგუმენტს, ამოწმებს არის თუ არა მსგავსი ელემენტი ლისტში, თუ არის, აბრუნებს True, თუ არ არის, აბრუნებს False. მას აქვს მეთოდი remove, რომელიც იღებს ერთ არგუმენტს და ცდილობს მის წაშლას სიიდან, თუ ასეთი ელემენტი არ აღმოჩნდება სიაში უნდა გამოიტყორცნოს ValueError შეტყობინებით "ვერ ვიპოვნე". კლასს უნდა ჰქონდეს __str__, რომელიც ჯერ დაალაგებს სიას ზრდადობით და მერე დააბრუნებს მის ელემენტებს სტრიქონად.

class Inset:
    def __init__(self):
        self.data = []
    
    def insert(self, element):
        if element not in self.data:
            self.data.append(element)
    
    def member(self, element):
        return element in self.data
    
    def remove(self, element):
        if element not in self.data:
            raise ValueError("Could not find this element")
        self.data.remove(element)
    
    def __str__(self):
        sorted_data = map(str, sorted(self.data))
        return ', '.join(sorted_data)

def main():
    test_data = Inset()
    # Add new elements
    test_data.insert(10)
    test_data.insert(12)
    test_data.insert(14)
    # Trying to add a duplicate element
    test_data.insert(14)  
    print(str(test_data))  # Output: 10, 12, 14
    # Test the <member> function
    print(test_data.member(12))  # Output: True
    print(test_data.member(8))  # Output: False
    # Test the <remove> function
    test_data.remove(10)
    print(str(test_data))  # Output: 12, 14

if __name__ == "__main__":
    main()
        