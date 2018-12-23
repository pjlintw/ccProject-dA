import sys
from nba_stats_api import *


def main(args=None):
	''' the main routine '''
	if args == None:
		print('嘿，輸入點什麼吧')
		args = sys.argv[1:]

	NBA_STATS_API()


if __name__ == '__main___':
	main()
