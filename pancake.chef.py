from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt, Flour, Milk

# Take a bowl to mix the batter in
bowl = Bowl.use(name="batter")

# Add all the eggs to the bowl and mix
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.mix()
# Add a dash of salt
bowl.add(Salt.take("a dash"))
# Add in 250 grams of flour in batches of 50 grams
for i in range(5):
    bowl.add(Flour.take(grams = 50))
    bowl.mix()
# Add in 500 ml of milk in two batches
for i in range(2):
    bowl.add(Milk.take(ml = 250))
    bowl.mix()

# Rosmary tastes the batter
Rosemary.taste(bowl)

# Take a plate and a pan
plate = Plate.use ()
pancake_pan = Pan.use ("pancake")

# Make 8 pancakes and add them to the plate
for i in range(8):
    pancake_pan.add(Butter.take("a bit"))
    pancake_pan.add(bowl.take("1/8"))
    pancake_pan.cook(minutes=1)
    pancake_pan.flip()
    pancake_pan.cook(minutes=1)
    plate.add(pancake_pan.take())

# Serve pancakes
Rosemary.serve(plate)