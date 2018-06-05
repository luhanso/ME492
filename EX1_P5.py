# Lucas Hanson - Exam 1 - Problem 5

CoefList = [5,4,3,2,1]
x = 2

N = len(CoefList)
SortList = sorted(CoefList)
sum = 0

for i in range(N):
	poly = SortList[i]*x**i
	sum = sum + poly
	print('sum = '+ str(sum))

	

