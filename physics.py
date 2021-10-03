import math
from math_add import *

class Physics:
    # mathematic 
    pi = 3.1415926535897932384626433832795028841971

    # basic
    g = 9.81
    c = 2.99792458e8
    G = 6.67430151515151515e-11
    h = 6.62607015e-34
    h_ = h / (2 * pi)
    e = 1.602176634e-19
    k = 1.380649e-23
    N_A = 6.0221407610e23
    epsilon0 = 1 / (4e-7 * pi * (c ** 2))
    mu0 = 4e-7 * pi
    alpha = (e ** 2) / (2 * h * epsilon0 * c)

    # Planck units
    m_p = math.sqrt(h_ * c / G)
    l_p = math.sqrt(h_ * G / (c ** 3))
    t_p = math.sqrt(h_ * G / (c ** 5))
    a_p = c / t_p
    E_p = math.sqrt(h_ * (c ** 5) / G)
    T_p = E_p / k
    q_p = math.sqrt(2 * c * h * epsilon0)
    I_p = q_p / t_p
    F_p = (c ** 4) / G
    p_p = (c ** 7) / (h_ * (G ** 2))
    omega_p = 1 / t_p
    L_p = (c ** 5) / G

    # coefficents
    asphalt_friction_coefficient = 0.7

    
    # formulas
    @classmethod
    def density(cls, weight, volume):
        """Density of material object

        Arguments
        ~~~~~~~~~

        weight: `[кг]`
            weight of object\n
            :class:`int` || :class:`float`

        volume: `[м^3]`
            object's volume\n
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        density: `[кг/м^3]`
            density of object
            :class:`int` || :class:`float`
        """
        return f'{weight / volume :g} кг/м^3'

    # MOVING OF OBJECTS
    # ====================================================================================
    # ====================================================================================
    # ====================================================================================
    @classmethod
    def average_speed_by_full(cls, full_movement, full_time):
        """Calculates average speed

        Arguments
        ~~~~~~~~~

        full_movement: `[м]`
            full movement (way) moved by object
            :class:`int` || :class:`float`

        full_time: `[с]`
            full time when object moved
            :class:`int` || :class:`float`

        Return
        ~~~~~~
        
        average_speed: `[м/с]`
            average speed
            :class:`int` || :class:`float`
        """

        return f'{full_movement / full_time :g} м/с'

    @classmethod
    def average_speed_by_speed(cls, speed, start_speed):
        """Calculate average speed by speed and start speed
        
        Arguments
        ~~~~~~~~~

        speed: `[м/с]`
            moving speed maximum
            :class:`int` || :class:`float`

        start_speed: `[м/с]`
            speed with which started object
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        average_speed: `[м/с]`
            object's average speed
            :class:`int` || :class:`float`
        """

        return f'{(speed + start_speed) / 2 :g} м/с'

    @classmethod
    def straight_motion(cls, speed, time):
        """Distance moved in a straight line

        Arguments
        ~~~~~~~~~

        speed: `[м/с]`
            speed of object, who moved this way
            :class:`int` || :class:`float`

        time: `[с]`
            time during which the object moved
            :class:`int` || :class:`float`

        Return
        ~~~~~~
        
        distance: `[м]`
            distance moved
            :class:`int` || :class:`float`
        """
        
        return f'{speed * time :g} м'

    @classmethod
    def acceleration_by_speeds(cls, speed, start_speed, time):
        """Calculate acceleration by speed and start speed
        
        Arguments
        ~~~~~~~~~

        speed: `[м/с]`
            moving speed average or maximum
            :class:`int` || :class:`float`

        start_speed: `[м/с]`
            speed with which started object
            :class:`int` || :class:`float`

        time: `[с]`
            time during which the object moved
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        acceleration: `[м/с^2]`
            object's acceleration
            :class:`int` || :class:`float`
        """

        acceleration = (speed - start_speed) / time

        return f'{acceleration :g} м/с^2'

    @classmethod
    def movement_by_start_speed(cls, start_speed, time, acceleration):
        """Calculate distance object moved by start speed, time and acceleration

        Arguments
        ~~~~~~~~~

        speed: `[м/с]`
            moving speed average or maximum
            :class:`int` || :class:`float`

        start_speed: `[м/с]`
            speed with which started object
            :class:`int` || :class:`float`

        time: `[с]`
            time during which the object moved
            :class:`int` || :class:`float`

        accelaration: `[м/с^2]`
            object's accelaration
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        moving: `[м]`
            object's distance, who his moved
            :class:`int` || :class:`float`
        """

        moving = (start_speed * time) + (acceleration * (time ** 2) * 0.5)

        return f'{moving :g} м'

    @classmethod
    def movement_by_speeds(cls, speed, start_speed, accelerate):
        """Calculate distance object moved by speeds and accelerate

        Arguments
        ~~~~~~~~~

        speed: `[м/с]`
            moving speed average or maximum
            :class:`int` || :class:`float`

        start_speed: `[м/с]`
            speed with which started object
            :class:`int` || :class:`float`

        accelaration: `[м/с^2]`
            object's accelaration
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        moving: `[м]`
            object's distance, who his moved
            :class:`int` || :class:`float`
        """

        moving = ((speed ** 2) - (start_speed ** 2)) / (2 * accelerate)

        return f'{moving :g} м'

    @classmethod
    def braking_distance(cls, speed):
        """Calculate distance object moved by speeds and accelerate

        Arguments
        ~~~~~~~~~

        speed: `[м/с]`
            moving speed average or maximum
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        braking distance: `[м]`
            object's distance, who his moved in braking
            :class:`int` || :class:`float`
        """

        moving = (speed ** 2) / (2 * cls.g * cls.asphalt_friction_coefficient)

        return f'{moving :g} м'

    # END
    # ====================================================================================
    # ====================================================================================
    # ====================================================================================


    # FALLING
    # ====================================================================================
    # ====================================================================================
    # ====================================================================================
    @classmethod
    def falling_speed(cls, height):
        """Calculates falling speed of obejct from n-high
        
        Arguments
        ~~~~~~~~~

        height: `[м]`
            the height from which the object was dropped
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        speed: `[м/с]`
            falling speed
            :class:`int` || :class:`float`
        """

        speed = math.sqrt(2 * cls.g * height)

        return f'{speed :g} м/с'

    @classmethod
    def falling_time(cls, height):
        """Calculates falling time of obejct from n-high
        
        Arguments
        ~~~~~~~~~

        height: `[м]`
            the height from which the object was dropped
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        time: `[с]`
            falling time
            :class:`int` || :class:`float`
        """

        time = math.sqrt(2 * height / cls.g)

        return f'{time :g} с'

    @classmethod
    def falling_height(cls, falling_speed):
        """Calculates height where falled object
        
        Arguments
        ~~~~~~~~~
        
        falling_speed: `[м/с]`
            object's falling speed
            :class:`int` || :class:`float`
            
        Return
        ~~~~~~
        
        height: `[м]`
            height, from which the object fell
            :class:`int` || :class:`float`
        """

        height = (falling_speed ** 2) / (2 * cls.g)

        return f'{height :g} м'

    # END
    # ====================================================================================
    # ====================================================================================
    # ====================================================================================

    # CIRCLE
    # ====================================================================================
    # ====================================================================================
    # ====================================================================================

    @classmethod
    def frequency_by_turns(cls, turns_count, turnaround_time):
        """Calculater frequency by turns any turnaround time
        
        Arguments
        ~~~~~~~~~

        turns_count: [число]
            turns count of object in certain time
            :class:`int` || :class:`float`

        turnaround_time
        """