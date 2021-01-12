
from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt, Flour, Milk

# Define portions (multiples of 4 give the most accurate measurements, 1 portion is 2 pancakes)
portion = 8

# Take a bowl to mix the batter in
bowl = Bowl.use(name="batter")

# Add all the eggs to the bowl and mix
for egg in Egg.take(amount = int(portion/2)):
    egg.crack()
    bowl.add(egg)
bowl.mix()
# Add a dash of salt
bowl.add(Salt.take("a dash"))
# Add flour in batches of 50 grams
for i in range(int(portion*1.25)):
    bowl.add(Flour.take(grams = 50))
    bowl.mix()
# Add milk in two batches
for i in range(2):
    bowl.add(Milk.take(ml = int(portion*62.5)))
    bowl.mix()

# Rosmary tastes the batter
Rosemary.taste(bowl)

# Take a plate and a pan
plate = Plate.use ()
pancake_pan = Pan.use ("pancake")

# Make pancakes and add them to the plate
for i in range(int(portion*2)):
    pancake_pan.add(Butter.take("a bit"))
    pancake_pan.add(bowl.take(str(1/(portion*2))))
    pancake_pan.cook(minutes=1)
    pancake_pan.flip()
    pancake_pan.cook(minutes=1)
    plate.add(pancake_pan.take())

# Serve pancakes
Rosemary.serve(plate)