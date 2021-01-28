"""
File: removeduplicates.py
-------------------------
This program gives you practice with constructing a new list
based on values given to you by the user.  You also get
practice removing duplicates from that list
"""


def read_list():
    i = "true"
    a = []
    while i == 'true':
        nums = int(input("Enter value (0 to stop): "))
        if nums == 0:
            break
        a.append(nums)
    return a


def remove_duplicates(num_list):
    return list(dict.fromkeys(num_list))



def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
