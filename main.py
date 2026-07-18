student_data = {
    "id1" : {"Name": "John", "class":"v", "subject_intergration": "English, Science, Physics"},
    "id2" : {"Name": "Victor", "class":"v", "subject_intergration": "English, Science, Physics"},
    "id3" : {"Name": "Peter", "class":"v", "subject_intergration": "English, Science, Physics"},
    "id4" : {"Name": "Peter", "class":"v", "subject_intergration": "English, Science, Physics"}
}

results = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["Name"], details["class"], details["subject_intergration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        results[student_id] = details

for k , v in results.items():
    print(k, ":", v)
