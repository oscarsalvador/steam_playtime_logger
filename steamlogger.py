from subprocess import Popen, PIPE, STDOUT
from datetime import datetime 

index_path = "/YOUR-PATH/v2.json"  #or /YOUR-PATH/index.html
csv_path = "/YOUR-PATH/steamPlayLog.csv"
minimum_minutes = 0
open_games = []

def resolve_name(appid, line):
    index = open(index_path, "r")
    games_list = index.read()

    start = games_list.find(":" + str(appid) + ",")
    #if the exact appid was found => the game currently available in the store
    if start != -1:
        end = games_list.find("\"}", start)
        return games_list[start:end].split("name\":\"")[-1]
    # not found => either non-steam game or a removed title
    # if path contains common & steam, it's a removed game; get the name from its folder
    if line.__contains__("/Steam/steamapps/common/"):
        name = line.split("/common/")[-1]
        name = name.split("/")[0]
        return name
    # last scenario, non-steam game; launch method varies, i just save the whole line
    return line.split("Game process removed: ")[-1]


def launch_op(line):
    appid = line.split(" ")[5] #Game process added : AppID <appid> ...

    new_launch = [appid, datetime.now(), line]
    open_games.append(new_launch)


def finish_op(line):
    appid = line.split(" ")[4] #Game process removed: AppID <appid> ...

    for i in open_games:
        if i[0] == appid:
            open_games.remove(i)

            now = datetime.now()
            diff = now - i[1]
            if int(diff.seconds/60) < minimum_minutes: #don't log if under minimum
                return

            format_code = '%Y/%m/%d,%H:%M:%S'

            game_name = resolve_name(i[0], line)
            print(game_name)

            f = open(csv_path, "a")
            entry = game_name + "," + i[1].strftime(format_code) + "," + \
                now.strftime(format_code) + "," + \
                str(int(diff.seconds/60)) + "\n"

            f.write(entry)
            f.close()

def main():
    p = Popen(['/usr/bin/steam-runtime', '%U'], 
        stdin=PIPE, stdout=PIPE, stderr=STDOUT, bufsize=10000)

    for line in p.stdout:
        exitcode = p.poll
        if (exitcode == 0) or (exitcode == 1): 
            exit()
        
        line = str(line)

        if "Game process added" in line:
            launch_op(line)  
        if "Game process removed" in line:
            finish_op(line)  


if __name__ == '__main__':
    main()
