while True:
    try:
        a = int(input())
        b = int(input())
        x = input("What you want to do add, sub, multi, div:")
        if (x == "add"):
            print(a + b)
        elif (x == "sub"):
            print(a-b)
        elif (x == "multi"):
            print(a*b)
        elif (x == "div"):
            print(a/b)
    except ValueError:
        print("Always enter a number!")
    except TypeError:
        print("Always enter a number!")
    except ZeroDivisionError:
        print("Always enter a number!")
    except OverflowError:
        print("Always enter a number!")
    except KeyboardInterrupt: 
        print("Smart move but i am your dad")
    finally:
        print("Thank you , never come back again")
