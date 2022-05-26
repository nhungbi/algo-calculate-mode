def calculate_mode(input_list):
    """
    Given a list of integers or strings, return a list of the 
    most frequent values.
    """
    elt_dict = {}
    for elt in input_list:
        if elt in elt_dict:
            elt_dict[elt] +=1
        else:
            elt_dict[elt] = 1 #if not in dict, then add an entry with value 1
    mode = max(elt_dict.values()) #max value
    output = []
    for k,v in elt_dict.items():
        if v == mode:
            output.append(k)
    
    return sorted(output)

# print(calculate_mode([2,1,3]))


    
