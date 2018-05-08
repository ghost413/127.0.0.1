#!/usr/bin/env python
from queue import PriorityQueue


class State(object):
	def __init__(self, value, parent, start=0, goal=0):
		self.children = []
		self.parent = parent
		self.value = value
		self.dist = 0

		if parent:
			self.path = parent.path[:]
			self.path.append(value)
			self.start = parent.start
			self.goal = parent.goal
		else:
			self.path = [value]
			self.start = start
			self.goal = goal

	def GetDist(self):
		pass

	def CreateChildren(self):
		pass


class StateString(State):
	def __init__(self, value, parent, start=0, goal=0):
		super(StateString, self).init(value, parent, start, goal)

	def GetDist(self):
		if self.value == self.goal:
			return 0
		dist = 0
		for i in range(len(self.goal)):
			letter = self.goal[i]
			dist += abs(i - self.value.index(letter))

	def CreateChildren(self):
		if not self.children:
			for i in xrange(len(self.goal) - 1):
				val = self.value
				val = val[:i] + val[i + 1] + val[i] + val[i + 2:]
				child = StateString(val, self)
				self.children.append(child)

	class AStarSolver:
		def __init__(self, start, goal):
			self.path = []
			self.visitedQueue = []
			self.PriorityQueue = PriorityQueue()
			self.start = start
			self.goal = goal

		def Solver(self):
			startState = StateString(self.start, 0, self.start, self.goal)
			count = 0
			self.PriorityQueue.put((0, count, startState))
			while(not self.path and self.PriorityQueue.qsize):
				closestChild = self.PriorityQueue.get()[2]
				closestChild.CreateChildren()
				self.visitedQueue.append(closestChild.value)
				for child in closestChild.children:
					if child.value not in self.visitedQueue:
						count += 1
						if not child.dist:
							self.path = child.path
							break
						self.PriorityQueue.put((child.dist, count))
				if not self.path:
					print('Goal of ' + self.goal + ' is not possible.')
				return self.path

		if __name__ == '__main__':
			start1 = 'hma'
			goal1 = 'ham'
			print('Starting...')
			a = AStarSolver(start1, goal1)
			a.Solve()
			for i in xrange(len(a.path)):
				print('%d) ' % i + a.path[i])
