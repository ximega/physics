import math
import re

class Result:
    def __init__(self, value, unit):
        self.__value__ = value
        self.unit = unit
        self.result = f'{value} {unit}'

    @property
    def __repr__(self):
        return f'<Result < result: {self.result} > value = {self.__value__}, unit = {self.unit}>'

    def __str__(self):
        return self.result

    def toValue(self):
        """
        Interpretates result to int or float value
        """
        return self.__value__

class Physics:
    # mathematic 
    pi = 3.1415926535897932384626433832795028841971

    # basic constants
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
            weight of object
            :class:`int` || :class:`float`

        volume: `[м^3]`
            object's volume
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        density: `[кг/м^3]`
            density of object
            :class:`int` || :class:`float`
        """
        return Result(weight / volume, 'кг/см^3')

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

        return Result(full_movement / full_time, 'м/с')

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

        return Result((speed + start_speed) / 2, 'м/с')

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
        
        return Result(speed * time, 'м')

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

        return Result(acceleration, 'м/с^2')

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

        return Result(moving, 'м')

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

        return Result(moving, 'м')

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

        return Result(moving, 'м')

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

        return Result(speed, 'м/с')

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

        return Result(time, 'с')

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

        return Result(height, 'м')

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
        """Calculater frequency by turns and turnaround time
        
        Arguments
        ~~~~~~~~~

        turns_count: [число]
            turns count of object in certain time
            :class:`int` || :class:`float`

        turnaround_time: [c]
            time of object turn around circle
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        frequency: [Гц]
            :class:`int` || :class:`float`
        """

        return Result(turns_count / turnaround_time, 'Гц')

    @classmethod
    def frequency_by_period(cls, period):
        """Calculater frequency by period
                
        Arguments
        ~~~~~~~~~

        period: [с]
            object turned time per one turnover
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        frequency: [Гц]
            :class:`int` || :class:`float`
        """

        return Result(1 / period, 'Гц')

    @classmethod 
    def period_by_turns(cls, turnaround_time, turns_count):
        """Calculater period by turns and turnaround time
        
        Arguments
        ~~~~~~~~~

        turnaround_time: [c]
            time of object turn around circle
            :class:`int` || :class:`float`

        turns_count: [число]
            turns count of object in certain time
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        period: [с]
            :class:`int` || :class:`float`
        """

        return Result(turnaround_time / turns_count, 'с')

    @classmethod
    def period_by_frequency(cls, frequency):
        """Calculater period by frequency
                
        Arguments
        ~~~~~~~~~

        frequency: [Гц]
            object's frequency
            :class:`int` || :class:`float`

        Return
        ~~~~~~

        period: [с]
            :class:`int` || :class:`float`
        """

        return Result(1 / frequency, 'с')