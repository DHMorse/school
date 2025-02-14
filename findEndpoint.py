from typing import Tuple

def findEndpoint(x1: int | float, y1: int | float, midpointX: int | float, midpointY: int | float) -> Tuple[int | float, int | float]:
    return 2 * midpointX - x1, 2 * midpointY - y1

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

        midpointX, midpointY = eval(input("Enter the midpoint (x, y): "))

        if verifyTuple(x1, y1) and verifyTuple(midpointX, midpointY):
            break

        print("Invalid input. Please try again.")

    return x1, y1, midpointX, midpointY

def main():
    x1, y1, midpointX, midpointY = getUserInput()

    endpointX, endpointY = findEndpoint(x1, y1, midpointX, midpointY)

    print(f"The endpoint of the line is: {endpointX}, {endpointY}")

if __name__ == "__main__":
    main()