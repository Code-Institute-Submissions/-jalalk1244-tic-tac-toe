

class ComputerPlayer:
    def computer_move():
        '''
        Returns a random computer move from the available squares 
        '''
        try:
            pc = random.choice(available_squares)
            available_squares.remove(pc)
            return pc
        except IndexError:
            print()


class UserPlayer:
    pass