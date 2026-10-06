def array_of_names(persons):
    full_names = []

    for first , last in persons.items():
        full_name = f"{first.capitalize()} {last.capitalize()}" # .capitalize() จะเปลี่ยนแค่ ตัวอักษรตัวแรกสุด ให้เป็นตัวพิมพ์ใหญ่
        full_names.append(full_name)   

    return full_names  
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))