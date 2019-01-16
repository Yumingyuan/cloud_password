dict=["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"
,"U","V","W","X","Y","Z"]
dictnum={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
str="8842101220480224404014224202480122"
lists=str.split('0')
char=''
for word in lists:
	sum=0
	for c in word:
		sum+=dictnum[c]
	char+=dict[sum]
print char
