"""
argparse is a library that will help us to handle
hour command line arguments easier than just using
`sts`.
"""
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")# Ask argparser to parse the arguments and set a description of what the program does
parser.add_argument("-n", default=1, help="number of times to meow", type=int)# Adds the argument in the first positional argument `"-n"` in this case to set its value, as well as the default value and help text for the console and set the type and conversion to the desired type (in this case, int), this last part removes the need to convert the type into an int as this library will do it for us.
# The second argument in the previous line sets the default value
args = parser.parse_args()# Parse all arguments

for _ in range (args.n):# There is no need to specify whether `args.n` is an int or not due to the fact that it was automatically converted by the line 8 where the `type` argument was passed as an `int`
    print("meow")
