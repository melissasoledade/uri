# URI 1052
# Switch case em python para escolha dos meses

def switch_case(number):
	switcher = {
		1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
	}
	return switcher.get(number, "Invalid month")

if __name__ == '__main__':
	number = int(input())
	print(switch_case(number))