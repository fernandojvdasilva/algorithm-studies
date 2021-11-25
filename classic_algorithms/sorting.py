

# sa, ea -> Start and End of array A 
# sb, eb -> Start and End of array B
def merge(sa, ea, sb, eb, arr):
	ia = sa
	ib = sb
	sorted_arr = []
	while ia < ea and ib < eb:
		if arr[ib] < arr[ia]:
			sorted_arr.append(arr[ib])
			ib += 1
		else:
			sorted_arr.append(arr[ia])
			ia += 1

	j = 0
	for i in range(sa, eb):
		arr[i] = sorted_arr[j]
		j += 1

	return arr


def merge_sort(s, e, arr):
	if e - s > 1:
		arr = merge_sort(s, (e/2), arr)
		arr = merge_sort((e/2), e, arr)
		arr = merge(s, (e/2), (e/2), e, arr)

	return arr	