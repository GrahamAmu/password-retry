#密碼重試程式
n = 3
while n > 0 :
	password = input("請輸入一組密碼: ")
	if password == "a123456":
		print("登入成功")
		break
	else:
		print("密碼錯誤! 還有",n-1,"次機會")
	n -= 1
