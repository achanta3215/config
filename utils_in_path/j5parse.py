#!/usr/local/bin/python3
import sys
import json5
print(end='')
lines = sys.stdin.readlines()
inputStr  = ''.join(str(s) for s in lines)

startIndex = inputStr.find('{')
endIndex = inputStr.rfind('}') + 1
extractedStr = inputStr[startIndex:endIndex]
leftTruncatedString = inputStr[0:startIndex]
rigthTruncatedString = inputStr[endIndex:len(inputStr) + 1]

json5Output = json5.loads(extractedStr)
jsonOutput = json5.dumps(json5Output, sort_keys=True, indent=4)
print(leftTruncatedString + jsonOutput + rigthTruncatedString)
