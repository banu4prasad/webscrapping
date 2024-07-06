import json

# Path to your JSON file
json_file_path = "/Users/banuprasadb/program/webscrapping/RAW/about us/aboutnmamit[1].json"

# Path to the file where you want to store the questions
output_file_path = "/Users/banuprasadb/program/questions/aboutnmamit.txt"

# Read the JSON file
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Extract questions
questions = [qa["question"] for qa in data["questions_and_answers"]]

# Write questions to the output file
with open(output_file_path, "w") as output_file:
    for question in questions:
        output_file.write(question + "\n")