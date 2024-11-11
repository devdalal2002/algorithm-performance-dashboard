def insert_bst(root, value):
    
    if root is None:
        return {"value": value, "left": None, "right": None}
    if value < root["value"]:
        root["left"] = insert_bst(root["left"], value)
    else:
        root["right"] = insert_bst(root["right"], value)
    return root

def search_bst(root, target):
   
    if root is None or root["value"] == target:
        return root
    if target < root["value"]:
        return search_bst(root["left"], target)
    return search_bst(root["right"], target)