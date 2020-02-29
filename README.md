# Recipe Presenting Chatbot

MVP: \
Chatbot designed to search the database of recipes, and easily deliver a recipe
that suits the user's dietary and flavor requirements.

2.0 \
Chatbot will be able to search recipes based on dietary and flavor requirements, 
as well as specified ingredients.

## Getting Started

create a virtual environment 
$ virtualenv env
activate virtual environment
$ source env/bin/activate
$ git clone https://github.com/BeeNeal/rasa_chatbot.git
$ cd rasa_chatbot
$ pip install -r requirements.txt
$ rasa train nlu

## Built With

[Rasa] https://rasa.com/docs/

## Authors

* **Brittany Neal**

### to-do
- combine intents under one umbrella 'inform'
- when integrating with RC site, take user preferences from DB (such as user diet preference)
- add story for a user preference if didn't find a recipe under that diet preference

## Flow
1) Bot greets user with list of what can do (welcome back vs initial greet with prompt for sign in) btns + text option
2) 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
