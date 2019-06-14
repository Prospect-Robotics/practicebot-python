import wpilib
import magicbot
import rev
from components.drivetrain import DriveTrain

class Robot(magicbot.MagicRobot):
    drivetrain : DriveTrain
    
    def createObjects(self):
        self.drivetrain_lf = rev.CANSparkMax(0, rev.MotorType.kBrushless)
        self.drivetrain_lr = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.drivetrain_rf = rev.CANSparkMax(2, rev.MotorType.kBrushless)
        self.drivetrain_rr = rev.CANSparkMax(3, rev.MotorType.kBrushless)
        self.joystick = wpilib.Joystick(1)
    
    def teleopPeriodic(self):
        """With magicbot, there is no scheduler.  It's up to user code to poll
        the joystick buttons and suchlike.
        """
        self.drivetrain.arcadeDrive(self.joystick)


if __name__=='__main__':
    import site
    wpilib.run(Robot)