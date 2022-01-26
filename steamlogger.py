from subprocess import Popen, PIPE, STDOUT
from datetime import datetime 

games = []

def launch_op(nuline):
    nuline = nuline.split("/common/")[-1]
    nuline = nuline.split("/")[0]

    nu_game = [nuline, datetime.now()]
    games.append(nu_juego)


def finish_op(nuline):
    nuline = nuline.split("/common/")[-1]
    nuline = nuline.split("/")[0]

    for i in games:
        if i[0] == nuline:
            games.remove(i)

            now = datetime.now()
            diff = now - i[1]
            format_code = '%Y-%m-%d,%H:%M:%S'

            f = open("/YOUR-PATH/steamPlayLog.csv", "a")
            entry = nuline + "," + i[1].strftime(format_code) + "," + \
                now.strftime(format_code) + "," + \
                str(int(diff.seconds/60 +1)) + "\n"

            f.write(entry)
            f.close()

def main():
    p = Popen(['/usr/bin/steam-runtime', '%U'], stdin=PIPE, stdout=PIPE, stderr=STDOUT, bufsize=10000)
    for line in p.stdout:
        exitcode = p.poll
        if (exitcode == 0) or (exitcode == 1): 
            exit()
        
        nuline = str(line)

        if ("Game process added" in nuline):
            launch_op(nuline)  
        if ("Game process removed" in nuline):
            finish_op(nuline)  


if __name__ == '__main__':
    main()
