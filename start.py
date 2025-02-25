from date_A import data , Sleep
import os 
from shap import shap , shap2 , shap3
import json


if os.path.exists("data_password"):
    pass
else:
    os.system("mkdir data_password")
while True:
    Sleep(3)
    os.system("clear")
    shap3()
    Sleep(2)
    file_name = input("Entey your name file\n>> ")
    if os.path.exists(file_name):
        print("file exists\nplease try again  :)")
        exit()
    elif file_name == "exit":
        exit()
    else:
        with open (f"{file_name}.json", "w") as file:
            file.write(json.dumps(data(), indent=4))
        os.system("clear")
        shap2()
        os.system(f"mv {file_name}.json data_password")
        print("file created successfully")
        Sleep(4)
        exit()
