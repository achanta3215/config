#!/usr/local/bin/python3
import sys
import json5
import json
lines = sys.stdin.readlines()
inputStr  = ''.join(str(s) for s in lines)

json5Output = json5.loads(inputStr)
jsonOutput = json.dumps(json5Output)
print(jsonOutput)
