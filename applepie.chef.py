from kitchen import Rosemary
from kitchen.utensils import Plate, Fridge, Oven, Bowl, PieDish
from kitchen.ingredients import Butter, Salt, Water, Flour, Apple, Sugar, Lemon, Cornstarch, Cinnamon, Egg

# Chilling water 
fridge = Fridge.use()
waterbowl = Bowl.use()
waterbowl.add(Water.take("Some"))
fridge.add(waterbowl)

# Preheat oven to 180 degrees
oven = Oven.use()
oven.preheat(degrees = 180)

# Get a bowl for the dough and mix it
dough = Bowl.use(name = "dough")
dough.add(Flour.take(grams = 300))
dough.add(Salt.take("a teaspoon"))
for i in range(5):
    dough.add(Butter.take(grams = 50))
    dough.add(waterbowl.take("1/5"))
    dough.mix()

# Taste the dough and chill in fridge
Rosemary.taste(dough)
fridge.add(dough)

# Mix filling
filling = Bowl.use(name = "filling")
for apple in Apple.take(6):
    apple.peel()
    apple.slice()
    filling.add(apple)
lemon = Lemon.take()
zest = lemon.zest()
juice = lemon.squeeze()
filling.add(Sugar.take(grams = 150))
filling.add(Cornstarch.take("a spoonful"))
filling.add(Salt.take("a pinch"))
filling.add(Cinnamon.take("a teaspoon"))
filling.add(zest.take("3/4"))
filling.add(juice.take("some"))
filling.mix()

# Rosemary tastes the filling
Rosemary.taste(filling)

# Assemble the pie
piedish = PieDish.use(name="apple pie")
piedish.add(dough.take("3/4"))
piedish.add(filling.take())
piedish.add(dough.take("1/4"))
glaze = Bowl.use(name = "glaze")
egg = Egg.take()
egg.crack()
glaze.add(egg)
glaze.mix()
piedish.add(egg)
piedish.add(Sugar.take("a spoon"))
piedish.add(zest.take("remainder"))

# Bake the pie
oven.add(piedish)
oven.bake(minutes=60)

# Serve the pie
plate = Plate.use()
plate.add(piedish.take())
Rosemary.serve(plate)