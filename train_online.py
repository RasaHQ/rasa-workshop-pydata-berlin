from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy

logger = logging.getLogger(__name__)


def run_online(input_channel, interpreter,
                          domain_file="domain.yml",
                          training_data_file='stories.md'):
    fallback = FallbackPolicy(fallback_action_name="utter_unclear",
                          core_threshold=0.2,
                          nlu_threshold=0.4)

    agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy(), fallback], interpreter = interpreter)
	
	

    training_data = agent.load_data(training_data_file)
    agent.train_online(training_data,
                       input_channel=input_channel,
                       epochs=200)

    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    nlu_interpreter = RasaNLUInterpreter('models/nlu/default/current')
    run_online(ConsoleInputChannel(), nlu_interpreter)