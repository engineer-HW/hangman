from random import shuffle

#Card
class Card():
    suits = ["spades","hearts","diamonds","clubs"]
    
    values = [None, None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

    def __init__(self, v, s):
        """スートも値も整数値です"""
        self.value = v
        self.suit = s
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False
        
    def __repr__(self):
        v = self.values[self.value] + "of" + self.suits[self.suit]
        return v
"""
カードクラスには2つのクラス変数suitsとvaluesが存在する。
valuseの最初の2つの要素には、リストのインデックス操作と値が一致するように、Noneをもたせている
ハートの2のカードを作成するなら、values[2]、suits[1]を指定すれば良い

特殊メソッド
__lt__
__gt__
上記の2つの特殊メソッドのおかげで、Cardオブジェクトは大小比較の演算子で比較できるようになる。

"""

#Deck
class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2, 15): #2から15
            for j in  range(4):
                self.cards.append(Card(i, j))
            shuffle(self.cards)

    def rm_card(self): #cardsリストから要素を一つ削除して、その要素を返す。リストの中が空だったら、Noneを返す
        if len(self.cards) == 0:
            return
        return self.cards.pop()

#Player
class Player():
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

#Game
class Game():
    def __init__(self):
        name1 = input("プレーヤー1の名前")
        name2 = input("プレーヤー2の名前")
        self.deck = Deck() #呼び出されると52枚のトランプが用意される
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは{}が勝ちました"
        w = w.format(winner)
        print(w)
    
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{}は{}、{}は{}を引きました"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards #52枚のトランプを変数cardsに格納
        print("戦争を始めます")
        while len(cards) >= 2: #トランプの枚数が2枚以下になったら終了
            m = "qで終了、それ以外のキーでplay:"
            respomse = input(m) #下の行と比較するために変数に格納している
            if respomse == 'q':
                break
            p1c = self.deck.rm_card() #プレーヤー1のカード
            p2c = self.deck.rm_card() #プレーヤー2のカード
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1 #勝ったら1点＋
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け"
    
game = Game()
game.play_game()

"""
Gameオブジェくトを作成すると、
1.プレーヤーの名前を聞いてくる
2.Deckオブジェクトを作成して、変数name1,name2を使って、Playerオブジェクトを作る
3.gameオブジェクトのplay_gameメソッドでゲームがはじまる
"""