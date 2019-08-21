CTRL_SCALE = 1


# Change a part of the name of a joint. Return the new name
def changeSuffix(jntname, currsuffix, suffix, separator):
    temp = jntname.split(separator)
    newtemp = [t.replace(currsuffix, suffix) for t in temp]

    result = separator.join(newtemp)
    return result

# Add a suffix to the selected. Return the new name
def addSuffix(selected, suffix, separator):
    newtemp = selected + separator + suffix
    return newtemp
