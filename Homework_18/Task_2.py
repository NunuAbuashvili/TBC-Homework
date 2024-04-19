# დაწერეთ ფუნქცია midpoint(x1, y1, x2, y2). ფუნქციამ უნდა გამოითვალოს x და y წერტილების შუა წერტილი და tuple-ის სახით დააბრუნოს. შუაწერტილის გამოთვლის ფორმულა შემდეგია: ( (x1 + x2) / 2 , (y1 + y2) / 2). გამოიძახეთ თქვენ მიერ შექმნილი ფუნქცია main-ში რამდენჯერმე სხვადასხვა პარამეტრებით და აჩვენეთ თქვენი ფუნქციის მუშაობა.

def midpoint(x1: int, y1: int, x2: int, y2: int) -> tuple[float, float]:
    # This function calculates the midpoint between two points (x1, x2) and (y1, y2)
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    return (midpoint_x, midpoint_y)

def main():
    # Test data 1
    print("Test data 1:")
    x1, y1, x2, y2 = 5, 7, 10, 14
    midpoint_coordinates = midpoint(x1, y1, x2, y2)
    print(f"Midpoint of the coordinates ({x1}, {y1}) and ({x2}, {y2}) is {midpoint_coordinates}")
    
    # Test data 2
    print("Test data 2:")
    x1, y1, x2, y2 = -2, 4, 6, 4
    midpoint_coordinates = midpoint(x1, y1, x2, y2)
    print(f"Midpoint of the coordinates ({x1}, {y1}) and ({x2}, {y2}) is {midpoint_coordinates}")
    
    # Test data 3
    print("Test data 3:")
    x1, y1, x2, y2 = 0, 0, 10, 10
    midpoint_coordinates = midpoint(x1, y1, x2, y2)
    print(f"Midpoint of the coordinates ({x1}, {y1}) and ({x2}, {y2}) is {midpoint_coordinates}")

if __name__ == "__main__":
    main()
