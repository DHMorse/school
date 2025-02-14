from typing import Tuple

def findMidPoint(x1: int | float, x2: int | float, y1: int | float, y2: int | float) -> Tuple[int | float, int | float]:
    return (x1 + x2) / 2, (y1 + y2) / 2

def getUserInput() -> Tuple[int | float, int | float, int | float, int | float]:
    def verifyTuple(num1: any, num2: any) -> bool:
        def isNumber(num: any) -> bool:
            return type(num) is int or type(num) is float
        
        if num1 is None and num2 is None:
            return False
        
        if not isNumber(num1) or not isNumber(num2):
            return False
        
        return True
    
    while True:
        x1, y1 = eval(input("Enter point 1 (x, y): "))

        x2, y2 = eval(input("Enter point 2 (x, y): "))

        if verifyTuple(x1, y1) and verifyTuple(x2, y2):
            break

        print("Invalid input. Please try again.")

    return x1, y1, x2, y2

def main():
    x1, y1, x2, y2 = getUserInput()

    midpointX, midpointY = findMidPoint(x1, x2, y1, y2)

    print(f"The midpoint between the two points is: {midpointX}, {midpointY}")

if __name__ == "__main__":
    main()