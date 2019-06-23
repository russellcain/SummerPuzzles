#**Sorting** - Implement two types of sorting algorithms: Merge sort and bubble sort.

# Bubble Sort O(N^2): Check pairwise elements and swap if out of order (i.e. something will 'bubble' to the top if it isn't meant to be at the bottom). If everything is in place, the array is sorted!
	# Can speed up Bubble Sorting by alternating how you read through the array, giving everything a chance to #BubbleUp2019

def BubbleSort(entries):
	print("Bubble Sorting: ", entries)
	needsSorting, stepsTaken = True, 0
	indices = range(len(entries[:-1])) # why keep calculating this, eh? The list length won't change anytime soon
	while needsSorting:
		for i in indices:
			needsSorting = False # be hopeful
			if (entries[i] > entries[i+1]):
				t = entries[i] # temp value for swap
				entries[i] = entries[i+1]
				entries[i+1] = t
				needsSorting = True
				stepsTaken += 1
	print("It took %i steps to arrive at: "%(stepsTaken), entries)

testing = [1,4,2,6,3,3,5]

BubbleSort(testing)

# Merge Sort O(N log N): This recursive algorithm breaks the array into (somewhat) concentric halves (if that makes sense). 

def MergeSort(entries, scratch, start, end):
	if start == end:
		return 

	midpoint = (start + end) // 2

	MergeSort(entries, scratch, start, midpoint)
	MergeSort(entries, scratch, midpoint + 1, end)

	left, right, scratch_index = start, midpoint+1, start
	while ((left < midpoint) and (right < end)):
		if entries[left] <= entries[right]:
			scratch[scratch_index] = entries[left]
			left += 1
		else:
			scratch[scratch_index] = entries[right]
			right += 1
			scratch_index += 1
	for i in range(left, midpoint+1):
		scratch[scratch_index] = entries[i]
		scratch_index += 1
	for i in range(right, end):
		scratch[scratch_index] = entries[i]
		scratch_index += 1
	for i in range(start, end):
		entries[i] = scratch[i]
	print("recursion done", entries)
	return entries

f = MergeSort(testing, [i for i in range(len(testing))], 0, len(testing))
print("Merge sort, baby", f)


