#testing 3way merge
#x = (start + end // 2)
#start + x // 2
#x + end // 2
 0 1 2
[3,2,1]
start = 0 end = 2
mid = 0 + 2 // 2 === 1 -> [2]

3rd = 0 + 1 // 2 === 0 -> [1]

3/4ths = 1 + 2 // 2 === 1 -> [1]

start to 3rd   3rd + 1 to 3/4ths   3/4ths + 1 to end
0 to 0            1 to 1               2 to 2
 
 
 
 0 1
[1,2]
start = 0 end 1
mid = 0 + 1 // 2 === 0

3rd = 0 + 0 // 2 === 0
3/4ths = 0 + 1 // 2 === 0

start to 3rd  3rd + 1 to 3/4ths    3/4ths + 1 to end
0 to 0             1 to 0             1 to 1