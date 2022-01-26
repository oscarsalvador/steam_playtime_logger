# Steam Playtime Logger
This is a small Python script to track every time a Steam game is played. It does so by tracking the title of the game and the times of launch and close. These are saved on a .csv, which can be visualized as a stacked bar chart with the R script added. 
![bar_chart](exit.png)

## Usage and configuration
1. Download the source code.
2. Edit line 26 with whichever path you'll use for the CSV file. Either copy the one on this repo or use another, but if you do the latter, know that the script does not add headers, only the entries.
3. Edit line 36 with however you launch Steam in your system. For example, if you use an icon, copy it's command into the string Popen launches.
4. Change the way you launch steam so that you launch this script instead. Following the previous example, change the icon's command to "python /wherever_you_place_the_script/steamlogger.py"


