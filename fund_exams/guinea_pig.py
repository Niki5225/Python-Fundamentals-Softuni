quantity_food_g = float(input()) * 1000
quantity_hay_g = float(input()) * 1000
quantity_cover_g = float(input()) * 1000
guinea_pig_g = float(input()) * 1000
run_out_of_food = False
for day in range(1, 30 + 1):
    quantity_food_g -= 300
    if day % 2 == 0:
        quantity_hay_g -= 0.05 * quantity_food_g
    if day % 3 == 0:
        quantity_cover_g -= 1 / 3 * guinea_pig_g
    if quantity_cover_g <= 0 or quantity_food_g <= 0 or quantity_hay_g <= 0:
        run_out_of_food = True
    if run_out_of_food:
        break
if run_out_of_food:
    print("Merry must go to the pet store!")
else:
    quantity_food_kg = quantity_food_g / 1000
    quantity_hay_kg = quantity_hay_g / 1000
    quantity_cover_kg = quantity_cover_g / 1000
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_kg:.2f}, Hay: {quantity_hay_kg:.2f}, "
          f"Cover: {quantity_cover_kg:.2f}.")
