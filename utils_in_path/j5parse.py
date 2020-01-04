#!/usr/local/bin/python3
import sys
import json5
print(end='')
lines = sys.stdin.readlines()
inputStr  = ''.join(str(s) for s in lines)

json5Output = json5.loads(inputStr)
jsonOutput = json5.dumps(json5Output, sort_keys=True, indent=4)
print(jsonOutput)
