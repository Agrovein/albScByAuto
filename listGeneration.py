#decompose all elements from list of lists and generate one overall list
def flatten_list(nested_list):
    print(nested_list)
    return [item for sublist in nested_list for item in sublist]