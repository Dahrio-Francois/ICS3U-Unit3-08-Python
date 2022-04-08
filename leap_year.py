#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program lets the user know if an inputted integer
#   is a leap year or not


def main():
    # this program starts the game

    # process & output
    try:
        year = int(input("Enter the year to check if it is a leap year or not: "))
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("\nThis year is a leap year!")
                else:
                    print("\nThis year is not a leap year!")
            else:
                print("\nThis year is a leap year!")
        else:
            print("\nThis is not a leap year")
    except Exception:
        print("\nThis was not an integer.")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
