class chr_base(object):
	def __init__(self):
		super()

		self.hp = 20
		self.ac = 20
		self.speed = 30

		self.stats = {
			'hp':self.hp,
			'ac':self.ac,
			'speed':self.speed
		}

		self.buffs = []


	def addBuff(self, buff):
		# accepts buff dict su
		if buff.immediateEffect is not None:
			self.applyEffect(buff.immediateEffect)



	def stat(self, statName):
		stat = self.stats[statName]

		for b in self.buffs:
			if stat in b['statEffects'].keys():
				stat += b['statEffects'][statName]

		return stat


	# def applyEffect()














#to be moved
class buff_null(object):
	def __init__(self):
		super()

		self._imediateEffect = False
		self.statEffects = []


class effect_null(object):
	def __init__(self, target):
		self.target = target
		self.effectDict ={
			'hp':-3,
			'ac':0,
			'value':-1
		}

	def apply(self):
		for k in self.effectDict.keys():
			getter = getattr(self.target,k,None)
			setter = getattr(self.target,'set_{}'.format(k),None)

			if getter is None or setter is None:
				continue

			targetValue = getter()
			setter(targetValue + self.effectDict[k])
			




class myClass():
	def __init__(self):

		self._value = 20

		self.stats = {
			'value':self.value
		}

	def applyEffect(self, effect):
		effect(self).apply()

	def value(self):
		return self._value

	def set_value(self, value):
		self._value = value



if __name__ == '__main__':
	mc = myClass()
	print mc.value()
	mc.applyEffect(effect_null)
	print mc.value()
	mc.applyEffect(effect_null)
	print mc.value()	
