
# https://stackoverflow.com/questions/13949637/how-to-update-json-file-with-python
import json


def updateJsonFile():
    jsonfile = None
    try:
        # Open the JSON file for reading
        jsonFile = open("./files/json_update_test.json", "r")
        data = json.load(jsonFile)  # Read the JSON into the buffer
        jsonFile.close()  # Close the JSON file
    except:
        jsonFile = open("./files/json_update_test.json", "w")
        print("Failed to open the file")

    try:
        data = {}
        data["location"] = "test"
        data["mode"] = "replay"

        # Save our changes to JSON file
        jsonfile = open("./files/json_update_test.json", "w+")

        json_data = json.dumps(data)
        print(json_data)
        jsonfile.write(json_data)

        jsonfile.close()
    except:
        print("can't modify the file")


if __name__ == '__main__':
    updateJsonFile()
