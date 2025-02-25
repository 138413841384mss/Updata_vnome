
from time import *
import threading
import timeit
import itertools
import os 
from shap import shap
import json

data_python = {
    "data" : []
}



def Sleep(x):
    for i in range(1,x):
        sleep(0.2)
        for j in range(1,4):
            print(f"\r{'.' * j}", end = "")
            sleep(0.3)
    print("")
        
def data():
    def N_charactr():
        print("characters")
        while True:
            try:
                char = input(">> ")
                char = int(char)
            except ValueError:
                print("something is worg")
            else:
                if char < 3 or char > 8:
                    print("beetwin 3,8")
                else:
                    return char
                    break    
    nlp = []
    
    Sleep(2)
    pass_list = ['1','2','3','4','5','6','7','8','9','0',
                'a','b','c','d','e','f','g','h','i','j','k',
                'l','m','n','o','p','q','r','s','t','u','v',
                'w','x','y','z','A','B','C','D','E','F','G',
                'H','I','J','K','L','M','N','O','P','Q','R',
                'S','T','U','V','W','X','Y','Z','!','@','#',
                '$','%','&','*']
    password = itertools.permutations(pass_list, N_charactr())
    start_time = time()
    for perm in password:
        nlp.append(("".join(map(str, perm),)))
    for i in nlp:
        data_python["data"].append(i)
    end_time = time()
    print(f"Number of passwords generated : {len(data_python['data']):,}")
    print(f"Time taken to generate all possible passwords : {end_time - start_time:.3f} seconds")
    return data_python

        

    