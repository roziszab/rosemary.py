from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Butter, Egg, Salt, Flour, BakingPowder, Sugar, ChocolateChips

# Preheat oven and get a bowl
oven = Oven.use()
oven.preheat(degrees = 175)
bowl = Bowl.use(name = "batter")

# Make batter by adding butter, suggar in bathes, eggs seperately, salt, flour in batches, chocolate chips and baking powder into bowl
bowl.add(Butter("A part"))
for i in range(20):
    bowl.add(Sugar.take(grams = 10))
    bowl.mix()
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
    bowl.mix()
bowl.add(Salt.take("a pinch"))
for i in range(4):
    bowl.add(Flour.take(grams = 75))
    bowl.mix()
bowl.add(ChocolateChips.take(grams=200))
bowl.add(BakingPowder.take("some"))

# Rosemary tastes the batter
Rosemary.taste(bowl)

# Get a tray and add batter by scoops
tray = BakingTray.use()
for i in range(16):
    tray.add(bowl.take("1/16"))

# Put the bakingtray in the oven and bake for 10 minutes
oven.add(tray)
oven.bake(minutes = 10)

# Place baked cookies on plate and serve
plate = Plate.use()
plate.add(tray.take())
Rosemary.serve(plate)