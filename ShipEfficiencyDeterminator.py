import datetime

username = raw_input("Welcome to the Ship Efficiency Determiner. Please input your username, so I know how to reffer to you from now on.")
print("Loading...")
print("...")
print("Loaded.")

now = datetime.datetime.now()
print ("Current date and time:")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

shipClass = raw_input("Okay, " + username + ". Tell me what class your ship is. (Please use capitalized forms, eg. Starfighter, Corvette, Star Destroyer, etc.")
#Typing in "CALIBRATION" opens up a secret option.

#Refer to SED_functions_bulk.py for all functions listed below, as well as a breakdown

#---------------------------Starfighter------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Starfighter():

    print("Okay, so it's a Starfighter. These ships are very fast, and the smallest type of ship currently available.")
    print("The most common weapon found on fighters are plasmas. 2 plasmas are oftentimes the best.")
    print("Size: 100-500")
    print("Power output: 25000")
    print("The current meta stats of this class are as follows:")

    shieldRegen = 10 #Input Meta ship info here
    shieldReinforcement = 10 #Input Meta ship info here
    cruiseSpeed = 10 #Input Meta ship info here
    cruiseAcceleration = 10 #Input Meta ship info here
    numberOfPlasmas = 10 #Input Meta ship info here
    hasIons = "yes" #Input Meta ship info here

    print("Shield regen: " + str(shieldRegen))
    print("Shield reinforcement: " + str(shieldReinforcement)) #Displays meta info
    print("Cruise speed: " + str(cruiseSpeed))
    print("Cruise acceleration: " + str(cruiseAcceleration))
    print("Number of plasmas: " + str(numberOfPlasmas))
    print("Has ion cannons: " + str(hasIons))
    print("-----------------------------------------------------")
    print("Keep in mind, effectiveness is measured from 0-100%")
    print("If something is larger than 100%, then it's better than the meta.")
    print("-----------------------------------------------------")


    shieldRegenInput = float(raw_input("Enter your ship's shield regen divisor."))
    shieldReinforcementInput = float(raw_input("Enter your ship's shield reinforcement divisor.")) #Asks to input user's ship info
    cruiseSpeedInput = float(raw_input("Enter your ship's cruise speed."))
    cruiseAccelerationInput = float(raw_input("Enter your ship's acceleration."))
    numberOfPlasmasInput = float(raw_input("Enter your ship's plasma count."))
    hasIonsInput = str(raw_input("Does it have an ion cannon?"))
    
    shieldRegenOutput = float(((shieldRegenInput - shieldRegen) * 100) / shieldRegen) + 100       
    shieldReinforcementOutput = float(((shieldReinforcementInput - shieldReinforcement) * 100) / shieldReinforcement) + 100     
    cruiseSpeedOutput = float(((cruiseSpeedInput - cruiseSpeed) * 100) / cruiseSpeed) + 100        
    cruiseAccelerationOutput = float(((cruiseAccelerationInput - cruiseAcceleration) * 100) / cruiseAcceleration) + 100        
    numberOfPlasmasOutput = float(((numberOfPlasmasInput - numberOfPlasmas) * 100) / numberOfPlasmas) + 100   
    if hasIonsInput == hasIons:
        hasIonsOutput = 100
    weaponEffectiveness = float(((hasIonsOutput - numberOfPlasmasOutput) * 100) / shieldRegen) + 100
          

    print("Shield regeneration effectiveness:" + str(shieldRegenOutput) + "%")
    print("Shield reinforcement effectiveness:" + str(shieldReinforcementOutput) + "%")
    print("Cruise speed effectiveness:" + str(cruiseSpeedOutput) + "%")
    print("Cruise acceleration effectiveness:" + str(cruiseAccelerationOutput) + "%")
    print("Weapon effectiveness:" + str(weaponEffectiveness) + "%")

    totalVariables = 5

    totalEffectiveness = (int(shieldRegenOutput) + int(shieldReinforcementOutput) + int(cruiseSpeedOutput) + int(cruiseAccelerationOutput)) / totalVariables

    print("-----------------------------------------------------")
    print("And, with that, I have calculated that the general effectiveness of your ship is: ")
    print(str(totalEffectiveness) + "%")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------Corvette------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Corvette():

    print("Corvettes. More reliable and spaceous than a fighter, overall a nice warship.")
    print("Their small size and enhanced power output makes them a starfighter on steroids.")
    print("Size: 500-2000")
    print("Power output: 35000")
    print("The current meta stats of this class are as follows:")

    shieldRegen = 10 #Input Meta ship info here
    shieldReinforcement = 10 #Input Meta ship info here
    cruiseSpeed = 10 #Input Meta ship info here
    cruiseAcceleration = 10 #Input Meta ship info here
    numberOfPlasmas = 10 #Input Meta ship info here
    numberOfShields = 10 #Input Meta ship info here
    HyperdriveTier = 10 #Input Meta ship info here
    blockCount = 10 #Input Meta ship info here
    optimalBlockCount = blockCount**1.1 #Smaller ships tend to be better off close to full block count
    hasIons = "yes" #Input Meta ship info here

    print("Shield regen: " + str(shieldRegen))
    print("Shield reinforcement: " + str(shieldReinforcement)) #Displays meta info
    print("Cruise speed: " + str(cruiseSpeed))
    print("Cruise acceleration: " + str(cruiseAcceleration))
    print("Number of plasmas: " + str(numberOfPlasmas))
    print("Has ion cannons: " + str(hasIons))
    print("Number of shields: " + str(numberOfShields))
    print("Hyperdrive tier: " + str(HyperdriveTier))
    print("Block count: " + str(blockCount))
    print("Optimal block count (equation determined): " + str(optimalBlockCount))
    print("-----------------------------------------------------")
    print("Keep in mind, effectiveness is measured from 0-100%,")
    print("If something is larger than 100%, then it's better than the meta.")
    print("-----------------------------------------------------")


    shieldRegenInput = float(raw_input("Enter your ship's shield regen divisor."))
    shieldReinforcementInput = float(raw_input("Enter your ship's shield reinforcement divisor.")) #Asks to input user's ship info
    cruiseSpeedInput = float(raw_input("Enter your ship's cruise speed."))
    cruiseAccelerationInput = float(raw_input("Enter your ship's acceleration."))
    numberOfPlasmasInput = float(raw_input("Enter your ship's plasma count."))
    numberOfShieldsInput = float(raw_input("Enter your ship's shield count."))
    hyperdriveTierInput = float(raw_input("Enter your ship's hyperdrive tier."))
    blockCountInput = float(raw_input("Enter your ship's block count."))
    hasIonsInput = str(raw_input("Does it have an ion cannon?"))
    
    shieldRegenOutput = float(((shieldRegenInput - shieldRegen) * 100) / shieldRegen) + 100
    shieldReinforcementOutput = float(((shieldReinforcementInput - shieldReinforcement) * 100) / shieldReinforcement) + 100       
    cruiseSpeedOutput = float(((cruiseSpeedInput - cruiseSpeed) * 100) / cruiseSpeed) + 100        
    cruiseAccelerationOutput = float(((cruiseAccelerationInput - cruiseAcceleration) * 100) / cruiseAcceleration) + 100        
    numberOfPlasmasOutput = float(((numberOfPlasmasInput - numberOfPlasmas) * 100) / numberOfPlasmas) + 100       
    numberOfShieldsOutput = float(((numberOfShieldsInput - numberOfShields) * 100) / numberOfShields) + 100       
    hyperdriveTierOutput = float(((hyperdriveTierInput - HyperdriveTier) * 100) / HyperdriveTier) + 100
    blockCountOutput = float(((blockCountInput - blockCount) * 100) / blockCount) + 100
    optimalBlockCountOutput = float(((blockCountInput - optimalBlockCount) * 100) / optimalBlockCount) + 100
    if hasIonsInput == hasIons:
        hasIonsOutput = 100
    weaponEffectiveness = float(((hasIonsOutput - numberOfPlasmasOutput) * 100) / shieldRegen) + 100



    print("Shield regeneration effectiveness:" + str(shieldRegenOutput) + "%")
    print("Shield reinforcement effectiveness:" + str(shieldReinforcementOutput) + "%")
    print("Cruise speed effectiveness:" + str(cruiseSpeedOutput) + "%")
    print("Cruise acceleration effectiveness:" + str(cruiseAccelerationOutput) + "%")
    print("Weapon effectiveness:" + str(weaponEffectiveness) + "%")
    print("Shield count effectiveness: " + str(numberOfShieldsOutput) + "%")
    print("Hyperdrive tier effectiveness: " + str(hyperdriveTierOutput) + "%")
    print("Block count (size) effectiveness: " + str(blockCountOutput) + "%")
    print("You are this close to the optimal block count: " + str(optimalBlockCountOutput) + "%")

    totalVariables = 9

    totalEffectiveness = (int(shieldRegenOutput) + int(shieldReinforcementOutput) + int(cruiseSpeedOutput) + int(cruiseAccelerationOutput) + int(numberOfPlasmasOutput) 
        + int(numberOfShieldsOutput) + int(hyperdriveTierOutput) + int(blockCountOutput) + int(optimalBlockCountOutput) ) / totalVariables

    print("-----------------------------------------------------")
    print("And, with that, I have calculated that the general effectiveness of your ship is: ")
    print(str(totalEffectiveness) + "%")
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------Frigate------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Frigate():

    print("Of course, Frigates. The poor man's warship. This class isn't the best for combat ever since it's nerf.")
    print("This class, however, is best when used in numbers, or as part of a fleet.")
    print("Size: 2000-4000")
    print("Power output: 50000")
    print("The current meta stats of this class are as follows:")

    shieldRegen = 10 #Input Meta ship info here
    shieldReinforcement = 10 #Input Meta ship info here
    cruiseSpeed = 10 #Input Meta ship info here
    cruiseAcceleration = 10 #Input Meta ship info here
    numberOfPlasmas = 10 #Input Meta ship info here
    numberOfShields = 10 #Input Meta ship info here
    HyperdriveTier = 10 #Input Meta ship info here
    blockCount = 10 #Input Meta ship info here
    optimalBlockCount = blockCount**1.1 #Smaller ships tend to be better off close to full block count, larger ones are better at half count or 3/4.

    print("Shield regen: " + str(shieldRegen))
    print("Shield reinforcement: " + str(shieldReinforcement)) #Displays meta info
    print("Cruise speed: " + str(cruiseSpeed))
    print("Cruise acceleration: " + str(cruiseAcceleration))
    print("Number of plasmas: " + str(numberOfPlasmas))
    print("Number of shields: " + str(numberOfShields))
    print("Hyperdrive tier: " + str(HyperdriveTier))
    print("Block count: " + str(blockCount))
    print("Optimal block count (equation determined): " + str(optimalBlockCount))
    print("-----------------------------------------------------")
    print("Keep in mind, effectiveness is measured from 0-100%,")
    print("If something is larger than 100%, then it's better than the meta.")
    print("-----------------------------------------------------")


    shieldRegenInput = float(raw_input("Enter your ship's shield regen divisor."))
    shieldReinforcementInput = float(raw_input("Enter your ship's shield reinforcement divisor.")) #Asks to input user's ship info
    cruiseSpeedInput = float(raw_input("Enter your ship's cruise speed."))
    cruiseAccelerationInput = float(raw_input("Enter your ship's acceleration."))
    numberOfPlasmasInput = float(raw_input("Enter your ship's plasma count."))
    numberOfShieldsInput = float(raw_input("Enter your ship's shield count."))
    hyperdriveTierInput = float(raw_input("Enter your ship's hyperdrive tier."))
    blockCountInput = float(raw_input("Enter your ship's block count."))
    
    shieldRegenOutput = float(((shieldRegenInput - shieldRegen) * 100) / shieldRegen) + 100
    shieldReinforcementOutput = float(((shieldReinforcementInput - shieldReinforcement) * 100) / shieldReinforcement) + 100       
    cruiseSpeedOutput = float(((cruiseSpeedInput - cruiseSpeed) * 100) / cruiseSpeed) + 100        
    cruiseAccelerationOutput = float(((cruiseAccelerationInput - cruiseAcceleration) * 100) / cruiseAcceleration) + 100        
    numberOfPlasmasOutput = float(((numberOfPlasmasInput - numberOfPlasmas) * 100) / numberOfPlasmas) + 100       
    numberOfShieldsOutput = float(((numberOfShieldsInput - numberOfShields) * 100) / numberOfShields) + 100       
    hyperdriveTierOutput = float(((hyperdriveTierInput - HyperdriveTier) * 100) / HyperdriveTier) + 100
    blockCountOutput = float(((blockCountInput - blockCount) * 100) / blockCount) + 100
    optimalBlockCountOutput = float(((blockCountInput - optimalBlockCount) * 100) / optimalBlockCount) + 100



    print("Shield regeneration effectiveness:" + str(shieldRegenOutput) + "%")
    print("Shield reinforcement effectiveness:" + str(shieldReinforcementOutput) + "%")
    print("Cruise speed effectiveness:" + str(cruiseSpeedOutput) + "%")
    print("Cruise acceleration effectiveness:" + str(cruiseAccelerationOutput) + "%")
    print("Weapon effectiveness:" + str(numberOfPlasmasOutput) + "%")
    print("Shield count effectiveness: " + str(numberOfShieldsOutput) + "%")
    print("Hyperdrive tier effectiveness: " + str(hyperdriveTierOutput) + "%")
    print("Block count (size) effectiveness: " + str(blockCountOutput) + "%")
    print("You are this close to the optimal block count: " + str(optimalBlockCountOutput) + "%")

    totalVariables = 9

    totalEffectiveness = (int(shieldRegenOutput) + int(shieldReinforcementOutput) + int(cruiseSpeedOutput) + int(cruiseAccelerationOutput) + int(numberOfPlasmasOutput) 
        + int(numberOfShieldsOutput) + int(hyperdriveTierOutput) + int(blockCountOutput) + int(optimalBlockCountOutput) ) / totalVariables

    print("-----------------------------------------------------")
    print("And, with that, I have calculated that the general effectiveness of your ship is: ")
    print(str(totalEffectiveness) + "%")
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------Destroyer------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Destroyer():

    print("Destroyers are very nice warships. They are great support craft for things like interdictors.")
    print("Destroyers tend to be rather quick on their feet, and pack a punch.")
    print("Size: 4000-8000")
    print("Power output: 60000")
    print("The current meta stats of this class are as follows:")

    shieldRegen = 10 #Input Meta ship info here
    shieldReinforcement = 10 #Input Meta ship info here
    cruiseSpeed = 10 #Input Meta ship info here
    cruiseAcceleration = 10 #Input Meta ship info here
    numberOfPlasmas = 10 #Input Meta ship info here
    numberOfShields = 10 #Input Meta ship info here
    HyperdriveTier = 10 #Input Meta ship info here
    blockCount = 10 #Input Meta ship info here
    optimalBlockCount = blockCount**1.1 #Smaller ships tend to be better off close to full block count, larger ones are better at half count or 3/4.

    print("Shield regen: " + str(shieldRegen))
    print("Shield reinforcement: " + str(shieldReinforcement)) #Displays meta info
    print("Cruise speed: " + str(cruiseSpeed))
    print("Cruise acceleration: " + str(cruiseAcceleration))
    print("Number of plasmas: " + str(numberOfPlasmas))
    print("Number of shields: " + str(numberOfShields))
    print("Hyperdrive tier: " + str(HyperdriveTier))
    print("Block count: " + str(blockCount))
    print("Optimal block count (equation determined): " + str(optimalBlockCount))
    print("-----------------------------------------------------")
    print("Keep in mind, effectiveness is measured from 0-100%,")
    print("If something is larger than 100%, then it's better than the meta.")
    print("-----------------------------------------------------")


    shieldRegenInput = float(raw_input("Enter your ship's shield regen divisor."))
    shieldReinforcementInput = float(raw_input("Enter your ship's shield reinforcement divisor.")) #Asks to input user's ship info
    cruiseSpeedInput = float(raw_input("Enter your ship's cruise speed."))
    cruiseAccelerationInput = float(raw_input("Enter your ship's acceleration."))
    numberOfPlasmasInput = float(raw_input("Enter your ship's plasma count."))
    numberOfShieldsInput = float(raw_input("Enter your ship's shield count."))
    hyperdriveTierInput = float(raw_input("Enter your ship's hyperdrive tier."))
    blockCountInput = float(raw_input("Enter your ship's block count."))
    
    shieldRegenOutput = float(((shieldRegenInput - shieldRegen) * 100) / shieldRegen) + 100
    shieldReinforcementOutput = float(((shieldReinforcementInput - shieldReinforcement) * 100) / shieldReinforcement) + 100       
    cruiseSpeedOutput = float(((cruiseSpeedInput - cruiseSpeed) * 100) / cruiseSpeed) + 100        
    cruiseAccelerationOutput = float(((cruiseAccelerationInput - cruiseAcceleration) * 100) / cruiseAcceleration) + 100        
    numberOfPlasmasOutput = float(((numberOfPlasmasInput - numberOfPlasmas) * 100) / numberOfPlasmas) + 100       
    numberOfShieldsOutput = float(((numberOfShieldsInput - numberOfShields) * 100) / numberOfShields) + 100       
    hyperdriveTierOutput = float(((hyperdriveTierInput - HyperdriveTier) * 100) / HyperdriveTier) + 100
    blockCountOutput = float(((blockCountInput - blockCount) * 100) / blockCount) + 100
    optimalBlockCountOutput = float(((blockCountInput - optimalBlockCount) * 100) / optimalBlockCount) + 100



    print("Shield regeneration effectiveness:" + str(shieldRegenOutput) + "%")
    print("Shield reinforcement effectiveness:" + str(shieldReinforcementOutput) + "%")
    print("Cruise speed effectiveness:" + str(cruiseSpeedOutput) + "%")
    print("Cruise acceleration effectiveness:" + str(cruiseAccelerationOutput) + "%")
    print("Weapon effectiveness:" + str(numberOfPlasmasOutput) + "%")
    print("Shield count effectiveness: " + str(numberOfShieldsOutput) + "%")
    print("Hyperdrive tier effectiveness: " + str(hyperdriveTierOutput) + "%")
    print("Block count (size) effectiveness: " + str(blockCountOutput) + "%")
    print("You are this close to the optimal block count: " + str(optimalBlockCountOutput) + "%")

    totalVariables = 9

    totalEffectiveness = (int(shieldRegenOutput) + int(shieldReinforcementOutput) + int(cruiseSpeedOutput) + int(cruiseAccelerationOutput) + int(numberOfPlasmasOutput) 
        + int(numberOfShieldsOutput) + int(hyperdriveTierOutput) + int(blockCountOutput) + int(optimalBlockCountOutput) ) / totalVariables

    print("-----------------------------------------------------")
    print("And, with that, I have calculated that the general effectiveness of your ship is: ")
    print(str(totalEffectiveness) + "%")
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------Cruiser------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Cruiser():

    print("Cruisers are classified as medium-sized warships, and they are more than capable in combat.")
    print("Some models are even good for orbital bombardment.")
    print("Size: 8000-12000")
    print("Power output: 80000")
    print("The current meta stats of this class are as follows:")

    shieldRegen = 9.25013 #Input Meta ship info here
    shieldReinforcement = 9.25013 #Input Meta ship info here
    cruiseSpeed = 27 #Input Meta ship info here
    cruiseAcceleration = 5.15 #Input Meta ship info here
    numberOfPlasmas = 4 #Input Meta ship info here
    numberOfShields = 12 #Input Meta ship info here
    HyperdriveTier = 3 #Input Meta ship info here
    blockCount = 12000 #Input Meta ship info here
    optimalBlockCount = blockCount**1.1 #Smaller ships tend to be better off close to full block count, larger ones are better at half count or 3/4.

    print("Shield regen: " + str(shieldRegen))
    print("Shield reinforcement: " + str(shieldReinforcement)) #Displays meta info
    print("Cruise speed: " + str(cruiseSpeed))
    print("Cruise acceleration: " + str(cruiseAcceleration))
    print("Number of plasmas: " + str(numberOfPlasmas))
    print("Number of shields: " + str(numberOfShields))
    print("Hyperdrive tier: " + str(HyperdriveTier))
    print("Block count: " + str(blockCount))
    print("Optimal block count (equation determined): " + str(optimalBlockCount))
    print("-----------------------------------------------------")
    print("Keep in mind, effectiveness is measured from 0-100%,")
    print("If something is larger than 100%, then it's better than the meta.")
    print("-----------------------------------------------------")


    shieldRegenInput = float(raw_input("Enter your ship's shield regen divisor."))
    shieldReinforcementInput = float(raw_input("Enter your ship's shield reinforcement divisor.")) #Asks to input user's ship info
    cruiseSpeedInput = float(raw_input("Enter your ship's cruise speed."))
    cruiseAccelerationInput = float(raw_input("Enter your ship's acceleration."))
    numberOfPlasmasInput = float(raw_input("Enter your ship's plasma count."))
    numberOfShieldsInput = float(raw_input("Enter your ship's shield count."))
    hyperdriveTierInput = float(raw_input("Enter your ship's hyperdrive tier."))
    blockCountInput = float(raw_input("Enter your ship's block count."))
    
    shieldRegenOutput = float(((shieldRegenInput - shieldRegen) * 100) / shieldRegen) + 100
    shieldReinforcementOutput = float(((shieldReinforcementInput - shieldReinforcement) * 100) / shieldReinforcement) + 100       
    cruiseSpeedOutput = float(((cruiseSpeedInput - cruiseSpeed) * 100) / cruiseSpeed) + 100        
    cruiseAccelerationOutput = float(((cruiseAccelerationInput - cruiseAcceleration) * 100) / cruiseAcceleration) + 100        
    numberOfPlasmasOutput = float(((numberOfPlasmasInput - numberOfPlasmas) * 100) / numberOfPlasmas) + 100       
    numberOfShieldsOutput = float(((numberOfShieldsInput - numberOfShields) * 100) / numberOfShields) + 100       
    hyperdriveTierOutput = float(((hyperdriveTierInput - HyperdriveTier) * 100) / HyperdriveTier) + 100
    blockCountOutput = float(((blockCountInput - blockCount) * 100) / blockCount) + 100
    optimalBlockCountOutput = float(((blockCountInput - optimalBlockCount) * 100) / optimalBlockCount) + 100



    print("Shield regeneration effectiveness:" + str(shieldRegenOutput) + "%")
    print("Shield reinforcement effectiveness:" + str(shieldReinforcementOutput) + "%")
    print("Cruise speed effectiveness:" + str(cruiseSpeedOutput) + "%")
    print("Cruise acceleration effectiveness:" + str(cruiseAccelerationOutput) + "%")
    print("Weapon effectiveness:" + str(numberOfPlasmasOutput) + "%")
    print("Shield count effectiveness: " + str(numberOfShieldsOutput) + "%")
    print("Hyperdrive tier effectiveness: " + str(hyperdriveTierOutput) + "%")
    print("Block count (size) effectiveness: " + str(blockCountOutput) + "%")
    print("You are this close to the optimal block count: " + str(optimalBlockCountOutput) + "%")

    totalVariables = 9

    totalEffectiveness = (int(shieldRegenOutput) + int(shieldReinforcementOutput) + int(cruiseSpeedOutput) + int(cruiseAccelerationOutput) + int(numberOfPlasmasOutput) 
        + int(numberOfShieldsOutput) + int(hyperdriveTierOutput) + int(blockCountOutput) + int(optimalBlockCountOutput) ) / totalVariables

    print("-----------------------------------------------------")
    print("And, with that, I have calculated that the general effectiveness of your ship is: ")
    print(str(totalEffectiveness) + "%")
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------Battlecruiser------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Battlecruiser():

    print("Battlecruisers are large warships with an even larger power output. They can easily take on multiple smaller ships.")
    print("Battlecruisers are also good as support vessels.")
    print("Size: 12000-20000")
    print("Power output: 100000")
    print("The current meta stats of this class are as follows:")

    shieldRegen = 10 #Input Meta ship info here
    shieldReinforcement = 10 #Input Meta ship info here
    cruiseSpeed = 10 #Input Meta ship info here
    cruiseAcceleration = 10 #Input Meta ship info here
    numberOfPlasmas = 10 #Input Meta ship info here
    numberOfShields = 10 #Input Meta ship info here
    HyperdriveTier = 10 #Input Meta ship info here
    blockCount = 10 #Input Meta ship info here
    optimalBlockCount = blockCount**1.1 #Smaller ships tend to be better off close to full block count, larger ones are better at half count or 3/4.

    print("Shield regen: " + str(shieldRegen))
    print("Shield reinforcement: " + str(shieldReinforcement)) #Displays meta info
    print("Cruise speed: " + str(cruiseSpeed))
    print("Cruise acceleration: " + str(cruiseAcceleration))
    print("Number of plasmas: " + str(numberOfPlasmas))
    print("Number of shields: " + str(numberOfShields))
    print("Hyperdrive tier: " + str(HyperdriveTier))
    print("Block count: " + str(blockCount))
    print("Optimal block count (equation determined): " + str(optimalBlockCount))
    print("-----------------------------------------------------")
    print("Keep in mind, effectiveness is measured from 0-100%,")
    print("If something is larger than 100%, then it's better than the meta.")
    print("-----------------------------------------------------")


    shieldRegenInput = float(raw_input("Enter your ship's shield regen divisor."))
    shieldReinforcementInput = float(raw_input("Enter your ship's shield reinforcement divisor.")) #Asks to input user's ship info
    cruiseSpeedInput = float(raw_input("Enter your ship's cruise speed."))
    cruiseAccelerationInput = float(raw_input("Enter your ship's acceleration."))
    numberOfPlasmasInput = float(raw_input("Enter your ship's plasma count."))
    numberOfShieldsInput = float(raw_input("Enter your ship's shield count."))
    hyperdriveTierInput = float(raw_input("Enter your ship's hyperdrive tier."))
    blockCountInput = float(raw_input("Enter your ship's block count."))
    
    shieldRegenOutput = float(((shieldRegenInput - shieldRegen) * 100) / shieldRegen) + 100
    shieldReinforcementOutput = float(((shieldReinforcementInput - shieldReinforcement) * 100) / shieldReinforcement) + 100       
    cruiseSpeedOutput = float(((cruiseSpeedInput - cruiseSpeed) * 100) / cruiseSpeed) + 100        
    cruiseAccelerationOutput = float(((cruiseAccelerationInput - cruiseAcceleration) * 100) / cruiseAcceleration) + 100        
    numberOfPlasmasOutput = float(((numberOfPlasmasInput - numberOfPlasmas) * 100) / numberOfPlasmas) + 100       
    numberOfShieldsOutput = float(((numberOfShieldsInput - numberOfShields) * 100) / numberOfShields) + 100       
    hyperdriveTierOutput = float(((hyperdriveTierInput - HyperdriveTier) * 100) / HyperdriveTier) + 100
    blockCountOutput = float(((blockCountInput - blockCount) * 100) / blockCount) + 100
    optimalBlockCountOutput = float(((blockCountInput - optimalBlockCount) * 100) / optimalBlockCount) + 100



    print("Shield regeneration effectiveness:" + str(shieldRegenOutput) + "%")
    print("Shield reinforcement effectiveness:" + str(shieldReinforcementOutput) + "%")
    print("Cruise speed effectiveness:" + str(cruiseSpeedOutput) + "%")
    print("Cruise acceleration effectiveness:" + str(cruiseAccelerationOutput) + "%")
    print("Weapon effectiveness:" + str(numberOfPlasmasOutput) + "%")
    print("Shield count effectiveness: " + str(numberOfShieldsOutput) + "%")
    print("Hyperdrive tier effectiveness: " + str(hyperdriveTierOutput) + "%")
    print("Block count (size) effectiveness: " + str(blockCountOutput) + "%")
    print("You are this close to the optimal block count: " + str(optimalBlockCountOutput) + "%")

    totalVariables = 9

    totalEffectiveness = (int(shieldRegenOutput) + int(shieldReinforcementOutput) + int(cruiseSpeedOutput) + int(cruiseAccelerationOutput) + int(numberOfPlasmasOutput) 
        + int(numberOfShieldsOutput) + int(hyperdriveTierOutput) + int(blockCountOutput) + int(optimalBlockCountOutput) ) / totalVariables

    print("-----------------------------------------------------")
    print("And, with that, I have calculated that the general effectiveness of your ship is: ")
    print(str(totalEffectiveness) + "%")
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------Star Destroyer------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def StarDestroyer():

    print("Star Destroyers are the warships of rich people. They're massive, and they can wipe the floor with an entire fleet, ")
    print("especially when tagteaming with other ship classes.")
    print("Size: 20000-32000")
    print("Power output: 125000")
    print("The current meta stats of this class are as follows:")

    shieldRegen = 10 #Input Meta ship info here
    shieldReinforcement = 10 #Input Meta ship info here
    cruiseSpeed = 10 #Input Meta ship info here
    cruiseAcceleration = 10 #Input Meta ship info here
    numberOfPlasmas = 10 #Input Meta ship info here
    numberOfShields = 10 #Input Meta ship info here
    HyperdriveTier = 10 #Input Meta ship info here
    blockCount = 10 #Input Meta ship info here
    optimalBlockCount = blockCount**1.1 #Smaller ships tend to be better off close to full block count, larger ones are better at half count or 3/4.

    print("Shield regen: " + str(shieldRegen))
    print("Shield reinforcement: " + str(shieldReinforcement)) #Displays meta info
    print("Cruise speed: " + str(cruiseSpeed))
    print("Cruise acceleration: " + str(cruiseAcceleration))
    print("Number of plasmas: " + str(numberOfPlasmas))
    print("Number of shields: " + str(numberOfShields))
    print("Hyperdrive tier: " + str(HyperdriveTier))
    print("Block count: " + str(blockCount))
    print("Optimal block count (equation determined): " + str(optimalBlockCount))
    print("-----------------------------------------------------")
    print("Keep in mind, effectiveness is measured from 0-100%,")
    print("If something is larger than 100%, then it's better than the meta.")
    print("-----------------------------------------------------")


    shieldRegenInput = float(raw_input("Enter your ship's shield regen divisor."))
    shieldReinforcementInput = float(raw_input("Enter your ship's shield reinforcement divisor.")) #Asks to input user's ship info
    cruiseSpeedInput = float(raw_input("Enter your ship's cruise speed."))
    cruiseAccelerationInput = float(raw_input("Enter your ship's acceleration."))
    numberOfPlasmasInput = float(raw_input("Enter your ship's plasma count."))
    numberOfShieldsInput = float(raw_input("Enter your ship's shield count."))
    hyperdriveTierInput = float(raw_input("Enter your ship's hyperdrive tier."))
    blockCountInput = float(raw_input("Enter your ship's block count."))
    
    shieldRegenOutput = float(((shieldRegenInput - shieldRegen) * 100) / shieldRegen) + 100
    shieldReinforcementOutput = float(((shieldReinforcementInput - shieldReinforcement) * 100) / shieldReinforcement) + 100       
    cruiseSpeedOutput = float(((cruiseSpeedInput - cruiseSpeed) * 100) / cruiseSpeed) + 100        
    cruiseAccelerationOutput = float(((cruiseAccelerationInput - cruiseAcceleration) * 100) / cruiseAcceleration) + 100        
    numberOfPlasmasOutput = float(((numberOfPlasmasInput - numberOfPlasmas) * 100) / numberOfPlasmas) + 100       
    numberOfShieldsOutput = float(((numberOfShieldsInput - numberOfShields) * 100) / numberOfShields) + 100       
    hyperdriveTierOutput = float(((hyperdriveTierInput - HyperdriveTier) * 100) / HyperdriveTier) + 100
    blockCountOutput = float(((blockCountInput - blockCount) * 100) / blockCount) + 100
    optimalBlockCountOutput = float(((blockCountInput - optimalBlockCount) * 100) / optimalBlockCount) + 100



    print("Shield regeneration effectiveness:" + str(shieldRegenOutput) + "%")
    print("Shield reinforcement effectiveness:" + str(shieldReinforcementOutput) + "%")
    print("Cruise speed effectiveness:" + str(cruiseSpeedOutput) + "%")
    print("Cruise acceleration effectiveness:" + str(cruiseAccelerationOutput) + "%")
    print("Weapon effectiveness:" + str(numberOfPlasmasOutput) + "%")
    print("Shield count effectiveness: " + str(numberOfShieldsOutput) + "%")
    print("Hyperdrive tier effectiveness: " + str(hyperdriveTierOutput) + "%")
    print("Block count (size) effectiveness: " + str(blockCountOutput) + "%")
    print("You are this close to the optimal block count: " + str(optimalBlockCountOutput) + "%")

    totalVariables = 9

    totalEffectiveness = (int(shieldRegenOutput) + int(shieldReinforcementOutput) + int(cruiseSpeedOutput) + int(cruiseAccelerationOutput) + int(numberOfPlasmasOutput) 
        + int(numberOfShieldsOutput) + int(hyperdriveTierOutput) + int(blockCountOutput) + int(optimalBlockCountOutput) ) / totalVariables

    print("-----------------------------------------------------")
    print("And, with that, I have calculated that the general effectiveness of your ship is: ")
    print(str(totalEffectiveness) + "%")
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------Dreadnought------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Dreadnought():

    print("Do I even need to say it? These things are massive. Only a few players can even pilot these behemoths.")
    print("Dreadnoughts are best used for station defending and support in a large fleet.")
    print("Size: 32000-48000")
    print("Power output: 150000")
    print("The current meta stats of this class are as follows:")

    shieldRegen = 10 #Input Meta ship info here
    shieldReinforcement = 10 #Input Meta ship info here
    cruiseSpeed = 10 #Input Meta ship info here
    cruiseAcceleration = 10 #Input Meta ship info here
    numberOfPlasmas = 10 #Input Meta ship info here
    numberOfShields = 10 #Input Meta ship info here
    HyperdriveTier = 10 #Input Meta ship info here
    blockCount = 10 #Input Meta ship info here
    optimalBlockCount = blockCount**1.1 #Smaller ships tend to be better off close to full block count, larger ones are better at half count or 3/4.

    print("Shield regen: " + str(shieldRegen))
    print("Shield reinforcement: " + str(shieldReinforcement)) #Displays meta info
    print("Cruise speed: " + str(cruiseSpeed))
    print("Cruise acceleration: " + str(cruiseAcceleration))
    print("Number of plasmas: " + str(numberOfPlasmas))
    print("Number of shields: " + str(numberOfShields))
    print("Hyperdrive tier: " + str(HyperdriveTier))
    print("Block count: " + str(blockCount))
    print("Optimal block count (equation determined): " + str(optimalBlockCount))
    print("-----------------------------------------------------")
    print("Keep in mind, effectiveness is measured from 0-100%,")
    print("If something is larger than 100%, then it's better than the meta.")
    print("-----------------------------------------------------")


    shieldRegenInput = float(raw_input("Enter your ship's shield regen divisor."))
    shieldReinforcementInput = float(raw_input("Enter your ship's shield reinforcement divisor.")) #Asks to input user's ship info
    cruiseSpeedInput = float(raw_input("Enter your ship's cruise speed."))
    cruiseAccelerationInput = float(raw_input("Enter your ship's acceleration."))
    numberOfPlasmasInput = float(raw_input("Enter your ship's plasma count."))
    numberOfShieldsInput = float(raw_input("Enter your ship's shield count."))
    hyperdriveTierInput = float(raw_input("Enter your ship's hyperdrive tier."))
    blockCountInput = float(raw_input("Enter your ship's block count."))
    
    shieldRegenOutput = float(((shieldRegenInput - shieldRegen) * 100) / shieldRegen) + 100
    shieldReinforcementOutput = float(((shieldReinforcementInput - shieldReinforcement) * 100) / shieldReinforcement) + 100       
    cruiseSpeedOutput = float(((cruiseSpeedInput - cruiseSpeed) * 100) / cruiseSpeed) + 100        
    cruiseAccelerationOutput = float(((cruiseAccelerationInput - cruiseAcceleration) * 100) / cruiseAcceleration) + 100        
    numberOfPlasmasOutput = float(((numberOfPlasmasInput - numberOfPlasmas) * 100) / numberOfPlasmas) + 100       
    numberOfShieldsOutput = float(((numberOfShieldsInput - numberOfShields) * 100) / numberOfShields) + 100       
    hyperdriveTierOutput = float(((hyperdriveTierInput - HyperdriveTier) * 100) / HyperdriveTier) + 100
    blockCountOutput = float(((blockCountInput - blockCount) * 100) / blockCount) + 100
    optimalBlockCountOutput = float(((blockCountInput - optimalBlockCount) * 100) / optimalBlockCount) + 100



    print("Shield regeneration effectiveness:" + str(shieldRegenOutput) + "%")
    print("Shield reinforcement effectiveness:" + str(shieldReinforcementOutput) + "%")
    print("Cruise speed effectiveness:" + str(cruiseSpeedOutput) + "%")
    print("Cruise acceleration effectiveness:" + str(cruiseAccelerationOutput) + "%")
    print("Weapon effectiveness:" + str(numberOfPlasmasOutput) + "%")
    print("Shield count effectiveness: " + str(numberOfShieldsOutput) + "%")
    print("Hyperdrive tier effectiveness: " + str(hyperdriveTierOutput) + "%")
    print("Block count (size) effectiveness: " + str(blockCountOutput) + "%")
    print("You are this close to the optimal block count: " + str(optimalBlockCountOutput) + "%")

    totalVariables = 9

    totalEffectiveness = (int(shieldRegenOutput) + int(shieldReinforcementOutput) + int(cruiseSpeedOutput) + int(cruiseAccelerationOutput) + int(numberOfPlasmasOutput) 
        + int(numberOfShieldsOutput) + int(hyperdriveTierOutput) + int(blockCountOutput) + int(optimalBlockCountOutput) ) / totalVariables

    print("-----------------------------------------------------")
    print("And, with that, I have calculated that the general effectiveness of your ship is: ")
    print(str(totalEffectiveness) + "%")
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------CALIBRATION------------------------------------------------------------------------------------------
def CALIBRATION():

    ionthrusters = float(raw_input("Enter number of ion thrusters."))
    plasmathrusters = float(raw_input("Enter number of plasma thrusters."))
    glowstonethrusters = float(raw_input("Enter number of glowstone thrusters."))
    shipclass = raw_input("Enter starship class. (Battlecruiser, Star Destroyer, etc.")
    m = float(raw_input("Input ship mass."))

    ionTotal = int(ionthrusters) * 2.75
    plasmaTotal = int(plasmathrusters) * 2.0
    glowstoneTotal = int(glowstonethrusters) * 1.75
    x = int(ionTotal) + int(plasmaTotal) + int(glowstoneTotal)

    if shipclass == "Starfighter":
        p = 25000
    elif shipclass == "Corvette":
        p = 35000
    elif shipclass == "Frigate":
        p = 50000
    elif shipclass == "Destroyer":
        p = 60000
    elif shipclass == "Cruiser":
        p = 80000
    elif shipclass == "Battlecruiser":
        p = 100000                                  #FIX SPEED BEING 0 UPON PRINTING
    elif shipclass == "Star Destroyer":
        p = 125000
    elif shipclass == "Dreadnought":
        p = 150000

    F = 200

    bps = int(0)

    speed = (x^0.4) / ((m^0.3) * F)

    maxspeed = p / x

    if speed < maxspeed:
        bps = (speed * 80) / 100
    elif maxspeed < speed:
        bps = (maxspeed * 80) / 100

    print("And with that, the speed of your ship is: " + str(speed))
    print("And the maximum speed is: " + str(maxspeed))
    print("With this in mind, the actual Blocks Per Second of your ship is as follows: " + str(bps))


#--------------------------------------------------------------------------------------------------------------------------

#-------------Crate Calculator---------------------------------------------------------------------------------------------
def CrateCalc():
    x = float(raw_input("Input ship block count."))
    crates = float((4.5 * x) / 100)
    print(crates)

#--------------------------------------------------------------------------------------------------------------------------    



if shipClass == "Starfighter":
    Starfighter()
elif shipClass == "Corvette":
    Corvette()
elif shipClass == "Frigate":
    Frigate()
elif shipClass == "Destroyer":
    Destroyer()
elif shipClass == "Cruiser":
    Cruiser()
elif shipClass == "Battlecruiser":
    Battlecruiser()
elif shipClass == "Star Destroyer":
    StarDestroyer()
elif shipClass == "Dreadnought":
    Dreadnought()
elif shipClass == "CALIBRATION":
    CALIBRATION()
elif shipClass == "CrateCalc":
    CrateCalc()


               
#(power^1.4 / max(1,max(cbrt(distance), 1)) * 4000)

