"""
Generators will allow us to generate a new iterable
object one at a time. It allows us to free the memory in
every iteration as the value will be YIELDED one at a time
and will not just build a whole array (flock in the `slow_iteration`)
function to then returns it (which uses too much runtime memory)
"""
def main():
    fast_iteration_with_generators()

def fast_iteration_with_generators():
    n = int(input("What's n? "))

    for i in sheep_generator_fast(n):
        print(i)

def sheep_generator_fast(n):
    for i in range(n):
        yield "🐑" * i






def slow_iteration():
    n = int(input("What's n? "))

    for i in sheep_slow(n):
        print(i)

def sheep_slow(n):
    # Use the flock array in order to store all of the sheeps and then return them all at once (hint: this will cause a memory leak as it will overwelm the memory available at runtime)
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()
