import TicTacToe
import Player

human1_test = Player.Human("x") # Player -> File; Human -> Class
human2_test = Player.Human("o")
object1 = TicTacToe.TicTacToe( human1_test, human2_test) # 1st TTT -> FileName; 2nd TTT -> Class name

#object1.reset_game()
#object1.print_score()

object1.print_state()
object1.game_loop()


