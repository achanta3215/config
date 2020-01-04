#!/usr/local/bin/python3
import sys
import json5
print(end='')
lines = sys.stdin.readlines()
inputStr  = ''.join(str(s) for s in lines)

toIndent = len(lines[1]) - len(lines[1].lstrip())

startIndex = inputStr.find('{')
endIndex = inputStr.rfind('}') + 1
extractedStr = inputStr[startIndex:endIndex]
leftTruncatedString = inputStr[0:startIndex]
rigthTruncatedString = inputStr[endIndex:len(inputStr) + 1]

json5Output = json5.loads(extractedStr)
jsonOutput = json5.dumps(json5Output, sort_keys=True, indent=toIndent)

formattedJSONOutput = jsonOutput
if (extractedStr.find("'") != -1):
  formattedJSONOutput = jsonOutput.replace('"', "'")

print(leftTruncatedString + formattedJSONOutput + rigthTruncatedString)
