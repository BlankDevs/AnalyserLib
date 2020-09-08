def read_jsonl_file(path):
    labeled = []

    with open(path, "r") as read_file:
        for line in read_file:
            labeled.append(json.loads(line))
    
    return labeled
