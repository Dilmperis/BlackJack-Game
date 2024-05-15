# BlackJack-Game

![image](https://github.com/Dilmperis/BlackJack-Game/assets/104980103/63a5eff5-4add-440b-bcae-feac1c39b01e)

### An implementation of the BlackJack-Game broken down in 3 files, the main file, the game file (actual game implementation) and the player file.

### The game has the following rules:

1) Objective: Beat the dealer's hand without going over 21.

2) Card Values: Numbered cards (2 through 10) are worth their face value. Face cards (Jack, Queen, King) are each worth 10 points. Aces can be worth either 1 point or 11 points, depending on which value benefits the hand the most, but you can only choose its value once when you get the Ace and cannot change it for the rest of the game.

3) The Deal: The dealer deals two cards to each player, starting from themselves. All of the player's cards are dealt face-up, while one of the dealer's cards is face-up (the "upcard") and the other is face-down (the "hidden card").

4) Player's Turn: Players take turns deciding whether to "hit" (take another card) or "stand" (keep their current hand). Players can continue to hit until they are satisfied with their hand or they bust (go over 21).

5) Dealer's Turn: Once all players have completed their turns, the dealer reveals their hidden card. The dealer must hit until their hand totals 17 or more. Some variations of blackjack may require the dealer to hit on a "soft 17" (a hand containing an ace that counts as 11). Althought in this implementation we ignored the rule of Dealer's 17 limit. The Dealer can hit or stop with any card combination.

6) Winning and Losing: If a player's hand is closer to 21 than the dealer's hand without going over, the player wins. If the player's hand exceeds 21, they bust and lose their bet. If the dealer busts and the player does not, the player wins. If both the player and the dealer have the same total the player loses.
