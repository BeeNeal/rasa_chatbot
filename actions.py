# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from /SpoonacularAPI/spoon_trial import *

class ActionFetchRecipe(Action):
      
# refers to the name of the action used when creating training stories
# how rasa knows which action to run when predicted
    def name(self) -> Text:
        return "action_recipe_search" # FIX THIS *&#*#*#&@)& (take off s)
# define what the action does
    def run(self, dispatcher: CollectingDispatcher,
        # tracker keeps track of conversation state, and which slots should be
        # filled at certain states
        # dispatcher sends response back to user
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        diet = tracker.get_slot("diet")
        dispatcher.utter_message("Cool, let me find a {} recipe for you!".format(diet))

        # these events must be reflected in training stories
        return [SlotSet("diet", diet)]

# Using the SWAPI API to return Star Wars data 

ENDPOINTS = {
    "base": "https://swapi.co/api/people/"
},

class ActionFetchStarWarsCharacterInfo(Action):
    # name is the title for the trigger to run the action
    def name(self) -> Text:
        return "action_star_wars_search"

    # the actual action that gets run when name is invoked
    def run(self, dispatcher: CollectingDispatcher,
        # tracker keeps track of slots
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sw_chars_to_id = {
            "Leia": 5,
            "Han": 14,
            "Chewie": 13,
            "Luke": 1,
            "C-3PO": 2,
            "R2-D2": 3,
            "Darth Vader": 4,
        }
        sw_character = tracker.get_slot("sw_character")
        full_path = ENDPOINTS[0] + sw_chars_to_id[sw_character]
        results = requests.get(full_path).json()
        if results:
            hair_color = results['hair_color']
            height = results['height']
            full_name = results['name']
            return "{} has {} hair, and is {}cm tall.".format(full_name)

        else:
            print("CHARACTER NOT FOUND")
            return "Hmm I don't know that character..."

        # dispatcher sends response back to user
        dispatcher.utter_message("Cool, let me find some info about {} for you!".format(sw_character))

def _create_path(base, sw_char_id):
    """Creates path to find star wars character data using endpoints"""

    # as of right now, is overkill
    pass

# _______________________________________
def fetch_recipe():
    """Fetch recipe from DB"""

    def name(self) -> Text:
        return "action_recipe_search"

    dispatcher.utter_message("This is working!") 

def test_custom_action(FormAction):
    """ """

    def name(self) -> Text:
        return "action_recipe_search"

    @staticmethod
    def required_slots(tracker:Tracker) -> List[Text]:
        # returns names of all slots that must be provides
        return ["purpose", "diet_type"]
    
    # can define slot_mappings here (8:50 ep 8 on rasa vid)

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
              ) -> List[Dict]:
        """Once req slots are filled, print buttons for available options"""

        purpose = tracker.get_slot('purpose')
        diet_type = tracker.get_slot("diet_type")

        results = ask_spoonacular()

        if len(results) == 0:
            return.utter_message("Sorry - try again")

            return []

        buttons = []
        message = "Here is the ingredient: {}".format(results[0])
        dispatcher.utter_button_message(message, buttons)

def ask_spoonacular(purpose, diet_type):
    """TEST """

    response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
    data = response.json()
    print(data[0]['name'])
    return data[0]