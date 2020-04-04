<!-- 
each ## are example stories - 
## story title
* user 
    - action taken by assistant
 -->

## Search recipe happy path
* greet
  - utter_greet
* want_recipe{"flavor":"spicy", "diet":"keto"}
  - action_recipe_search
* thanks
  - utter_goodbye

## Search recipe with ingredient happy path
* greet
   -utter_greet
* want_recipe{"ingredient:"olives"}
   -search_recipe_by_ingredient
   -utter_confirm_appeasement
* affirm

## Search recipe with ingredient sad path
* greet
   -utter_greet
* want_recipe{"ingredient:"olives"}
   -action_search_recipe_by_ingredient
   -confirm_appeasement
* deny
   -utter_ask_purpose

## determine preferences
* greet
	- utter_new_user_greet

## provide purpose
* greet
  - utter_greet
* want_recipe
  - action_recipe_search
  - utter_ask_purpose

## search recipe + flavor query
* greet
  - utter_greet
* want_recipe{"diet":"keto"}
  - utter_ask_flavor
  - slot{"flavor":"spicy"}
<!--general inform is better, then capture wider range of entities -->
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
  - slot{"flavor":"spicy"}


## happy path
* greet
  - utter_greet
* request_recipe
  - recipe_form
  - form{"name: "recipe_form"}
  - form{"name": null}
  - utter_slots_values
* thankyou
  - utter_goodbye

<!-- {"purpose": "dessert", "diet_type":"keto"}
   - action_recipe_search
   - form{"name: "action_recipe_search"}
   - form{"name": null}
 -->

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

## user asks whats possible
* ask_whats_possible
  - utter_explain_whats_possible

## user asks for something out of scope
* out_of_scope
  - utter_cannot_help
  - utter_explain_whats_possible

<!-- ## fallback policy
   - utter_clarify
   - utter_explain_whats_possible -->
## interactive_story_1
* greet
    - action_default_ask_affirmation
* out_of_scope



<!-- how to determine not_appeased b/c not ___diet, or with new intent of need for a potluck? -->