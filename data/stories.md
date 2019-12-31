<!-- 
each ## are example stories - 
## story title
* user 
    - action taken by assistant
 -->

## provide purpose
* greet
  - utter_greet
* want_recipe
	- action_recipe_search
  - utter_ask_purpose

## Search recipe happy path
* greet
  - utter_greet
* want_recipe{"flavor":"spicy", "diet":"keto"}
  - action_recipe_search
* thanks
  - utter_goodbye

## search recipe + flavor query
* greet
  - utter_greet
* want_recipe{"diet":"keto"}
	- utter_ask_flavor
	- slot{"flavor":"spicy"}
<!--general inform is better, than capture wider range of entities -->
* inform{"flavor":"spicy"}
  - action_recipe_search
* thanks
  - utter_goodbye

## search recipe + diet query
* greet
  - utter_greet
* want_recipe
	- utter_ask_diet_info
	- slot{"diet":"keto"}
	- utter_ask_flavor
	-slot{"flavor":"spicy"}

<!--general inform is better, than capture wider range of entities -->
* inform{"flavor":"spicy"}
   - action_recipe_search
* thanks
  - utter_goodbye


## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy


## save recipe for later path
* provide_recipe
  - utter_store_recipe_confirmation
* thanks
  - utter_goodbye

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
