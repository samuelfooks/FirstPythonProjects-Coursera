# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score_player = 0
score_dealer=0
deck=[]
player_hand=[]
dealer_hand=[]
playerupdate=str("")
dealerupdate=str("")
outcome=str("")
playerturn=True

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def drawcardback(self, canvas, pos):
        card_loc= (36,48)
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0]+CARD_BACK_CENTER[0],pos[1]+CARD_BACK_CENTER[1]],CARD_BACK_SIZE)
        # define hand class
class Hand:
    global player_hand, dealer_hand, playerturn, in_play
    def __init__(self):
        self.hand=[]
        
        

    def __str__(self):
        hand_string="hand contains "
        for i in range(len(self.hand)):
            hand_string += str(self.hand[i])
            
        return hand_string
    

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        hand_value=[]
        
        for card in self.hand:
            rank=card.rank
            value=VALUES[rank]
            hand_value.append(value)
        
        for card in self.hand:
            rank=card.rank
            if rank != "A":
            
                return  sum(hand_value)
        
            else:
                if sum(hand_value)+10<=21:
                    return (sum(hand_value) + 10)
            
                else:
                    return sum(hand_value) 
                
    def drawplayer(self, canvas, pos):
        for card in self.hand:
            cardposition=(100*self.hand.index(card) + 20),(20)
            card.draw(canvas,cardposition)
    def drawdealer(self,canvas, pos):
        for card in self.hand:
            cardpos=(100*self.hand.index(card)+20),(400)
            card.draw(canvas,cardpos)
            if in_play==True:
                card.drawcardback(canvas,[20,400])
                
            else:
                card.draw(canvas,cardpos)
            
            
                
    
            
                
#            
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
        
        
#        list comprehension
#        rank_suit_list=[suit+rank for suit in SUITS for rank in RANKS]

        
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
       
       
                
    def __str__(self):
        deck_string="deck contains"
        for i in range(len(self.deck)):
            deck_string += str(" ") + str(self.deck[i])
            
        return deck_string
    
    def shuffle(self):
        self.shuffle=random.shuffle(self.deck)
        return self.deck
        
    def deal_card(self):
        return self.deck.pop(-1)
        
       
                
                
#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand,dealer_hand,playerupdate, dealerupdate

    # your code goes here
    playerupdate=str("")
    dealerupdate=str("")
    playerturn=True
    in_play = True
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    dealer_hand=Hand()
    i=0
    while i < 2:
        dealt_card=deck.deal_card()
        player_hand.add_card(dealt_card)
        i+=1
    j=0
    while j < 2:
        dealt_card=deck.deal_card()
        dealer_hand.add_card(dealt_card)
        j+=1
    
    playerupdate=str("Hit or Stand?")
    

    
def hit():
    global in_play, player_hand, score_dealer, playerupdate, dealerupdate
    if in_play==True:
       
        if player_hand.get_value()<=21:
            player_hand.add_card(deck.deal_card())
            
            playerupdate=str("Player hand " + str(player_hand.get_value()))
            if player_hand.get_value()<=21:
                playerupdate=str("Hit? or Stand?")
            else:
                playerupdate=str("Hand is busted at " + str(player_hand.get_value()))
                in_play=False
                dealerupdate= str("Dealer wins at " + str(dealer_hand.get_value()))
                score_dealer+=1
                
def stand():
    global in_play, dealer_hand, score_player, score_dealer, dealerupdate, playerupdate 
    if in_play==True:
        playerupdate= str("Player stays at " + str(player_hand.get_value()))
        if dealer_hand.get_value()<=21:
            while dealer_hand.get_value()<=17:
                dealer_hand.add_card(deck.deal_card())
                
                dealerupdate=str("Dealer hand " + str(dealer_hand.get_value()))
            
            else:
                in_play=False
                if dealer_hand.get_value()<=21:
                    dealerupdate=str("Dealer stays at " + str(dealer_hand.get_value()))
                     
                    
                    if dealer_hand.get_value()>=player_hand.get_value():
                    
                        playerupdate=str("House wins, thats fucking vegas for ya")
                        score_dealer +=1
                    else:
                        playerupdate=str( "player wins at" + str(player_hand.get_value())+ ",wow")
                        score_player+=1
                else:
                    dealerupdate=str("Dealer busted at "+ str(dealer_hand.get_value()))
                    playerupdate=str( "player wins at " +str(player_hand.get_value())+ ",wow")
                    score_player+=1
      
                
            
      
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_hand, dealer_hand, dealerupdate, playerupdate, score_player, score_dealer, in_play
    
    
    dealer_hand.drawdealer(canvas,[200,200])
        
    player_hand.drawplayer(canvas,[100,20])
    
    
     
    
    canvas.draw_text("Player Cards", [130,150], 24, "blue")
    canvas.draw_text(str(playerupdate), [180,200], 26, "blue")
    canvas.draw_text(("Player score= " + str(score_player)), [400,150], 24, "blue")
    canvas.draw_text("Dealer Cards", [130, 380], 24, "red")
    canvas.draw_text(str(dealerupdate), [300,340], 26, "red")
    canvas.draw_text(("Dealer score= "+ str(score_dealer)), [400,380], 24, "red")
#    canvas.draw_text(outcome, [300,300], 36, "black")
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
