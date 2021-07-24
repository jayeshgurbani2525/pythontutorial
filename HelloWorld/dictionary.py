phone = input("phone: ")
digits_maping = {
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
}
output = ""
for ch in phone: 
	output += digits_maping.get(ch, "!") + " "
print(output)