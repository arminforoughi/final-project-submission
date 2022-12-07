import pandas as pd
import numpy as np
import random

class Die():
    def __init__(self,faces):
        self.faces = np.unique(faces)
        self.df_die = pd.DataFrame({'Faces':self.faces, 'weights':[1 for i in range(len(self.faces))]})

    def change_the_weight(self, face, weight):
        try:
            float(weight)
        except:
            print('not numeric weight')
            return
        if face in self.df_die['Faces'].tolist():
            #self.df_die[face] = weight
            self.df_die['weights'][self.df_die.index[self.df_die['Faces'] == face]] = float(weight)

    def roll(self, roll_times = 1):
        return random.choices(self.df_die['Faces'], weights=self.df_die['weights'], k=roll_times)
    def show(self):
        return self.df_die
class Game():
    def __init__(self, Die_list):
        self.games = Die_list

    def play(self, roll_times):
        name = 1
        self.__df = pd.DataFrame({1:self.games[0].roll(roll_times)})
        for game in self.games[1:]:
            name += 1
            self.__df[name] = game.roll(roll_times)
        return self. __df
    def show(self,typa ='wide'):

        if typa == 'wide':
            return self. __df
        elif typa == 'narrow':
            return pd.DataFrame(self.__df.unstack(level=-1))
        else:
            raise ValueError("worng type")



class Analyzer():
    def __init__(self, game):

        self.game = game
        self.df_narrow = self.game.show('narrow')
        self.df_wide = self.game.show()
        self.df_face_counts_per_roll = None
        self.unique_df = None
        self.combo_df = None

    def face_counts_per_roll(self):
        self.df_face_counts_per_roll = self.df_wide.apply(pd.Series.value_counts,axis = 1).fillna(0)

    def jackpot(self):

        self.unique_df = self.df_wide[self.df_wide.nunique(1) == 1]
        return (self.df_wide.nunique(1) == 1).sum()

    def combo(self):

        self.combo_df = self.df_wide.value_counts()
