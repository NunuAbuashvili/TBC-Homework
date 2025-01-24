# შექმენით კლასი Queue. ეს უნდა იყოს მონაცემთა სტრუქტურა Stack-ის მსგავსი, როგორიც ლექციაზე გავაკეთეთ. მთავარი განსხვავება არის ის, რომ ელემენტის ამოღების პრინციპი აქვს განსხვავებული. პირველი ჩამატებული ელემენტი უნდა დაბრუნდეს პირველი. ამ პრინციპის სახელწოდებაა FIFO(First in First Out)
# []
# 1 - [1]
# 2 - [1, 2]
# 3 - [1, 2, 3]

# 1 - [2, 3]
# 2 - [3]
# 3 - []

class Queue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def enqueue(self, new_element):
        self.elements.append(new_element)
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.elements.pop(0)

test_data = Queue()
# Add new elements
test_data.enqueue(29)
test_data.enqueue(4)
test_data.enqueue(19)
test_data.enqueue(96)
# Test the <pop> function
print(test_data.dequeue()) # Output: 29
print("Left in queue", test_data.elements) # Output: Left in queue [4, 19, 96]
print(test_data.dequeue()) # Output: 4
print("Left in queue", test_data.elements) # Output: Left in queue [19, 96]
