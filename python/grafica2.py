import matplotlib.pyplot as plt
import pandas as pd

videogames = [
    ["Wii Sports","Wii",2006.0,"Sports","Nintendo",41.49,29.02,3.77,8.46,82.74],
    ["Super Mario Bros.","NES",1985.0,"Platform","Nintendo",29.08,3.58,6.81,0.77,40.24],
    ["Mario Kart Wii","Wii",2008.0,"Racing","Nintendo",15.85,12.88,3.79,3.31,35.82],
    ["Wii Sports Resort","Wii",2009.0,"Sports","Nintendo",15.75,11.01,3.28,2.96,33.0],
    ["Pokemon Red/Pokemon Blue","GB",1996.0,"Role-Playing","Nintendo",11.27,8.89,10.22,1.0,31.37],
    ["Tetris","GB",1989.0,"Puzzle","Nintendo",23.2,2.26,4.22,0.58,30.26],
    ["New Super Mario Bros.","DS",2006.0,"Platform","Nintendo",11.38,9.23,6.5,2.9,30.01],
    ["Wii Play","Wii",2006.0,"Misc","Nintendo",14.03,9.2,2.93,2.85,29.02],
    ["New Super Mario Bros. Wii","Wii",2009.0,"Platform","Nintendo",14.59,7.06,4.7,2.26,28.62],
    ["Duck Hunt","NES",1984.0,"Shooter","Nintendo",26.93,0.63,0.28,0.47,28.31],
    ["Nintendogs","DS",2005.0,"Simulation","Nintendo",9.07,11.0,1.93,2.75,24.76],
    ["Mario Kart DS","DS",2005.0,"Racing","Nintendo",9.81,7.57,4.13,1.92,23.42],
    ["Pokemon Gold/Pokemon Silver","GB",1999.0,"Role-Playing","Nintendo",9.0,6.18,7.2,0.71,23.1],
    ["Wii Fit","Wii",2007.0,"Sports","Nintendo",8.94,8.03,3.6,2.15,22.72],
    ["Wii Fit Plus","Wii",2009.0,"Sports","Nintendo",9.09,8.59,2.53,1.79,22.0],
    ["Kinect Adventures!","X360",2010.0,"Misc","Microsoft Game Studios",14.97,4.94,0.24,1.67,21.82],
    ["Grand Theft Auto V","PS3",2013.0,"Action","Take-Two Interactive",7.01,9.27,0.97,4.14,21.4],
    ["Grand Theft Auto: San Andreas","PS2",2004.0,"Action","Take-Two Interactive",9.43,0.4,0.41,10.57,20.81],
    ["Super Mario World","SNES",1990.0,"Platform","Nintendo",12.78,3.75,3.54,0.55,20.61],
    ["Brain Age: Train Your Brain in Minutes a Day","DS",2005.0,"Misc","Nintendo",4.75,9.26,4.16,2.05,20.22],
    ["Pokemon Diamond/Pokemon Pearl","DS",2006.0,"Role-Playing","Nintendo",6.42,4.52,6.04,1.37,18.36],
    ["Super Mario Land","GB",1989.0,"Platform","Nintendo",10.83,2.71,4.18,0.42,18.14],
    ["Super Mario Bros. 3","NES",1988.0,"Platform","Nintendo",9.54,3.44,3.84,0.46,17.28],
    ["Grand Theft Auto V","X360",2013.0,"Action","Take-Two Interactive",9.63,5.31,0.06,1.38,16.38],
    ["Grand Theft Auto: Vice City","PS2",2002.0,"Action","Take-Two Interactive",8.41,5.49,0.47,1.78,16.15],
    ["Pokemon Ruby/Pokemon Sapphire","GBA",2002.0,"Role-Playing","Nintendo",6.06,3.9,5.38,0.5,15.85],
    ["Pokemon Black/Pokemon White","DS",2010.0,"Role-Playing","Nintendo",5.57,3.28,5.65,0.82,15.32],
    ["Brain Age 2: More Training in Minutes a Day","DS",2005.0,"Puzzle","Nintendo",3.44,5.36,5.32,1.18,15.3],
    ["Gran Turismo 3: A-Spec","PS2",2001.0,"Racing","Sony Computer Entertainment",6.85,5.09,1.87,1.16,14.98],
    ["Call of Duty: Modern Warfare 3","X360",2011.0,"Shooter","Activision",9.03,4.28,0.13,1.32,14.76],
    ["Pokémon Yellow: Special Pikachu Edition","GB",1998.0,"Role-Playing","Nintendo",5.89,5.04,3.12,0.59,14.64],
    ["Call of Duty: Black Ops","X360",2010.0,"Shooter","Activision",9.67,3.73,0.11,1.13,14.64],
    ["Pokemon X/Pokemon Y","3DS",2013.0,"Role-Playing","Nintendo",5.17,4.05,4.34,0.79,14.35],
    ["Call of Duty: Black Ops 3","PS4",2015.0,"Shooter","Activision",5.77,5.81,0.35,2.31,14.24],
    ["Call of Duty: Black Ops II","PS3",2012.0,"Shooter","Activision",4.99,5.88,0.65,2.52,14.03],
    ["Call of Duty: Black Ops II","X360",2012.0,"Shooter","Activision",8.25,4.3,0.07,1.12,13.73],
    ["Call of Duty: Modern Warfare 2","X360",2009.0,"Shooter","Activision",8.52,3.63,0.08,1.29,13.51],
    ["Call of Duty: Modern Warfare 3","PS3",2011.0,"Shooter","Activision",5.54,5.82,0.49,1.62,13.46],
    ["Grand Theft Auto III","PS2",2001.0,"Action","Take-Two Interactive",6.99,4.51,0.3,1.3,13.1],
    ["Super Smash Bros. Brawl","Wii",2008.0,"Fighting","Nintendo",6.75,2.61,2.66,1.02,13.04],
    ["Call of Duty: Black Ops","PS3",2010.0,"Shooter","Activision",5.98,4.44,0.48,1.83,12.73],
    ["Animal Crossing: Wild World","DS",2005.0,"Simulation","Nintendo",2.55,3.52,5.33,0.88,12.27],
    ["Mario Kart 7","3DS",2011.0,"Racing","Nintendo",4.74,3.91,2.67,0.89,12.21],
    ["Halo 3","X360",2007.0,"Shooter","Microsoft Game Studios",7.97,2.83,0.13,1.21,12.14],
    ["Grand Theft Auto V","PS4",2014.0,"Action","Take-Two Interactive",3.8,5.81,0.36,2.02,11.98],
    ["Pokemon HeartGold/Pokemon SoulSilver","DS",2009.0,"Action","Nintendo",4.4,2.77,3.96,0.77,11.9],
    ["Super Mario 64","N64",1996.0,"Platform","Nintendo",6.91,2.85,1.91,0.23,11.89],
    ["Gran Turismo 4","PS2",2004.0,"Racing","Sony Computer Entertainment",3.01,0.01,1.1,7.53,11.66],
    ["Super Mario Galaxy","Wii",2007.0,"Platform","Nintendo",6.16,3.4,1.2,0.76,11.52],
    ["Pokemon Omega Ruby/Pokemon Alpha Sapphire","3DS",2014.0,"Role-Playing","Nintendo",4.23,3.37,3.08,0.65,11.33],
    ["Super Mario Land 2: 6 Golden Coins", "GB", 1992.0, "Adventure", "Nintendo", 6.16, 2.04, 2.69, 0.29, 11.18],
    ["Grand Theft Auto IV","X360",2008.0,"Action","Take-Two Interactive",6.76,3.1,0.14,1.03,11.02],
    ["Gran Turismo","PS",1997.0,"Racing","Sony Computer Entertainment",4.02,3.87,2.54,0.52,10.95],
    ["Super Mario 3D Land","3DS",2011.0,"Platform","Nintendo",4.89,2.99,2.13,0.78,10.79],
    ["Gran Turismo 5","PS3",2010.0,"Racing","Sony Computer Entertainment",2.96,4.88,0.81,2.12,10.77],
    ["Call of Duty: Modern Warfare 2","PS3",2009.0,"Shooter","Activision",4.99,3.69,0.38,1.63,10.69],
    ["Grand Theft Auto IV","PS3",2008.0,"Action","Take-Two Interactive",4.76,3.76,0.44,1.62,10.57],
    ["Super Mario All-Stars","SNES",1993.0,"Platform","Nintendo",5.99,2.15,2.12,0.29,10.55],
    ["Pokemon FireRed/Pokemon LeafGreen","GBA",2004.0,"Role-Playing","Nintendo",4.34,2.65,3.15,0.35,10.49],
    ["Super Mario 64","DS",2004.0,"Platform","Nintendo",5.08,3.11,1.25,0.98,10.42],
    ["Just Dance 3","Wii",2011.0,"Misc","Ubisoft",6.05,3.15,0.0,1.07,10.26],
    ["Call of Duty: Ghosts","X360",2013.0,"Shooter","Activision",6.72,2.63,0.04,0.82,10.21],
    ["Halo: Reach,X360",2010.0,"Shooter","Microsoft Game Studios",7.03,1.98,0.08,0.78,9.88],
    ["Mario Kart 64","N64",1996.0,"Racing","Nintendo",5.55,1.94,2.23,0.15,9.87],
    ["New Super Mario Bros. 2","3DS",2012.0,"Platform","Nintendo",3.66,3.07,2.47,0.63,9.82],
    ["Halo 4","X360",2012.0,"Shooter","Microsoft Game Studios",6.63,2.36,0.04,0.73,9.76],
    ["Final Fantasy VII","PS",1997.0,"Role-Playing","Sony Computer Entertainment",3.01,2.47,3.28,0.96,9.72],
    ["Call of Duty: Ghosts", "PS3", 2013.0, "Shooter", "Activision", 4.09, 3.73, 0.38, 1.38, 9.59],
    ["Just Dance 2", "Wii", 2010.0, "Misc", "Ubisoft", 5.84, 2.89, 0.01, 0.78, 9.52],
    ["Gran Turismo 2", "PS", 1999.0, "Racing", "Sony Computer Entertainment", 3.88, 3.42, 1.69, 0.5, 9.49],
    ["Call of Duty 4: Modern Warfare", "X360", 2007.0, "Shooter", "Activision", 5.91, 2.38, 0.13, 0.9, 9.32],
    ["Donkey Kong Country", "SNES", 1994.0, "Platform", "Nintendo", 4.36, 1.71, 3.0, 0.23, 9.3],
    ["Minecraft", "X360", 2013.0, "Misc", "Microsoft Game Studios", 5.58, 2.83, 0.02, 0.77, 9.2],
    ["Animal Crossing: New Leaf", "3DS", 2012.0, "Simulation", "Nintendo", 2.01, 2.32, 4.36, 0.41, 9.09],
    ["Mario Party DS", "DS", 2007.0, "Misc", "Nintendo", 4.46, 1.88, 1.98, 0.7, 9.02],
    ["The Elder Scrolls V: Skyrim", "X360", 2011.0, "Role-Playing", "Bethesda Softworks", 5.03, 2.86, 0.1, 0.85, 8.84],
    ["Super Mario Kart", "SNES", 1992.0, "Racing", "Nintendo", 3.54, 1.24, 3.81, 0.18, 8.76],
    ["FIFA 16", "PS4", 2015.0, "Sports", "Electronic Arts", 1.11, 6.06, 0.06, 1.26, 8.49],
    ["Wii Party", "Wii", 2010.0, "Misc", "Nintendo", 1.79, 3.53, 2.49, 0.68, 8.49],
    ["Halo 2", "XB", 2004.0, "Shooter", "Microsoft Game Studios", 6.82, 1.53, 0.05, 0.08, 8.49],
    ["Mario Party 8", "Wii", 2007.0, "Misc", "Nintendo", 3.81, 2.3, 1.58, 0.73, 8.42],
    ["Pokemon Black 2/Pokemon White 2", "DS", 2012.0, "Role-Playing", "Nintendo", 2.91, 1.86, 3.14, 0.43, 8.33],
    ["FIFA Soccer 13", "PS3", 2012.0, "Action", "Electronic Arts", 1.06, 5.05, 0.13, 2.01, 8.24],
    ["The Sims 3", "PC", 2009.0, "Simulation", "Electronic Arts", 0.98, 6.42, 0.0, 0.71, 8.11],
    ["GoldenEye 007", "N64", 1997.0, "Shooter", "Nintendo", 5.8, 2.01, 0.13, 0.15, 8.09],
    ["Mario & Sonic at the Olympic Games", "Wii", 2007.0, "Sports", "Sega", 2.58, 3.9, 0.66, 0.91, 8.06],
    ["Final Fantasy X", "PS2", 2001.0, "Role-Playing", "Sony Computer Entertainment", 2.91, 2.07, 2.73, 0.33, 8.05],
    ["Final Fantasy VIII", "PS", 1999.0, "Role-Playing", "SquareSoft", 2.28, 1.72, 3.63, 0.23, 7.86],
    ["Pokémon Platinum Version", "DS", 2008.0, "Role-Playing", "Nintendo", 2.82, 1.78, 2.69, 0.55, 7.84],
    ["Pac-Man", "2600", 1982.0, "Puzzle", "Atari", 7.28, 0.45, 0.0, 0.08, 7.81],
    ["Grand Theft Auto: Liberty City Stories", "PSP", 2005.0, "Action", "Take-Two Interactive", 2.9, 2.83, 0.24, 1.75, 7.72],
    ["Super Mario Galaxy 2", "Wii", 2010.0, "Platform", "Nintendo", 3.66, 2.42, 0.98, 0.64, 7.69],
    ["Star Wars Battlefront (2015)", "PS4", 2015.0, "Shooter", "Electronic Arts", 2.93, 3.29, 0.22, 1.23, 7.67],
    ["Call of Duty: Advanced Warfare", "PS4", 2014.0, "Shooter", "Activision", 2.8, 3.3, 0.14, 1.37, 7.63],
    ["The Legend of Zelda: Ocarina of Time", "N64", 1998.0, "Action", "Nintendo", 4.1, 1.89, 1.45, 0.16, 7.62],
    ["Crash Bandicoot 2: Cortex Strikes Back", "PS", 1997.0, "Platform", "Sony Computer Entertainment", 3.78, 2.17, 1.31, 0.31, 7.58],
    ["Super Mario Bros. 2","NES",1988.0,"Platform","Nintendo",5.39,1.18,0.7,0.19,7.46],
    ["Super Smash Bros. for Wii U and 3DS","3DS",2014.0,"Fighting","Nintendo",3.24,1.35,2.42,0.43,7.45],
    ["Call of Duty: World at War","X360",2008.0,"Shooter","Activision",4.79,1.9,0.0,0.69,7.37]
]

columns = ["Name","Platform","Year","Genre","Publisher","NA_Sales","EU_Sales","JP_Sales","Other_Sales","Global_Sales"]

df_videogames = pd.DataFrame(videogames, columns=columns)

ventas_NA = df_videogames['NA_Sales'].sum()
ventas_EU = df_videogames['EU_Sales'].sum()
ventas_JP = df_videogames['JP_Sales'].sum()
ventas_Otros = df_videogames['Other_Sales'].sum()

# Crea una lista con las ventas y las etiquetas de las regiones
ventas = [ventas_NA, ventas_EU, ventas_JP, ventas_Otros]
etiquetas = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

# Genera el gráfico circular
plt.pie(ventas, labels = etiquetas, autopct='%1.1f%%')

plt.axis('equal')  # Asegura que se dibuje un círculo
plt.show()  # Muestra el gráfico
