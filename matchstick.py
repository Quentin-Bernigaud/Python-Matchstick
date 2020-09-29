a = l = m = int(input("Entrez le nombre d'étages : "))
for i in range(l):
    output = ""
    output += " " * (l-i)
    output += "|" + 2 * ("|" * i)
    print(output)
m = int(input("Combien est-ce qu'on retire d'allumette (Max : "+str(a)+" ? : "))
n = int(input("Sur quelle ligne ? : "))