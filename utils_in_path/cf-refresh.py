#!/usr/bin/python3
from pathlib import Path
import subprocess
import json

# path to config directory
configDirPath = Path(Path.home(), 'dev/config')

# create config directory
configDirPath.mkdir(parents=True, exist_ok=True)

# update from git repository
subprocess.run(["git", "pull"], cwd=configDirPath)

# .spacemacs related configuration
subprocess.run(["rm", ".spacemacs"], cwd=Path.home())
Path(Path.home(), '.spacemacs').symlink_to(Path(configDirPath, '.spacemacs'))

subprocess.run(["touch", "../.sourcedBashProfileFile"])

## Check if .history file exists, and if not create base config
if (not Path('../.history').exists()):
  subprocess.run(["touch", "../.history"])
  with open('../.historyDefault') as defaultHistoryConfig:
    defaultHistoryData = json.load(defaultHistoryConfig)
    with open('../.history', 'w') as historyFile:
      json.dump(defaultHistoryData, historyFile)

## Handle updations to .history file
with open('../.history', 'r+') as historyFile:
  historyData = json.load(historyFile)
  if (not historyData['addedPathToBashProfile']):
    with open (str(Path(Path.home(), '.bash_profile').absolute()), 'a') as bashProfile:
      bashProfile.write('export PATH="$PATH:$HOME/dev/config/utils_in_path"')
      historyData['addedPathToBashProfile'] = True
      historyFile.seek(0)
      json.dump(historyData, historyFile)
      historyFile.truncate()
  if (not historyData['sourcedBashProfileFile']):
    with open (str(Path(Path.home(), '.bash_profile').absolute()), 'a') as bashProfile:
      bashProfile.write('source $HOME/dev/config/.sourcedBashProfileFile')
      historyData['sourcedBashProfileFile'] = True
      historyFile.seek(0)
      json.dump(historyData, historyFile)
      historyFile.truncate()

    

