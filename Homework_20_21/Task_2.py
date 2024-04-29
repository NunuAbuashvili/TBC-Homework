"""
დაწერეთ პროგრამა, რომელიც დაადგენს არის თუ არა გზა მიმართულ გრაფში ორ წერტილს შორის. მიმართული გრაფი ნიშნავს, რომ თუ გვაქვს გზა A -> B, ეს არ ნიშნავს რომ გვაქვს გზა B -> A. სხვა სიტყვებით რომ ვთქვათ, A-დან B-ში მიდის გზა, მაგრამ არა - პირიქით, B - დან A - ში ვერ მოხვდები. 

Example:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
}

A -> E = True
C -> D = False

"""
# A global dictionary to store the results of function calls using the (starting point, ending point) tuple as the key.
cache = {}

def has_path(graph: dict, start: str, end: str) -> bool:
    # This function checks if there is a path (direct or indirect) from start point to end point inside the given graph, and returns a boolean
    
    # Check if the result is already cached
    if (start, end) in cache:
        return cache[(start, end)]
    
    # Check if the start point is present as a key in the graph, and if the length of its value is greater than 0
    if (start not in graph) or (len(graph[start]) == 0):
        cache[(start, end)] = False
        return False
    
    # Check if the end point is a direct value of the start point
    if end in graph[start]:
        cache[(start, end)] = True
        return True
    
    # If not, loop through each value of the start point and recursively check if there is a path from start point to end point
    for point in graph[start]:
        if has_path(graph, point, end):
            cache[(start, end)] = True
            return True
        
    cache[(start, end)] = False
    return False

def main():
    GRAPH = {
        'A': ['P'],
        'C': ['O', 'D', 'E'],
        'D': ['I'],
        'E': [],
        'F': ['G'],
        'M': ['O', 'T', 'P'],
        'N': ['S', 'C', 'L', 'I'],
        'P': ['S'],
        'S': ['F'],
        'T': ['I', 'R', 'O'],
        'U': [],
    }
    
    
    start_point = input("Please, enter the starting point: ")
    end_point = input("Please, enter the ending point: ")
    print(f"Is there a path from {start_point} to {end_point}?", end=" ")
    print(has_path(GRAPH, start_point, end_point))

if __name__ == "__main__":
    main()
