# 70. Calculate cost of tiling a floor (area × tile price).
length = float(input("Enter the lenght of floor : "))
width = float(input("Enter the width of floor : "))
area = length * width                    

tile_price = float(input("Enter the tile price : "))
cost = area * tile_price                  

print(f"Total area of floor : {area:.2f} sq.units")
print(f"Tile Price : ₹{tile_price:.2f} per sq.unit")
print(f"Total cost for tiling floor : ₹{cost:.2f}")
