import json
class FileUtil:

    def readFromFile(p_file):
        with open(p_file, "r") as f:
            return json.load(f)
    
    def saveToFile(p_file, content):
        with open(p_file, "w+") as f:
            json.dump(content, f)
        
