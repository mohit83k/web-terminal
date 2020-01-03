import utils
import terminal


def execute(cmd):
	output = {}
	out , err = terminal.run(cmd)

	if err is not None :
		output["error"] = err

	if out is not None:
		output["result"] = out 
	else:
		output["result"] = "No Stdout of the command"

	return utils.convert_to_json(output)



