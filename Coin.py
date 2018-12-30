import random


class Coin:
    def __init__(self,rare=False,clean=True,heads=True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value) 
        
        self.is_rare=rare
        self.is_clean=clean
        self.heads=heads

        if self.is_rare:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value

        if self.is_clean:
            self.color=self.clean_color
        else:
            self.color=self.rusty_color

    def rust(self):
        self.color=self.rusty_color    

    def clean(self):
        self.color=self.clean_color

    def __del__(self):
        print("Coin Spend")

    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads=choice

    def __str__(self):
        if self.original_value>=1:
            return "${} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value*100))
        

class Pound(Coin):
    def __init__(self):
        data={
            "original_value":1.00,
            "clean_color":"gold",
            "rusty_color":"greenish",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
            }
        
        super().__init__(**data)

class One_Pence(Coin):
    def __init__(self):
         data={
            "original_value":0.01,
            "clean_color":"bronze",
            "rusty_color":"brownish",
            "num_edges":1,
            "diameter":20.3,
            "thickness":1.52,
            "mass":3.50
            }
         super().__init__(**data)


coins=[One_Pence(),Pound()]

for coin in coins:
    arguments=[coin, coin.color,coin.value,coin.diameter,coin.thickness,coin.mass]

    string="{}- Color, Value:{}, Diameter:{}, Thickness:{}, Mass:{}".format(*arguments)

    print(string)
