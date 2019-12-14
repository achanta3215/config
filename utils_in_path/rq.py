#!/usr/local/bin/python3
import requests
import json
import tempfile
import subprocess
import sys

[_, first] = sys.argv
response = requests.get(first)
with tempfile.NamedTemporaryFile(mode='w+t', suffix='.tmp') as tmpFile:
  tmpFile.write(json.dumps(response.json(), indent = 4))
  #tmpFile.write('Hello')
  tmpFile.flush()
  subprocess.run(['vim', tmpFile.name])
  
