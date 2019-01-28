
with open("/Users/Bharathan/projects/python_practise/input_01.txt", "r") as f:
    excludeFileContent = list(filter(None, f.read().splitlines()))

print(excludeFileContent)
