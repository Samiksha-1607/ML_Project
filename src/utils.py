import os
import dill

def save_object(file_path, obj):
    print("Inside save_object")   # debug

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as file_obj:
        dill.dump(obj, file_obj)

    print("Saved at:", file_path)