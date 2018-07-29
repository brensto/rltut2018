class Tile:
	#A tile on the map. May or may not block movement or sight.
	def __init__(self, blocked, block_sight=None):
		self.blocked = blocked

		#By default, if a tile is blocked to movement it will also block sibht
		if block_sight is None:
			block_sight = blocked

		self.block_sight = block_sight

		self.explored = False

		