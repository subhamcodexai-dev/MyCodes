while True:
    Grade = input("What is your grade:")

    match Grade:
        case "A" | "a":
            print("Excellent")
        case "B" | "b":
            print("Good")
        case "C" | "c":
            print("Average")
        case "D" | "d":
            print("Below Average")
        case "E" | "e":
            print("Fail")
        case _:
            print("Invalid")
            break

        



            