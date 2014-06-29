def minPay1(balance, annualInterestRate, monthlyPaymentRate):
	monthlyInterestRate = annualInterestRate/12
	prevBalance = balance
	month = 0
	totalPaid = 0
	while month<12:
		month +=1
		print('Month: ' + str(month))
		minMonthlyPayment = monthlyPaymentRate*prevBalance
		monthlyUnpaidBalance = prevBalance - minMonthlyPayment
		totalPaid += minMonthlyPayment
		prevBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
		print('Minimum monthly payment: ' + "%.2f" % minMonthlyPayment)
		print('Remaining balance: ' + "%.2f" % prevBalance)
	print('Total paid: ' + "%.2f" % totalPaid)
	print('Remaining balance: ' + "%.2f" % prevBalance)

s = 'naaihuos'
total = s.count('a') + s.count('i') + s.count('o') + s.count('u') + s.count('e')
print('Number of vowels: ' + str(total))
s = 'obobobobztbobobobobohbo'

def countBobs(s):
    i = 0
    count = 0
    while i<=(len(s)-3):        
        if(s[i]=='b'):
            if(s[i+1]=='o' and s[i+2]=='b'):
                count +=1
        i+=1
    print('Number of times bob occurs is:' + str(count))
countBobs(s)
	
