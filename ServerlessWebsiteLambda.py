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

	# Test lookup 
	dataLines = ["papa'a la,sunburned",
				"slippahs,flip flops",
				"aka'a ka,to laugh",
				"shoots den,later then",
				"lilikoi,passionfruit"]
	
	bLineFound = False 
	inLine = hawaiiValue + "," + englishValue
	for aLine in dataLines: 
		# parse line on comma, line looks like: papa'a la,sunburned
		if (inLine == aLine.strip()): 
			bLineFound = True
			break 

	# Compose response
	if (bLineFound): 
		msg = "exists," + inLine
	else: 
		msg = "to_be_added," + inLine

	
	resp = {
		"statusCode": 200,
		"headers": {
			"Access-Control-Allow-Origin": "*",
		},
		"body": msg 
	}

	return resp
	