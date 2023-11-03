#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv[1:]
num_args = len(argv)
if num_args == 0:
   print(f"0 argument.")
else:
    print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
    for i, arg in enumerate(argv):
        print(f"{i + 1}: {arg}")
