import TicTacToe
import Player

human1_test = Player.Human("x") # Player -> File; Human -> Class
ais_test = Player.AI("o")
#human2_test = Player.Human("o")
object1 = TicTacToe.TicTacToe(human1_test, ais_test) # 1st TTT -> FileName; 2nd TTT -> Class name

#object1.reset_game()
#object1.print_score()

object1.print_state()
object1.game_loop()


