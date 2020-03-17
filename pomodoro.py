import time
import argparse
import os
from collections import defaultdict
from tqdm import tqdm

def _clear():
    try:
        os.system("clear")
    except:
        os.system("cls")

def main(work_time, rest_time, n, work_color, rest_color):
    colors = defaultdict(lambda: "\033[0;0m")
    colors['red'] =  "\033[1:31m"
    colors['blue'] = "\033[1;34m"
    colors['cyan'] = "\033[1;36m"
    colors['green'] = "\033[0;32m"
    colors['reset'] = "\033[0;0m"

    # TODO: actual infinite time <16-03-20, vvvm23> #
    try:
        for i in range(999999 if n == None else n):
            _clear()
            print(f"Pomodoro Cycle {i+1}" + ("" if n == None else f"/{n}"))
            print(colors[work_color])
            with tqdm(total=work_time, desc='Working time', dynamic_ncols=True,
                      bar_format='{desc} {percentage:3.0f}% |{bar}| Remaining Time: {remaining}    ') as pbar:
                for t in range(work_time):
                    time.sleep(1)
                    pbar.update(1)

            input(colors['reset'] + "Press ENTER to continue to resting..")
            if n != None and i==n-1:
                break

            print(colors[rest_color])
            with tqdm(total=rest_time, desc='Resting time', dynamic_ncols=True,
                      bar_format='{desc} {percentage:3.0f}% |{bar}| Remaining Time: {remaining}') as pbar:
                for t in range(rest_time):
                    time.sleep(1)
                    pbar.update(1)
            input(colors['reset'] + "Press ENTER to continue working..")
    except KeyboardInterrupt as e:
        print(colors['reset'])
        print("Thanks for studying with me!")
        exit()
    except Exception as e:
        raise e
    print(colors['reset'])
    print("Thanks for studying with me!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Command Line Program to enforce the Pomodoro technique")

    parser.add_argument("--wt", help="Amount of time on focused work in minutes.", default=25)
    parser.add_argument("--rt", help="Amount of time resting in minutes.", default=5)
    parser.add_argument("-n", help="Number of cycles to do.", default=None)
    parser.add_argument("--wc", help="Color of the progress bar in work mode.", default='red')
    parser.add_argument("--rc", help="Color of the progress bar in rest mode.", default='green')

    args = parser.parse_args()
    main(int(args.wt)*60, int(args.rt)*60, None if args.n == None else int(args.n), args.wc, args.rc)
