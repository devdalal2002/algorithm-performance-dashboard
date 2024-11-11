def perform_linear_search(data, target):
    
    for idx, value in enumerate(data):
        if value == target:
            return idx
    return -1