from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Butter, Egg, Salt, Flour, BakingPowder, Sugar, ChocolateChips

# Define number of cookies (multiples of 8 give the most accurate measurements)
cookies = 8

# Preheat oven and get a bowl
oven = Oven.use()
oven.preheat(degrees = 175)
bowl = Bowl.use(name = "batter")

# Make batter by adding butter, suggar in bathes, eggs seperately, salt, flour in batches, chocolate chips and baking powder into bowl
bowl.add(Butter("A part"))
for i in range(int((cookies/8)*10)):
    bowl.add(Sugar.take(grams = 10))
    bowl.mix()
for egg in Egg.take(int(cookies/8)):
    egg.crack()
    bowl.add(egg)
    bowl.mix()
bowl.add(Salt.take("a pinch"))
for i in range(int(cookies/4)):
    bowl.add(Flour.take(grams = 75))
    bowl.mix()
bowl.add(ChocolateChips.take(grams=int(cookies/8)*100))
bowl.add(BakingPowder.take("some"))

# Rosemary tastes the batter
Rosemary.taste(bowl)

# Get a tray and add batter by scoops
tray = BakingTray.use()
for i in range(cookies):
    tray.add(bowl.take(str(1/cookies)))

# Put the bakingtray in the oven and bake for 10 minutes
oven.add(tray)
oven.bake(minutes = 10)

# Place baked cookies on plate and serve
plate = Plate.use()
plate.add(tray.take())
Rosemary.serve(plate)