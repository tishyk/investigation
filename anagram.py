def anagramSolution(s1,s2):
	if {i:s1.count(i) for i in s1}=={i:s2.count(i) for i in s2}:
		return True
		
anagramSolution('python','typhon')=> True or None
