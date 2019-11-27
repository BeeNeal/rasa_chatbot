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

class ActionFetchRecipe(Action):
      
# refers to the name of the action used when creating training stories
# how rasa knows which action to run when predicted
    def name(self) -> Text:
        return "action_recipe_search"
# define what the action does
    def run(self, dispatcher: CollectingDispatcher,
        # tracker keeps track of conversation state
        # dispatcher sends response back to user
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        diet = tracker.get_slot("diet")
        dispatcher.utter_message("Cool, let me find a {} recipe for you!".format(diet))

        # these events must be reflected in training stories
        return [SlotSet("diet", diet)]
