import csv
import random
import math




c = 0
while c < 10000:
    while True:

        Computer_Rock = 0
        Computer_Paper = 0
        Computer_Scissors = 0
   
        CR_Overall = 0
        CP_Overall = 0
        CS_Overall = 0

        Possible_choice = ["rock", "paper", "scissors"]
        Computer_choice = random.choice(Possible_choice)
        break

    if Computer_choice == "rock":
        Computer_Rock += 1

    elif Computer_choice == "paper":
        Computer_Paper += 1

    elif Computer_choice == "scissors":
        Computer_Scissors +=1

    with open("leaderboard.csv", "r") as f:
        RPS_Data = csv.reader(f)

        Win_Overall = 0
        Draw_Overall = 0
        Losses_Overall = 0
        for line in RPS_Data:
            if line:
                try:
                    Win_Overall += int(line[0])
                    Draw_Overall += int(line[1])
                    Losses_Overall += int(line[2])
                except ValueError:
                    print("Skip Line Error")
                    continue
        
    with open("ComputerRPS_Choice.csv", "a") as CPchoice_Data:
        CPchoice_Data.write(f"{Computer_Rock},{Computer_Paper},{Computer_Scissors}\n")

    with open("ComputerRPS_Choice.csv", "r") as Cfile:
        CPchoice_Data = csv.reader(Cfile)
        
        for line in CPchoice_Data:
            if line:
                try:
                    CR_Overall += int(line[0])
                    CP_Overall += int(line[1])
                    CS_Overall += int(line[2])
                except ValueError:
                    print("Skip Line Error")
                    continue
    c += 1
print ("10,000 Computer Answers Generated")