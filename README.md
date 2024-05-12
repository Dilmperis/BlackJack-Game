# BlackJack-Game

![image](https://github.com/Dilmperis/BlackJack-Game/assets/104980103/63a5eff5-4add-440b-bcae-feac1c39b01e)

### An implementation of the BlackJack-Game with the following rules:

1) Objective: Beat the dealer's hand without going over 21.

2) Card Values: Numbered cards (2 through 10) are worth their face value. Face cards (Jack, Queen, King) are each worth 10 points. Aces can be worth either 1 point or 11 points, depending on which value benefits the hand the most, but you can only choose its value once when you get the Ace and cannot change it for the rest of the game.

3) The Deal: The dealer deals two cards to each player, starting from themselves. All of the player's cards are dealt face-up, while one of the dealer's cards is face-up (the "upcard") and the other is face-down (the "hidden card").

4) Player's Turn: Players take turns deciding whether to "hit" (take another card) or "stand" (keep their current hand). Players can continue to hit until they are satisfied with their hand or they bust (go over 21).

5) Dealer's Turn: Once all players have completed their turns, the dealer reveals their hidden card. The dealer must hit until their hand totals 17 or more. Some variations of blackjack may require the dealer to hit on a "soft 17" (a hand containing an ace that counts as 11). Althought in this implementation we ignored the rule of Dealer's 17 limit. The Dealer can hit or stop with any card combination.

6) Winning and Losing: If a player's hand is closer to 21 than the dealer's hand without going over, the player wins. If the player's hand exceeds 21, they bust and lose their bet. If the dealer busts and the player does not, the player wins. If both the player and the dealer have the same total the player loses.

___
### A Preview example output after running the python files and choosing 4 players: 

Welcome to BlackJack by Giannis Dilmperis!

The game begins and Players are dealt one card face up in clockwise direction, starting from the dealer.
Then the dealer starts dealing one more round of cards the same way,
keeping only his card face down and all the others face up.

At the end everybody has 2 open cards, except from the Dealer who has one open card and one hidden.


How many players are playing? 4

======== Beginning Dealing Round ========

Dealer gets 2

Player 1 gets K

Player 2 gets J

Player 3 gets 7

Player 4 gets K

 
Dealer gets Hidden Card

Player 1 gets 5

Player 2 gets 7

Player 3 gets 2

Player 4 gets 9
 
========================== Round 1 ==========================

Does Player 1 with ['K', '5'] want another card? Yes or No: yep

Wrong input. Choose Yes or No: yes

Player 1 gets K

Player 1 lost with cards ['K', '5', 'K']. The total value of cards is 25, above 21.

 
Does Player 2 with ['J', '7'] want another card? Yes or No: no

Player 2 has ['J', '7'] with value 17 and stops there.

 
Does Player 3 with ['7', '2'] want another card? Yes or No: yes

Player 3 gets 5

Player 3 has ['7', '2', '5'] with total value of cards 14.

 
Does Player 4 with ['K', '9'] want another card? Yes or No: no

Player 4 has ['K', '9'] with value 19 and stops there.
 
 
========================== Round 2 ==========================


Does Player 3 with ['7', '2', '5'] want another card? Yes or No: yes

Player 3 gets Q

Player 3 lost with cards ['7', '2', '5', 'Q']. The total value of cards is 24, above 21.

 
 
======================= Dealer's Turn =======================

The Dealer's Hidden Card is 4

Player 2 still plays with holding cards ['J', '7'] of value 17

Player 4 still plays with holding cards ['K', '9'] of value 19

 
Does the Dealer with ['2', '4'] want another card? Yes or No: yes

Dealer gets 8

Dealer has ['2', '4', '8'] with total value of cards 14.

 
Does the Dealer with ['2', '4', '8'] want another card? Yes or No: yes

Dealer gets A

The Dealer got A. The Ace counts as 1 or 11? 1

Dealer has ['2', '4', '8', 'A as 1'] with total value of cards 15.

 
Does the Dealer with ['2', '4', '8', 'A as 1'] want another card? Yes or No: yes

Dealer gets 3

Dealer has ['2', '4', '8', 'A as 1', '3'] with total value of cards 18.

 
Does the Dealer with ['2', '4', '8', 'A as 1', '3'] want another card? Yes or No: yes

Dealer gets 2

Dealer has ['2', '4', '8', 'A as 1', '3', '2'] with total value of cards 20.

 
Does the Dealer with ['2', '4', '8', 'A as 1', '3', '2'] want another card? Yes or No: no

Dealer has ['2', '4', '8', 'A as 1', '3', '2'] with value 20 and stops there.


================================= RESULTS ===============================

The Dealer has 20

Player 1 lost with 25.

Player 2 lost with 17.

Player 3 lost with 24.
Player 4 lost with 19.
