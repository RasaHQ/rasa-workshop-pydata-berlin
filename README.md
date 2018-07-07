# PyData Berlin - Building conversational AI with the Rasa stack

This repo contains the code for my workshop at PyData Berlin 2018. You can find the slides of my talk [here](https://www.slideshare.net/JustinaPetraityt/deprecating-the-state-machine-building-conversational-ai-with-the-rasa-stack).

## Installation

To follow this demo, you will need Rasa NLU, Rasa Core and spacy installed. You can do it by running:

`python -m pip install -U rasa_core==0.9.6 rasa_nlu[spacy]`

You will also need a spacy language model which you can download by executing:

`python -m spacy download en_core_web_md`

`python -m spacy link --force en_core_web_md en`

## How to use this repository

The repo contains three notebooks:
- `rasa-workshop-starter` - this is a notebook which we will used during the workshop
- `rasa-workshop-completed` - this is a notebook which contains the completed, not executed code of the workshop
- `rasa-workshop-completed-executed` - this is a notebook which contains the complete and executed code of the workshop

The additional files in this repo will be explained during the session. Once you train the models, you can find them in a directory called `models`.

## Get in touch

If you encounter any problems while installing the dependencies or have any questions regarding this notebook, shoot me a message on juste@rasa.com
