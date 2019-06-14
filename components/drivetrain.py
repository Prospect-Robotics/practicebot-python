import wpilib
import rev

#MotorType = wpilib.RobotDrive.MotorType
#del wpilib.RobotDrive.MotorType # having nested classes present messes up variable injection.

class DriveTrain(wpilib.RobotDrive):
    lf : rev.CANSparkMax
    rf : rev.CANSparkMax
    lr : rev.CANSparkMax
    rr : rev.CANSparkMax
    joystick : wpilib.Joystick
    
    MotorType = None
    
    def __init__(self):
        # The dependencies haven't been injected yet, we can't call super().__init__()
        pass
    
    def setup(self):
        # setup() is called after magic variable injection.
        super().__init__(self.lf, self.lr, self.rf, self.rr)
    
    def execute(self):
        # The robot main loop handles periodic tasks on the drivetrain.  We
        # don't need to do anything.
        # (The robot program will crash if this method isn't here, so we must 
        # have this empty implementation.)
        pass
    
    def joystick_drive(self):
        self.arcadeDrive(self.joystick)