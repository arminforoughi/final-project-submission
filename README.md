
# Metadata

* Title: **Final Project Report**
* Class: DS 5100
* Date: Dec 6, 2022
* Student Name: Armin Foroughi


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/).

```bash
pip install montecarlo
```

## importing library 

```python
#library
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from montecarlo import Die, Game, Analyzer
```
## Demo
Creating one fair coin (with faces H and T) and one unfair coin. 
The unfair coin has one face with a weight of 5 and the others 1.
```python
#library
coin_fair = Die(['H', 'T']) #fair coin
coin_unfair1 = Die(['H', 'T']) #unfair coin
coin_unfair1.change_the_weight('H', 5) # changing the weight

```
creating and playing game 
```python

game2 = Game([coin_unfair1, coin_unfair1, coin_fair])#creating a unfair game variable 
game2.play(1000)# playing the game 1000 times 
```
analyzing game 
```python
analyzer2 = Analyzer(game2)
print('game 2 with two unfair coins has {} out of 1000 jackpots'.format(analyzer2.jackpot()))
```
## API description
### class Die 
create class die 

#### change_the_weight
        
changes the weight of the given face.
        input:face, weight
        action:change in df_die

#### roll
takes roll_times and rolls the die roll_times 
returns 

#### show

return df_die

### class Game
A class that we can play games in 
 
input:Die_list: a list of dies 
takes a list of dies and initiates the game

#### play
input:roll_times 

takes roll_times and rolls all the dice roll_times times.


#### show

takes typa as arguement and returns private df as typa



### class Analyzer

Takes game as arguament an does some analysis on the game

takes game as argument and initilizes it also initializes the needed dataframes

#### face_counts_per_roll(self):
  
method to compute how many times a given face is rolled in each event.

#### jackpot(self):

a method to count how many times a roll resulted in all faces being the same

#### combo(self):

method to compute the distinct combinations of faces rolled, along with their counts

## License

[MIT](https://choosealicense.com/licenses/mit/)
