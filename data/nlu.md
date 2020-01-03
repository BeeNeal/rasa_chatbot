<!-- write NLU model training examples

These are things a user may say 

label entities by enclosing in brackets with label in parentheses
 ie: [entity](label)

 Don't have to capture all possible intents , 10-15 examples/intent of good 
 quality is a good start. Check that examples correspond to the actual intents, 
 and make sure examples are diverse -->

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- right
- definitely
- absolutely
- sure

## thanks
- thanks
- thank you
- great! Thank you!
- awesome, you're the best
- you're the best
- appreciate it

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:deny
- no
- never
- nah
- nope
- I don't think so
- don't like that
- no way
- not really
- what?
- negative

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- see ya
- peace

## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- hi there
- how's it going
- how's it goin?
- howdy

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad
- feeling blue

<!-- star wars test b/c convenient SWAPI API for custom functions -->
## intent:ask_about_star_wars
- hey do you know anything about star wars?
- have you seen star wars?
- Star Wars
- star wars


## intent:provide_star_wars_char_info
- [Leia](sw_character)
- [Luke](sw_character) Skywalker
- Princess [Leia](sw_character)
- [Leia](sw_character) Organa
- [Han](sw_character)
- [Han](sw_character) Solo
- [Chewie](sw_character)
- Chewbacca
- [Luke](sw_character)
- [Darth Vader](sw_character)
- Darth
- Vader
- [R2-D2](sw_character)
- [C-3PO](sw_character)

## intent:provide_recipe
- Can you save www.recipe@this.com for later? 
- Can you add this recipe to my saved recipes?
- Please add this recipe to my save-for-later
- please save this recipe
- can you save this recipe URL for me?
- please keep this recipe
- please add this recipe: www.recipe@this.com
- store this www.recipe@this.com recipe for me 
- would you save this recipe for me?
- save this
- I want to save this recipe
- I want to save this for later
- I need this for later
- I need to try this later
- add this to my save for later
- file this away for later

## intent:provide_ingredient
- I'm searching for a recipe that uses [olives](ingredient)
- I have [olives](ingredient) I want to use up
- I need a recipe that uses olives
- I'm looking for a recipe with pistachios

## intent:want_recipe
- looking for a recipe
- looking for
- I need a recipe
- want a recipe
- recipe
- Do you have a recipe
- Can you give me an idea for
- Can you give me a dessert idea
- what is your favorite dessert?
- What's the best broccoli dish?
- what's a good salad dressing?
- what's good to eat when you're feeling sick?
- I need something for a [potluck](purpose)
- I need an item for a [potluck](purpose)
- I need a [dinner](purpose) recipe
- I want [dessert](purpose)
- I need [dessert](purpose)
- I need to bring something for a [potluck](purpose)
- I need to bring something to a [potluck](purpose)
- What's a good dish to bring to a [potluck](purpose)?
- I'm looking for something to eat for [breakfast](purpose)
- I'm looking for something [quick](purpose)
- I need something I can cook quickly
- I'd like something for [lunch](purpose)
- I'm searching for a [paleo](diet) recipe
- I'm [paleo](diet) and need a [dessert](purpose) recipe
- Do you have any [paleo](diet) [dessert](purpose) recipes?
- Do you have any recipes for a [paleo](diet) [dessert](purpose)?

## intent:provide_flavor_info
- [spicy](flavor)
- [sweet](flavor)
- [sour](flavor)
- [bitter](flavor)
- [umami](flavor)
- [refreshing](flavor)


## intent:provide_diet_info
- [keto](diet)
- [gluten-free](diet)
- [paleo](diet)
- [vegan](diet)
- 

## intent:search_recipe_by_flavor
- I want something [sweet](flavor)
- I'm craving something [sweet](flavor)
- I want something [spicy](flavor)
- I'm hungry for meat
- I'd like something [salty](flavor)
- I'm in the mood for something [salty](flavor)
- I'm in the mood for something [savory](flavor)
- Something [sweet](flavor) sounds good
- Something [sugary](flavor) sounds good

## intent:inform_location
- [San Francisco](location)
- [New York](location)
- [Seattle](location)
- [San Jose](location)

## regex:email
- ^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$

## synonym: keto-code
	- keto
	- high-fat
	- high fat
	- low-carb
	- low carb

## synonym: paleo
	- paleo
	- primal
	- grain-free

## synonym: sweet
	- sweet
	- sugar
	- sugary
	- sugared
	- sweetened
	- saccharine

## synonym: salty
	- salt
	- salty
	- salted
	- savory

## synonym: quick
    - quick
    - quickly
    - in under 30
    - in under 30 minutes