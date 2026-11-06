import argparse
import time
start_time = time.time()


#recurvise implementation, this seems to be the easiest way to implement this.
#I mean I could have easily done an iterative approach but whatever
def moveTower(height,froP, toP, witP):
    if height >= 1:
        moveTower(height-1,froP,witP,toP)
        moveTower(height-1,witP,toP,froP)




parser = argparse.ArgumentParser()
parser.add_argument("discs", type=int, help="Number of discs to run with", default=100)
args = parser.parse_args()
N = args.discs

moveTower(N,"A","B","C")
print("done in %s secs" % (time.time() - start_time)) 
