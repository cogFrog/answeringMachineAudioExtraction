#import serialByteExtraction

def ynInput(prompt):
    while True:
        response = input(prompt + " (y/n): ")
        if (response.lower() == "y"):
            return True
        elif (response.lower() == "n"):
            return False
        else:
            print("Invalid response")

res = ynInput("Retrieve saved data?")
print(res)