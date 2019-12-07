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

## intent:want_recipe
- looking for a recipe
- looking for
- I need a recipe
- want a recipe
- recipe

## intent:provide_diet_info
- [keto](diet)
- [gluten-free](diet)
- [paleo](diet)
- [vegan](diet)

## intent:provide_flavor_info
- [spicy](flavor)
- [sweet](flavor)
- [sour](flavor)
- [bitter](flavor)
- [umami](flavor)

## intent:provide_purpose
- I need something for a [potluck](purpose)
- I need a [dinner](purpose) recipe
- I want [dessert]([purpose])
- I'm looking for something to eat for [breakfast](purpose)
- I'm looking for something [quick](purpose)
- I need something I can cook quickly
- I'd like something for [lunch](purpose)
- 

## intent:search_recipe_by_flavor
- I want something [sweet](flavor)
- I'm craving something [sweet](flavor)
- I want something [spicy](flavor)
- I'm hungry for meat
- I'd like something [salty](flavor)

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

## synonym: quick
    - quick
    - quickly
    - in under 30
    - in under 30 minutes