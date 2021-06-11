from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.container import Container


def validate_input_variable_type(variable):
    if type(variable) != Container:
        raise RuntimeError('Failed to add sound to container. Given variable should be container.')


class AddSoundToContainerStatement():

    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.AddSoundToContainerStatementContext):
        sound = ctx.SOUND()
        container = variables.get(str(ctx.VARIABLE()))
        try:
            validate_input_variable_type(container)
        except RuntimeError as err:
            print(err)
            return
        container.value.append(str(sound))
