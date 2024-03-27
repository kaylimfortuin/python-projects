x=int(input("How many eggs would you like to order?: "))

doz=x/12
los=x%12
tot=doz*3.25 or los*0.45

print("You have orderd:", x, "eggs that's", int(doz), "dozen at R3.25 per dozen and:", int(los), "loose eggs at 45c each for a total of R", round(tot,2))