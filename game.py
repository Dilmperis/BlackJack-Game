import random
from player import Player

class BlackjackGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.dealer = Player("Dealer")
        self.cards = {'A': "11 or 1",
                      '2': 2,
                      '3': 3,
                      '4': 4,
                      '5': 5,
                      '6': 6,
                      '7': 7,
                      '8': 8,
                      '9': 9,
                      'J': 10,
                      'Q': 10,
                      'K': 10}

    def deal_card(self):
        random_card = random.choice(list(self.cards.keys()))
        return random_card

    def card_value_calculate(self, card, player):
        if card == 'A':
            card_value = int(input(f'The {player.name} got {card}. The Ace counts as 1 or 11? '))
            while card_value != 1 and card_value != 11:
                card_value = int(input('Wrong Input. Choose 1 or 11 as the value of Ace: '))
            index = player.cards.index('A')
            player.cards[index] = f'A as {card_value}'
        elif card == 'A as 1':
            card_value = 1
        elif card == 'A as 11':
            card_value = 11
        else:
            card_value = self.cards[card]

        return card_value

    def sum_value_of_cards(self, player):
        value = [self.card_value_calculate(card, player) for card in player.cards]
        return sum(value)

    def beginning_game(self):
        print('======== Beginning Dealing Round ========')
        for round in range(2):
            # Dealer's Card:
            dealer_card = self.deal_card()
            self.dealer.cards.append(dealer_card)
            print(f'Dealer gets {dealer_card}') if round == 0 else print('Dealer gets Hidden Card')

            # Player's Cards
            for player in self.players:
                card = self.deal_card()
                player.cards.append(card)
                print(f'{player.name} gets {card}')
            print(' ')

    def hitting_or_stopping(self):
        rounds = 0
        player_need_more_cards = [True for _ in range(self.num_players)]

        while True in player_need_more_cards:
            rounds += 1
            print(f'========================== Round {rounds} ==========================')
            for player_index, player in enumerate(self.players):
                if player_need_more_cards[player_index]:
                    holding_cards = player.cards
                    stop_or_continue = input(f'Does {player.name} with {holding_cards} want another card? Yes or No: ').title()
                    while stop_or_continue != 'Yes' and stop_or_continue != 'No':
                        stop_or_continue = input(f'Wrong input. Choose Yes or No: ').title()
                    stop_or_continue = True if stop_or_continue == 'Yes' else False

                    if stop_or_continue:
                        card = self.deal_card()
                        player.cards.append(card)
                        print(f'{player.name} gets {card}')

                        sum_value = self.sum_value_of_cards(player)
                        if sum_value > 21:
                            player_need_more_cards[player_index] = False
                            print(f'{player.name} lost with cards {holding_cards}. The total value of cards is {sum_value}, above 21.')
                        elif sum_value == 21:
                            player_need_more_cards[player_index] = False
                            print(f'{player.name} has BlackJack with cards {holding_cards}. The total value of cards is {sum_value}.')
                        else:
                            print(f'{player.name} has {holding_cards} with total value of cards {sum_value}.')
                    else:
                        player_need_more_cards[player_index] = stop_or_continue
                        sum_value = self.sum_value_of_cards(player)
                        if sum_value <= 21:
                            print(f'{player.name} has {holding_cards} with value {sum_value} and stops there.')
                        else:
                            print(f'{player.name} has {holding_cards} with value {sum_value} so {player.name} lost.')
                    print(' ')
            print(' ')

    def dealer_hit_or_stop(self):
        print("======================= Dealer's Turn =======================")
        print(f"The Dealer's Hidden Card is {self.dealer.cards[1]}")
        for player in self.players:
            sum_value = self.sum_value_of_cards(player)
            holding_cards = player.cards
            if sum_value <= 21:
                print(f'{player.name} still plays with holding cards {holding_cards} of value {sum_value}')
        print(' ')

        holding_cards = self.dealer.cards
        sum_value = self.sum_value_of_cards(self.dealer)

        stop_or_continue = True
        while stop_or_continue:
            stop_or_continue = input(f'Does the Dealer with {holding_cards} want another card? Yes or No: ').title()
            while stop_or_continue != 'Yes' and stop_or_continue != 'No':
                stop_or_continue = input(f'Wrong input. Choose Yes or No: ').title()
            stop_or_continue = True if stop_or_continue == 'Yes' else False

            if stop_or_continue:
                card = self.deal_card()
                self.dealer.cards.append(card)
                print(f'Dealer gets {card}')

                sum_value = self.sum_value_of_cards(self.dealer)

                if sum_value == 21:
                    print(f'Dealer has BlackJack with cards {holding_cards}. The total value of cards is {sum_value}.')
                    return sum_value
                elif sum_value > 21:
                    print(f'Dealer lost with cards {holding_cards}. The total value of cards is {sum_value}, above 21.')
                    return sum_value
                else:
                    print(f'Dealer has {holding_cards} with total value of cards {sum_value}.')
            else:
                if sum_value <= 21:
                    print(f'Dealer has {holding_cards} with value {sum_value} and stops there.')
                else:
                    print(f'Dealer has {holding_cards} with value {sum_value} so Dealer lost.')
                return sum_value
            print(' ')

    def play(self):
        self.beginning_game()
        self.hitting_or_stopping()
        dealer_value_of_cards = self.dealer_hit_or_stop()

        print('\n============================================================== RESULTS =============================================================')
        if dealer_value_of_cards == 21:
            print("Everybody Lost, the Dealer has blackjack!")
        elif dealer_value_of_cards > 21:
            print(f"The Dealer lost with {dealer_value_of_cards}!\n")
            for player in self.players:
                sum_value = self.sum_value_of_cards(player)
                if sum_value > 21:
                    print(f'{player.name} lost with {sum_value}.')
                else:
                    print(f'{player.name} won with {sum_value}.')
        else:
            print(f'The Dealer has {dealer_value_of_cards}\n')
            for player in self.players:
                sum_value = self.sum_value_of_cards(player)
                if sum_value > 21:
                    print(f'{player.name} lost with {sum_value}.')
                elif sum_value > dealer_value_of_cards:
                    print(f'{player.name} won with {sum_value}.')
                else:
                    print(f'{player.name} lost with {sum_value}.')
