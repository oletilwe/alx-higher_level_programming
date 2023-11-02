#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    num_args = len(argv)
    if num_args == 0:
        print(f"Number of arguments: 0.")
    elif num_args == 1:
        print(f"Number of arguments: 1.")
        print(f"1: {argv[0]}")
    else:
        print(f"Number of arguments: {num_args}:")
        for i, arg in enumerate(argv):
            print(f"{i+1}: {arg}")
