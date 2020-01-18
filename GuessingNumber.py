import random
# import sys
# import time
class UserInput:

    def takeInput(self):

        userInput = input()
        return userInput

    def numberChecker(self,number):
        try:
            if number == "!":
                return number
            typecastedNumber = int(number)
            return typecastedNumber
        except:
            print(" Enter a valid number :")
            return self.numberChecker(self.takeInput())

class  GuessingNumber:

    def numberGenerator(self):
        generatedNumber = random.randint(0,100)
        return generatedNumber

class CheckNumber(GuessingNumber):

    def generatedNumber(self):
        return GuessingNumber.numberGenerator(self)

    def matchNumber(self, gussedNumber):
        # print(self.gussedNumber())
        generatedNumber = self.generatedNumber()

        if gussedNumber == generatedNumber:
            return 0, generatedNumber
        elif gussedNumber < generatedNumber:
            return -1, generatedNumber
        else:
            return 1, generatedNumber

    def matchNumbers(self,gussedNumber,generatedNumber):
        if gussedNumber == generatedNumber:
            return 0
        elif gussedNumber < generatedNumber:
            return -1
        else:
            return 1

class Design:
    
    def design(self,specialCharacter):
        print(specialCharacter*50)


class Message(Design):

    def toHome(self):
        return "\n Thanks for playing. Choose another option.. "

    def bye(self):
        return "\n Thanks for playing. Come again to play.. Bye..."

    def welcome(self):
        print("\n### Welcome to the Jungle ###\n")

    def showMenu(self):
        # time.sleep(1)
        self.design("#")
        # print(" type -> ! -> to exit the game. ")
        print(" Press SHIFT +\n")
        print(" 1. Exit ")
        print(" 2. Easy ")
        print(" 3. Extream ")
        self.design("#")

    def exitChoice(self):
        self.design("#")
        print(" Press SHIFT +\n")
        print(" 1. Exit ")
        self.design("#")
        print(" Enter your number :")

class startGame:

    msg = Message()
    dg = Design()

    def checkUserInput(self, generatedInput, this_msg):

            ui = UserInput()
            inputNumber = ui.takeInput()
            if inputNumber == "!":
                # exit() # shows dialogue box to kill
                self.dg.design("@")
                if generatedInput == 0:
                    print(this_msg+\
                    self.msg.toHome()+"\n"+("@"*50))
                    return inputNumber
                print(this_msg+str(generatedInput)+\
                    self.msg.toHome()+"\n"+("@"*50))
                return inputNumber
            
            userInput = ui.numberChecker(inputNumber)
            # print(isinstance(userInput,int))

            if userInput == "!":
                # exit() # shows dialogue box to kill
                self.dg.design("@")
                if generatedInput == 0:
                    print(this_msg+\
                    self.msg.toHome()+"\n"+("@"*50))
                    return userInput
                print(this_msg+str(generatedInput)+\
                    self.msg.toHome()+"\n"+("@"*50))
                return userInput

            return userInput

    def sameCode(self, output):

        if output == 0:
            self.dg.design("*")
            print(" You Made It!" )
            print(self.msg.toHome())
            self.dg.design("*")
            return "home"

        elif output == -1:
            self.dg.design("*")
            print(" Your Guess is Low... ")
            self.dg.design("*")

        else:
            self.dg.design("*")
            print(" Your Guess is High... ")
            self.dg.design("*")

    def Easy(self):
        
        gn = GuessingNumber()
        generatedInput = gn.numberGenerator()
        # print(generatedInput)
        gusse_msg = " Gussed number was "

        while(True):         
            
            userInput = self.checkUserInput(generatedInput, gusse_msg)
            if userInput == "!":
                return "home"

            cn = CheckNumber()
            output = cn.matchNumbers(userInput,generatedInput)

            ifyoumadeit = self.sameCode(output)
            if ifyoumadeit == "home":
                return "home"

    def Extream(self):
        
        Flag = 1
        generatedInput = 0
        gusse_msg = " Gussed number was "
        nothing_msg = " Nothing Gussed Yet! "
        
        while(True):         
            if Flag == 1:
                Flag =  0
                userInput = self.checkUserInput(0,nothing_msg)
            else:
                userInput = self.checkUserInput(generatedInput, gusse_msg)

            if userInput == "!":
                return "home"

            cn = CheckNumber()
            output, generatedInput = cn.matchNumber(userInput)

            ifyoumadeit = self.sameCode(output)
            if ifyoumadeit == "home":
                return "home"

class EndGames:

    ui = UserInput()
    msg = Message()
    dg = Design()
    s = startGame()

    msg.welcome()
    msg.showMenu()

    while(True):
        userChoice = ui.takeInput()
        if userChoice == "!":
            # exit() # shows dialogue box to kill
            dg.design("@")
            exit(msg.bye()+"\n"+("@"*50))
            # sys.exit(msg.bye()+"\n"+("@"*50))
            
        elif userChoice == "@":
            msg.exitChoice()
            homeCheck = s.Easy()
            if homeCheck == "home":
                msg.showMenu()
                continue 
            # break

        elif userChoice == "#":
            msg.exitChoice()
            homeCheck = s.Extream()
            if homeCheck == "home":
                msg.showMenu()
                continue 

        else:
            dg.design("$")
            msg.showMenu()
            dg.design("$")
            continue
        
if __name__ == "__main__":

    EndGames()




