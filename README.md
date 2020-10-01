# Facebook-profile-scraper

# Ants vs. SomeBees

 A tower defense game called Ants Vs. SomeBees that resembles Plants vs Zombies. CS61a project

### Files

* ants.py: The game logic of Ants Vs. SomeBees
* ants_gui.py: The original GUI for Ants Vs. SomeBees
* graphics.py: Utilities for displaying simple two-dimensional animations
* utils.py: Some functions to facilitate the game interface
* ucb.py: Utility functions for CS 61A
* assets: A directory of images and files used by gui.py
* folder: A directory of images used by ants_gui.py


### Installing

Install the given files. The 'folder' folder has the image files for the game. Once the files are downloaded, run line below in terminal to start the game.

```
python3 ants_gui.py
```


## Rules

* The Colony: This is where the game takes place. The colony consists of several places that are chained together to form a tunnel where bees can travel through. The colony has some quantity of food that can be expended to deploy ant troops.

* Places: A place links to another place to form a tunnel. The player can place a single ant into each place. However, there can be many bees in a single place.

* The Hive: This is the place where bees originate. Bees exit the beehive to enter the ant colony.

* Ants: Ants are the usable troops in the game that the player places into the colony. Each type of ant takes a different action and requires a different amount of food to place. The two most basic ant types are the HarvesterAnt, which adds one food to the colony during each turn, and the ThrowerAnt, which throws a leaf at a bee each turn. You will be implementing many more.
```
 * HarvesterAnt: Food Cost - 2, Armor - 1
 * ThrowerAnt: Food Cost - 3, Armor - 1
 * ShortThrower: Food Cost - 2, Armor - 1
 * LongThrower: Food Cost - 2, Armor - 1
 * FireAnt: Food Cost - 5, Armor - 3
 * HungryAnt: Food Cost - 4, Armor - 1
 * NinjaAnt: Food Cost - 5, Armor - 1
 * WallAnt: Food Cost - 4, Armor - 4
 * BodyguardAnt: Food Cost - 4, Armor - 2
 * TankAnt: Food Cost - 6, Armor - 2
 * ScubaThrower: Food Cost - 6, Armor - 1
 * QueenAnt: Food Cost - 7, Armor - 1
 * SlowThrower: Food Cost - 4, Armor - 1
 * ScaryThrower: Food Cost - 6, Armor - 1
```
 
* Bees: Bees are the antagonistic troops in the game that the player must defend the colony from. Each turn, a bee either advances to the next place in the tunnel if no ant is in its way, or it stings the ant in its way. Bees win when at least one bee reaches the end of a tunnel.


## Acknowledgments

This was a given CS61a project with some skeleton code. 
