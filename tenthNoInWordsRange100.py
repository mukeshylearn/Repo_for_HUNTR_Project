from num2words import num2words
print("PRINTING NUMBERS FROM 0 TO 100")
for i in range(0,101):
	print(i)
	if (i % 10 == 0) & (i != 0) :
		print(f"PRINTING WORDY VERSION OF {i} : {num2words(i)}")
