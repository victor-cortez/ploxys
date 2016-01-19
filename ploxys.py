from random import randint
import os

#function to save your images in order
def sanitize(num):
    cadeia = str(num)
    zeros = 9 - len(cadeia)
    adicao = "0" * zeros
    return adicao + cadeia
# never let the children number get below zero
def nozero(inteiro):
    if inteiro > 0:
        return inteiro
    else:
        return 0
print("Ploxys version 1.1")
# simulation values
num_ploxys = int(input("Type the initial amount of ploxys: "))
num_foods = int(input("Type the initial amount of food: "))
num_rounds = int(input("Type the number of rounds: "))
min_lifespan = int(input("Type the minimal initial lifespan: "))
max_lifespan = int(input("Type the maximal initial lifespan: "))

#creating the data directory
diretorio = input("Type the data directory's name: ")
os.makedirs(diretorio)
os.chdir(diretorio)
data_initial_ploxys = open("data_intial_ploxys.txt","w")

# here the ploxys are creates, each ploxy is a list holding its x, its y , how many roudns it will live, his birthdate and his generation and how many children it will give birth respectively
ploxys = [[randint(1,900),randint(1,900),randint(min_lifespan,max_lifespan),randint(((-1) * (min_lifespan - 1)),0),0,randint(1,4)]   for i in range(0,num_ploxys)  ]
data_initial_ploxys.write("\n".join([str(i) for i in ploxys]))
data_initial_ploxys.close()

# the calculation of the average initial ploxys lifespan
soma = 0
filhagem = 0
for ploxy in ploxys:
    soma += ploxy[2]
    filhagem += ploxy[5]
media = soma / num_ploxys
media_filhagem = filhagem / num_ploxys

# here the inital foods are create, each one is a list holding its position in x and y
foods = [[randint(1,901),randint(1,901)] for i in range (0,num_foods)]

# base numbers to calculate the average lifespan of the reproduced ploxys
soma_reproduzidos = 0
filhagem_reproduzidos = 0
count = 0

# data storage
data_run_test = open("data_run_teste.txt","w")
conta = 0

tabela = open("table.txt","w")
# the simulation starts
for i in range (0,num_rounds):


    # each ploxy moves ramdomly from -5 to 5 pixels in each round, if the ploxy lifespan is over, the ploxy does not goes into the next round
    ploxys = [ [(ploxy[0] + randint(-5,5)) % 900 ,(ploxy[1] + randint(-5,5)) % 900,ploxy[2],ploxy[3], ploxy[4],ploxy[5]] for ploxy in ploxys if ploxy[2] + ploxy[3] > i]



    # it chekcs if any food has been eaten, if it has, the food will be deleted
    for food in foods:
        eaten = False
        for ploxy in ploxys:
            if [ploxy[0],ploxy[1]] == food:
                eaten = True
                # the ploxy that ate the food, generates children and a new food is generated
                for i in range(0,ploxy[5]):
                    ploxys.append([ploxy[0],ploxy[1],ploxy[2] + randint(-5,5),conta,ploxy[4] + 1,nozero(ploxy[5] + randint(-1,1))])
                foods.append([randint(0,900),randint(0,900)])
                soma_reproduzidos += ploxy[2]
                filhagem_reproduzidos += ploxy[5]
                count += 1
                data_run_test.write("This ploxy ate and reproduced : " + str(ploxy) + "\n")
                print ("This ploxy ate and reproduced : " + str(ploxy))
                break

        # if the food is eaten, it is removed
        if eaten ==  False:
            pass
        else:
            foods.remove(food)
    #data storage
    data_run_test.write("Round number " + str(conta) + " and with " + str(len(ploxys)) + " alive\n")
    tabela.write(str(conta) + " " + str(len(ploxys)) + "\n")
    print ("Round number " + str(conta) + " and with " + str(len(ploxys)) + " alive")
    if len(ploxys) == 0:
        data_run_test.write("The population died")
        print ("The population died")
        break
    conta += 1
    #processing the collected data and calculating the averages
data_run_test.close()
media_reproduzidos = soma_reproduzidos / count
media_filhagem_reproduzidos = filhagem_reproduzidos / count

tabela.close()
data_final_ploxys = open("data_final_ploxys.txt","w")


# it shows how many ploxys survived, e saves the final data and averages
soma_sobreviventes = 0
soma_filhagem = 0
for ploxy in ploxys:
    soma_sobreviventes += ploxy[2]
    soma_filhagem += ploxy[5]
if len(ploxys) > 0:
    media_sobreviventes = soma_sobreviventes / len(ploxys)
    media_filhagem_finalistas = soma_filhagem / len(ploxys)
else:
    media_filhagem_finalistas = 0
    media_sobreviventes = 0
print ("--------")
data_final_ploxys.write("\n".join([str(i) for i in ploxys]))
data_final_ploxys.close()
data_final = open("data_final.txt","w")

data_final.write("The game started with %d ploxys, but ends with %d ploxys.\n" % (num_ploxys,len(ploxys)))
data_final.write("The average lifespan of the initial ploxys was: %f rounds\n" % media)
data_final.write("The average lifespan of the reproduced ploxys was: %f rounds\n" % media_reproduzidos)
data_final.write("The average lifespan of the remaining ploxys is: %f rounds\n" % media_sobreviventes)
data_final.write("The average number of children per birth of the initial ploxys was: %f children\n" % media_filhagem)
data_final.write("The average number of children per birth of the reproduced ploxys was: %f children\n" % media_filhagem_reproduzidos)
data_final.write("The average number of children per birth of the remaining ploxys is: %f children\n" % media_filhagem_finalistas)
data_final.close()
print ("The game started with %d ploxys, but ends with %d ploxys." % (num_ploxys,len(ploxys)))
print ("The average lifespan of the initial ploxys was: %f rounds" % media)
print ("The average lifespan of the reproduced ploxys was: %f rounds" % media_reproduzidos)
print ("The average lifespan of the remaining ploxys is: %f rounds" % media_sobreviventes)
print ("The average number of children per birth of the initial ploxys was: %f children" % media_filhagem)
print ("The average number of children per birth of the reproduced ploxys was: %f children" % media_filhagem_reproduzidos)
print ("The average number of children per birth of the remaining ploxys is: %f children" % media_filhagem_finalistas)
