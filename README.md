# PyRoutine
Install using ```pip install PyRoutine```

A system to automate clicks on your device. Press alt+p to make that place a click point. Add as many
click points as you wish. Once you are done, you should press alt+f. The system will then process the .json file and click. This may take up to a few minutes based on how many points you choose.
Right now, this system can only do right clicks. More functionality is under development.

Use:
```Python
from PyRoutine import track, click
track.get_input()
click.autoclick(1)
```
As Simple as that! 
