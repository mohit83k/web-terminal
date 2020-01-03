import json

#constants
EMPTY_STRING = ""

def read_json_file(filename):
	with open(filename) as json_data:
		return json.load(json_data)

def write_json_file(filename,data):
	
    with open(filename, 'w') as outfile:
    	json.dump(data ,outfile)


def convert_to_json(obj):
	return json.dumps(obj)

