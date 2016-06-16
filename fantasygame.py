game = {
	"tom":{'rope': 2, 'torch': 1, 'gold coin': 442, 'dagger': 1, 'arrow': 12},
	"jack":{'rope': 6, 'torch':2, 'gold coin': 142, 'dagger': 1, 'arrow': 25},
	"kent":{'rope': 5, 'torch': 2, 'gold coin': 2, 'dagger': 0, 'arrow': 1}
}

def inventoryCounts(player,item):
	numInv = 0
	for k,v in player.items():
		numInv = numInv + v.get(item,0)
	return numInv

print ("%s ropes" %inventoryCounts(game,'rope'))
