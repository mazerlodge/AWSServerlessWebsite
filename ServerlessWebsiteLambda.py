import json 

def lambda_handler(event, context):
	print("In lambda handler")

	# Check for valid parameters and parse them.
	englishValue = "NOT_SET"
	hawaiiValue = "NOT_SET" 
	qsParams = "NOT_SET"
	
	for aKey in event.keys(): 
		print("Key found = %s" % aKey)
		
		if (aKey == "queryStringParameters"): 
			print(event["queryStringParameters"])
			qsParams = event["queryStringParameters"]
			englishValue = qsParams["eParam"]
			hawaiiValue = qsParams["hParam"]

	print("Got params %s and %s " % (englishValue, hawaiiValue))
	
	resp = {
		"statusCode": 200,
		"headers": {
			"Access-Control-Allow-Origin": "*",
		},
		"body": "RETURN_TEXT_GOES_HERE E~H " + englishValue + "~" + hawaiiValue 
	}

	return resp
	