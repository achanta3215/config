#!/usr/bin/python3
from pathlib import Path
import subprocess
configDirPath = Path(Path.home(), 'dev/config')

configDirPath.mkdir(parents=True, exist_ok=True)
subprocess.run(["git", "pull"], cwd=configDirPath)
subprocess.run(["rm", ".spacemacs"], cwd=Path.home())
Path(Path.home(), '.spacemacs').symlink_to(Path(configDirPath, '.spacemacs'))

