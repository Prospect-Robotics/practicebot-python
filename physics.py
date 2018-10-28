#
# See the documentation for more details on how this works
#
# The idea here is you provide a simulation object that overrides specific
# pieces of WPILib, and modifies motors/sensors accordingly depending on the
# state of the simulation. An example of this would be measuring a motor
# moving for a set period of time, and then changing a limit switch to turn
# on after that period of time. This can help you do more complex simulations
# of your robot code without too much extra effort.
#


from pyfrc.physics import motor_cfgs, drivetrains
from pyfrc.physics.units import units


class PhysicsEngine(object):
    
    def __init__(self, physics_controller):
        '''
            :param physics_controller: `pyfrc.physics.core.PhysicsInterface` object
                                       to communicate simulation effects to
        '''
        
        self.physics_controller = physics_controller
        self.drivetrain = drivetrains.FourMotorDrivetrain()
            
    def update_sim(self, hal_data, now, tm_diff):
        
        lf = hal_data['pwm'][0]['value']
        lr = hal_data['pwm'][1]['value']
        rf = hal_data['pwm'][2]['value']
        rr = hal_data['pwm'][3]['value']
        
        y, angle = self.drivetrain.get_vector(lr, rr, lf, rf)
        self.physics_controller.drive(y, angle, tm_diff)
            