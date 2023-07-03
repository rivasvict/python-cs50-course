def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 250]

print(total(*coins), "knuts")# Unpacking happens with the * and it is basically the spread operator I know in Javascript. 



# Unpacking can also work for dicts as well but instead of a single *, we should use **. And it uses the keys of the dict to send to the function named arguments
coins_dict = {"galleons": 100, "sickles": 50, "knuts": 250};
print(total(**coins_dict), "knuts")
# The previous line is the same as doing this:
print(total(galleons=100, sickles=50, knuts=250), "knuts")
# This way of unpacking with ** for dicts does not care about the position of the arguments as long as no more than the total number of argument is input and the names of the keys match the names of the arguments.
coins_dict_disordered = {"sickles": 50, "knuts": 250, "galleons": 100}
print(total(**coins_dict_disordered), "knuts")


# This will not work as this dict will not satisfy the function signature
#coins_dict_wrong = {"galleons": 100, "sickles": 50, "knuts_coinage": 250}
#print(total(**coins_dict_wrong), "knuts")




# *args and **kwargs
"""
*args: Array-like argument unpacking (args is a convention) (first argument)
**kwargs: Dict-like argument unpacking (kwargs is a convention) (second argument)
"""
def f(*args, **kwargs):
    print("Positional:", args)
    #print("Named:", kargs)# kwargs

f(100, 50, 25)
#f(galleons=100, sickes=50, knuts=25)#kwargs
