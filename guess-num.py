import random
while True:
	start = input('請決定隨機數字的起始值：')
	end = input('請決定隨機數字的結束值：')
	start = int(start)
	end = int(end)
	if start > end:
		print('起始值不得大於結束值，請重新設定。')
	else:
		r = random.randint(start, end)
		count = 0
		while True:
			count += 1 # count = count + 1
			num = input('請猜數字：')
			num = int(num)
			if num == r:
				print('恭喜你猜對了！')
				print('這是你猜的第', count, '次')
				break
			elif num > r:
				print('比答案大唷，再猜猜！')
				print('這是你猜的第', count, '次')
			elif num < r:
				print('比答案小唷，再猜猜！')
				print('這是你猜的第', count, '次')

