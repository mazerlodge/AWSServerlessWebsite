#!/usr/local/bin/python3

def qtest(x): 
	return(x) 


def test(dictVar): 

	varE = "NOT_SET"
	varH = "NOT_SET" 

	if "eParam" in dictVar.keys(): 
		varE = dictVar["eParam"]

	if "hParam" in dictVar.keys(): 
		varH = dictVar["hParam"]

	print("Got %s and %s " %(varE, varH))

dict = {"Key": "value", "eParam" : "abc", "hParam" : "def" }
test(dict)
