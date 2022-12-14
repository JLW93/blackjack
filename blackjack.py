from random import shuffle

class Blackjack():

    def __init__(self, deck, player, dealer):
        """
        Takes in 3 lists. One for the deck of cards, one for the
        player's empty hand, and one for the dealer's empty hand.
        """

        self.deck = deck
        self.player = player
        self.dealer = dealer
    
    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        """
        Takes 1 card from the top of the shuffled deck (end of the list) and
        adds it to the player's hand until they have 2 cards, and does the 
        same for the dealer's hand.
        """

        while len(self.player) < 2:
            self.player.append(self.deck.pop())
        
        while len(self.dealer) < 2:
            self.dealer.append(self.deck.pop())

    def total(self):
        """
        Prints out 1 of the 2 cards in the dealer's hand, keeping the other
        hidden. Then prints out the player's hand and the total value of those cards.
        Returns the total to be used outside of the Class later.
        """

        print(f'Dealer\'s hand: {self.dealer[-1]} (One card is hidden)')
        total = sum(self.player)
        print(f'Your hand: {self.player}')
        print(f'Your total: {total}')

        return total

    def hit(self):
        """
        Pops off the top card of the deck (last item in the list), and adds it to
        the player's hand.
        """

        self.player.append(self.deck.pop())

    def reveal(self):
        """
        Prints out the contents and totals of both hands. If the dealer's total is less than
        17, the dealer hits. Otherwise, the dealer will stand. Compares the values and prints
        the results accordingly.
        """

        print(f'Your Hand: {self.player}, Your total: {sum(self.player)}.')
        print(f'Dealer\'s Hand: {self.dealer}, Dealer\'s total: {sum(self.dealer)}.')

        while sum(self.dealer) < 17:
            self.dealer.append(self.deck.pop())
            print(f'\nDealer\'s new hand: {self.dealer}, Dealer\'s new total: {sum(self.dealer)}.\n')

        if sum(self.player) > 21:
            print('You busted!')
        elif sum(self.player) == sum(self.dealer):
            print('Game tied.')
        elif sum(self.player) > sum(self.dealer) and sum(self.player) < 21 or sum(self.player) == 21:
            print('You win!')
        elif sum(self.player) < sum(self.dealer) and sum(self.dealer) < 21 or sum(self.dealer) == 21:
            print('You lose!')
        elif sum(self.dealer) > 21:
            print('Dealer busted. You win!')

    def reset(self):
        """
        Places the cards from the player's and dealer's hands back into the deck, to be reshuffled.
        """
        while len(self.player) > 0:
            self.deck.append(self.player.pop())

        while len(self.dealer) > 0:
            self.deck.append(self.dealer.pop())

# 13 cards per suit, 4 suits in a deck of cards.
# Suit doesn't come into play in Blackjack, so suits are not specified here
# Only the number value matters
deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] * 4
player = []
dealer = []

game = Blackjack(deck, player, dealer)

while True:
    start = input('\nWould you like to start playing Blackjack? ')
    if start.lower() == 'yes':
        turn = 1
        game.reset()
        game.shuffle()
        game.deal()
        while True:
            total = game.total()
            if total == 21 and turn == 1:
                print('You win!')
                break
            elif total > 21:
                print('You busted!')
                break
            action = input('\nWould you like to Hit, or Stand? ')
            if action.lower() == 'hit':
                game.hit()
                turn += 1
            elif action.lower() == 'stand':
                game.reveal()
                break
            else:
                print('Please choose either to Hit or Stand')      
    else:
        print('Have a nice day.')
        break
