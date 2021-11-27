
all_colors = set()

with open('colors.txt') as favorite_colors_file:
    for  line in favorite_colors_file:
         all_colors.add(line.strip())
print('Amber wases of Grain ' in all_colors)