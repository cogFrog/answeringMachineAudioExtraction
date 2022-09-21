#import serialByteExtraction

def ynInput(prompt):
    while True:
        response = input(prompt + " (y/n): ")
        if response.lower() == "y":
            return True
        elif response.lower() == "n":
            return False
        else:
            print("Invalid response")


def confirmExtension(name, extension):
    if name.split(".")[-1] != extension:
        name += ".pickle"
    return name


if ynInput("Retrieve saved data?"):
    audioSaveFileName = input("Provide filename: ")
    audioSaveFileName = confirmExtension(audioSaveFileName, "pickle")

    # todo: open pickle file, empty into data
    data = "pickled data (" + audioSaveFileName + ")"
else:
    serialPort = input("Provide serial port name: ")
    # todo: open serial port and get data over serial, add exceptions
    data = "serial data (" + serialPort + ")"

    if ynInput("Would you like to save this data?"):
        newSaveFileName = input("Provide filename: ")
        newSaveFileName = confirmExtension(newSaveFileName, "pickle")

        # todo: save data to pickle file
        print("saved: " + data + " to " + newSaveFileName)

if ynInput("Would you like to play the retrieved audio?"):
    print("playing: " + data)  # todo: actually play audio
if ynInput("Would you like to save the retrieved audio?"):
    audioSaveFileName = input("Provide filename: ")
    audioSaveFileName = confirmExtension(audioSaveFileName, "wav")
    # todo: save data
    print("saved audio: " + data + " to " + audioSaveFileName)

