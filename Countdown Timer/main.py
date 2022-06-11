import time

def countdown(start):
    while start:
        mins, secs = divmod(start,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        start -= 1

    print(f'TIMER DONE')

start = int(input('Enter time in seconds: '))

countdown(start)