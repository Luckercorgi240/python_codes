class Things:
    def show_introduction(self):
        print('Hello, I am + ' + type(self).__name__)

class Inanimate(Things):
	pass

class Animate(Things):
    def do_stuff(self):
        print(type(self).__name__ + ' do animate stuff')

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print(type(self).__name__ + ' breathe')
    def move(self):
        print(type(self).__name__+ ' move')
    def eat_food(self):
        print(type(self).__name__ + ' eat food')
    def lay_eggs(self):
        print(type(self).__name__ + ' lay eggs')

# class Things(Things)
#     def do_something(self):
#         print(type(self).__name__ + "do something...")    

class Mammals(Animals):
    def feed_young_with_milk(self):
        print(type(self).__name__ + ' feed young with milk')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print(type(self).__name__ + ' eat leaves from trees')

class Dolphins(Mammals):
    def eat_fish(self):
        print(type(self).__name__ + ' eat fish')
    def do_stuff(self):
        print(type(self).__name__ + ' do dolphin stuff')
    
    def move(self):
        print(type(self).__name__ + " swim")

class Chickens(Animals):
    def lay_eggs(self):
        print(type(self).__name__ + ' lay eggs')

class Humans(Mammals):
    def chew_gum(self):
        print(type(self).__name__ + ' chew gum')

reginald = Giraffes()
reginald.breathe()
reginald.eat_food()
reginald.move()
reginald.feed_young_with_milk()
reginald.eat_leaves_from_trees()
print()

longneck = Giraffes()
longneck.breathe()
longneck.eat_food()
longneck.move()
longneck.feed_young_with_milk()
longneck.eat_leaves_from_trees()
print()

egghead = Chickens()
egghead.breathe()
egghead.eat_food()
egghead.lay_eggs()
egghead.do_stuff()
print()

blue = Dolphins()
blue.breathe()
blue.eat_fish()
blue.feed_young_with_milk()
blue.move()
blue.do_stuff()

pan = Humans()
pan.breathe()
pan.chew_gum()
pan.do_stuff()
pan.eat_food()
pan.feed_young_with_milk()