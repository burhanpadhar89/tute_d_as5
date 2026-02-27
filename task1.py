students={"alice":88.5,
          "john":90,
          "justin":80.9,
          "roy":70.2}

name=input("enter student name:")

if name in students:
    print(f"{name}'s marks: {students[name]} ")
else:
    print("student not found!!")    