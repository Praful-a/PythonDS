# Time Complexity = O(n^2) space = O(n)
# def printDups(string):
# 	n = len(string)
# 	visited = [False for _ in range(n)]
# 	for i in range(n):
# 		if visited[i] == True:
# 			continue
# 		count = 1
# 		for j in range(i+1, n):
# 			if string[i] == string[j]:
# 				visited[j] = True
# 				count += 1
# 		if count > 1:
# 			print(string[i], count)

# Time Complexity = O(N log N) Space = O(k) where k is size of map
def printDups(string):
	m = {}
	for i in range(len(string)):
		if string[i] not in m:
			m[string[i]] = 1 
		else:
			m[string[i]] += 1
	for i in m:
		if m[i] > 1:
			print(i, m[i])

string = "test string"
printDups(string)