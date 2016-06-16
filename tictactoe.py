import pprint

theBoard = {'topL':'O','topM':'O','topR':'O',
	    'midL': 'X','midM': 'X', 'midR': ' ',
	    'lowL': ' ','lowM': ' ','lowR': 'X'	}

def printBoard(board):
	print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
	print ('-+-+-')
	print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
	print ('-+-+-')
	print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])


#printBoard(theBoard)

turn  = 'X'

for i in xrange(9):

	printBoard(theBoard)
	print('Turn for ' + turn + '. Move on which space?')
	
	move = raw_input()

	theBoard[move] = turn
	
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

pprint.pprint(theBoard)
