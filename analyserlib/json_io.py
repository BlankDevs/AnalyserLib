def read_jsonl_file(path):
    
    '''
    Reads a jsonl file
    
    Args:
        path (string): path to the file
    Returns:
        jsonl file
 
    '''
    
    labeled = []

    with open(path, "r") as read_file:
        for line in read_file:
            labeled.append(json.loads(line))
    
    return labeled
