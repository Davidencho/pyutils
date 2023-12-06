import sys

op_sys = sys.platform.lower()

if "win" in op_sys:
    print("You're on Windows")
elif "linux" in op_sys:
    print("You're on Linux")
elif "darwin" in op_sys:
    print("You're on MacOS.")
else:
    print("Pls use a normal OS :)")