import wpilib
import magicbot
from components.drivetrain import DriveTrain

class Robot(magicbot.MagicRobot):
    my_drivetrain : DriveTrain
    
    def createObjects(self):
        self.my_drivetrain_lf = wpilib.Talon(0)
        self.my_drivetrain_lr = wpilib.Talon(1)
        self.my_drivetrain_rf = wpilib.Talon(2)
        self.my_drivetrain_rr = wpilib.Talon(3)
        self.joystick = wpilib.Joystick(1)
    
    def teleopPeriodic(self):
        """With magicbot, there is no scheduler.  It's up to user code to poll
        the joystick buttons and suchlike.
        """
        self.my_drivetrain.arcadeDrive(self.joystick)


if __name__=='__main__':
    wpilib.run(Robot)