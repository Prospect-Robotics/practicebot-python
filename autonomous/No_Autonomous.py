import wpilib
from magicbot.state_machine import *

class NullAuto(AutonomousStateMachine):
    @state(first=True)
    def do_nothing(self):
        pass
