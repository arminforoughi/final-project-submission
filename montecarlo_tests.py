import unittest
from montecarlo import Die, Game, Analyzer

class test_die(unittest.TestCase):


    def test_die1(self):
        new = Die([1,2,3,4,5])
        new.change_the_weight(3, .4)
        self.assertEqual(float(new.show()[new.show().Faces == 3]['weights']), .4)
        #assertEqual(1,1)

    def test_die2(self):
        new = Die([1,2,3,4,5, 1,2,3,4,5])
        new.change_the_weight(3, .4)
        new.change_the_weight(5, .1)
        self.assertEqual(float(new.show()[new.show().Faces == 5]['weights']), .1)
        #assertEqual(1,1)

    def test_die3(self):
        coin_fair = Die(['H', 'T']) #fair coin
        coin_unfair1 = Die(['H', 'T']) #unfair coin
        coin_unfair1.change_the_weight('H', 5)
        self.assertEqual(float(coin_unfair1.show()[coin_unfair1.show().Faces == 'H']['weights']), 5)
        coin_unfair1.roll(5)
        self.assertEqual(len(coin_unfair1.df_die), 2)
        #assertEqual(1,1)
        #assertEqual(1,1)
    def test_die3(self):
        coin_fair = Die(['H', 'T']) #fair coin
        coin_fair.roll(5)
        self.assertEqual(len(coin_fair.roll(5)), 5)
        #assertEqual(1,1)
        #assertEqual(1,1)

class test_Game(unittest.TestCase):


    def test_game1(self):
        coin_fair = Die(['H', 'T']) #fair coin
        game1 = Game([coin_fair, coin_fair, coin_fair]) #creating a fair game variable
        self.assertEqual(len(game1.play(1000)),1000)

    def test_game2(self):
        coin_fair = Die(['H', 'T']) #fair coin
        game1 = Game([coin_fair, coin_fair, coin_fair]) #creating a fair game variable
        game1.play(1000) # playing the game 1000 times
        self.assertEqual(len(game1.show()),1000)

    def test_game3(self):
        coin_fair = Die(['H', 'T']) #fair coin
        coin_unfair1 = Die(['H', 'T']) #unfair coin
        coin_unfair1.change_the_weight('H', 5) # changing the weight
        game2 = Game([coin_unfair1, coin_unfair1, coin_fair])#creating a unfair game variable
        game2.play(1000)
        self.assertEqual(game2.show('narrow').shape,(3000, 1))
        #assertEqual(1,1)

class test_Analyzer(unittest.TestCase):

    def test_analyzer1(self):

        die_fair = Die([1,2,3,4,5,6])
        die_unfair1 = Die([1,2,3,4,5,6])
        die_unfair1.change_the_weight(6, 5)
        die_unfair2 = Die([1,2,3,4,5,6])
        die_unfair1.change_the_weight(1, 5)
        game2 = Game([die_unfair1, die_unfair1, die_unfair2, die_fair])
        play2 = game2.play(10000)

        analyzer2 = Analyzer(game2)

        analyzer2.combo()

        self.assertEqual(len(analyzer2.combo_df.index.names), 4)

    def test_analyzer2(self):

        die_fair = Die([1,2,3,4,5,6])

        game1 = Game([die_fair, die_fair, die_fair, die_fair, die_fair])
        play1 = game1.play(10000)

        analyzer1 = Analyzer(game1)

        analyzer1.face_counts_per_roll()
        self.assertEqual(analyzer1.df_face_counts_per_roll.shape, (10000, 6))

    def test_analyzer3(self):

        die_fair = Die([1,2,3,4,5,6])

        game1 = Game([die_fair, die_fair, die_fair, die_fair, die_fair])
        play1 = game1.play(10000)

        analyzer1 = Analyzer(game1)
        analyzer1.jackpot()

        self.assertEqual(len(analyzer1.unique_df.columns), 5)


if __name__ == '__main__':
    unittest.main()


    #with open('testing.txt', 'w') as f:
    #    unittest.main(f)
