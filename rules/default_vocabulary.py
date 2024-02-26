

from vocabulary.rules.stack import VOCABULARY_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """

    The label to identify the rule interface.
    """
    label = 'DEFAULT'

VOCABULARY_RULESTACK.add_rule(DefaultRuleClass())
