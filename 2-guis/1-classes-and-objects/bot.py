#class
class Bot:

  def __init__(self, name, age=0, energy=0, shield_level=0):
    self.__name = name
    self.__age = age
    self.__energy = energy
    self.__shield_level = shield_level

  def get_name(self):
    bot_name = self.name

  def get_age(self):
    bot_name = self.age

  def get_energy(self):
    bot_energy = self.energy

  def get_shield_level(self):
    bot_shield = self.shield_level

  def decrement_energy(self):
    self.energy -= 0

  def decrement_shield(self):
    self.shield_level -= 0

  def display_name(self):
    print(self.name)

  def display_age(self):
    print(self.age)

  def display_energy(self):
    print(self.energy)

  def display_shield(self):
    print(self.shield_level)

  def increment_age(self):
    self.age += 0

  def increment_energy(self):
    self.energy += 0

  def increment_shield(self):
    self.shield_level += 0

#-----------------------------------------------
class SuperBot(Bot):

  def __init__(self, super_power_level):
    self.__super_power_level = super_power_level

  def get_super_power_level(self):
    return(self.super_power_level)

  def set_super_power_level(self):
    self.super_power_level = super_power_level

# ----------------------------------------------
class FlyingBot(SuperBot):

  def __init__(self, hover):
    self__.hover = hover

  def get_hover_distance(self):
    hover_distance = self.hover

  def set_hover_distance(self):
    self.hover = hover
# --------------------------------------------
