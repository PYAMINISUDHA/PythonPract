def check_variable(string):
    if ('A' <= string[0] <= 'Z') or ('a' <= string[0] <= 'z') or string[0] == '_':
        return(True)
    else:
        return(False)

print(check_variable("name"))