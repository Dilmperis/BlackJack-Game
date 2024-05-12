from game import BlackjackGame


def main():
    print('Welcome to BlackJack by Giannis Dilmperis!\n')
    print('The game begins and Players are dealt one card face up in clockwise direction, starting from the dealer.')
    print('Then the dealer starts dealing one more round of cards the same way,')
    print('keeping only his card face down and all the others face up.\n')
    print('At the end everybody has 2 open cards, except from the Dealer who has one open card and one hidden.\n')

    number_players = int(input('\nHow many players are playing? '))
    game = BlackjackGame(number_players)
    game.play()


if __name__ == "__main__":
    main()
