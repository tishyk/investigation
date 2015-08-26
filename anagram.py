def anagramSolution(s1,s2):
	if {i:s1.count(i) for i in s1}=={i:s2.count(i) for i in s2}:
		return True
# in 1 row - anagramCheking = lambda s1,s2:{i:s1.count(i) for i in s1}=={i:s2.count(i) for i in s2}		
anagramSolution('python','typhon')=> True or None
