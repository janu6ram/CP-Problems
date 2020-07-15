# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch
# of fabric requires purchasing 1 entire yard. With this in mind,
# write the function fabricYards(inches) that takes the number of
# inches of fabric desired, and returns the smallest number of whole
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of
# inches of fabric desired and returns the number of inches of excess
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!


def fun_fabricyards(inches):
    # your code goes here
    full = inches//36
    extra = inches - (full * 36)
    if extra >= 1:
        return full + 1
    return full


def fun_fabricexcess(inches):
    # your code goes here
    total = fun_fabricyards(inches)
    print("total", total)
    excess = (total * 36) - inches
    return inches


fun_fabricexcess(1)
