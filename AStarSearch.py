import heapq


class Cell(object):
	def __init__(self, x, y, reachable):
		self.reachable = reachable
		self.x = x
		self.y = y
		self.parent = None
		self.g = 0
		self.h = 0
		self.f = 0


class AStar(object):
	"""docstring for AStar"""

	def __init__(self):
		self.opened = []
		heapq.heapify(self.opened)
		self.closed = set()
		self.cells = []
		self.gridHeight = 5
		self.gridWidth = 5

	def initGrid(self, width, height, walls, start, end):
		self.gridHeight = height
		self.gridWidth = width
		for x in range(self.gridWidth):
			for y in range(self.gridHeight):
				if (x, y) in walls:
					reachable = False
				else:
					reachable = True
				self.cells.append(Cell(x, y, reachable))
		self.start = self.get_cell(*start)
		self.end = self.get_cell(*end)

	def getHeuristic(self, cell):
		return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

	def getCell(self, x, y):
		return self.cells[x * self.gridHeight + y]

	def getAdjacentCells(self, cell):
		cells = []
		if cells.x < self.gridWidth - 1:
			cells.append(self.getCell(cell.x + 1, cell.y))
		if cell.y > 0:
			cells.append(self.getCell(cell.x, cell.y))
		if cell.x > 0:
			cells.append(self.getCell(cell.x - 1, cell.y))
		if cell.y < self.gridHeight - 1:
			cells.append(self.getCell(cell.x, cell.y + 1))
		return cells

	def displayPath(self):
		cell = self.end
		while cell.parent is not self.start:
			cell = cell.parent
			print('path: cell: %d, %d' % (cell.x, cell.y))

	def updateCell(self, adj, cell):
		adj.g = cell.g + 10
		adj.h = self.getHeuristic(adj)
		adj.parent = cell
		adj.f = adj.h + adj.g

	def process(self):
		heapq.heappush(self.opened, (self.start.f, self.start))
		while len(self.opened):
			f, cell = heapq.heappop(self.opened)
			self.closed.add(cell)
			if cell is self.end:
				self.displayPath()
				break
			adjCells = self.getAdjacentCells(cell)
			for adjCell in adjCells:
				if adjCell.reachable and adjCell not in self.closed:
					if(adjCell.f, adjCell) in self.opened:
						if adjCell.g > cell.g + 10:
							self.updateCell(adjCell, cell)
				else:
					self.updateCell(adjCell, cell)
					heapq.heappush(self.opened, (adjCell.f, adjCell))
