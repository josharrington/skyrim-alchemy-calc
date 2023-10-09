#http://www.uesp.net/wiki/Skyrim:Alchemy_Effects

from math import floor

def getValue(ings, effects):
	durationMods = []
	magnitudeMods = []
	valueMods = []
	values = []

	#TODO: Make sure mods only add factor for effects that exist here
	#Verify mag, dur and value multipliers
	#Verify effect values
	for ing in ings:
		for effect in ing["effects"]:
			if effect.find(";") > -1:
				factor = test.split(";")[1]
				mod = factor[-1]
				factor = factor[:-1]
				if mod == "x":
					magnitudeMods.append(float(factor))
				elif mod == "d":
					durationMods.append(float(factor))
				elif mod == "v":
					valueMods.append(float(factor))

	for effect in effects:
		if not effect["fixedMagnitude"]:
			effect["calcedMag"] = effect["baseMagnitude"] * 4 * 1.5
		else:
			effect["calcedMag"] = effect["baseMagnitude"]

		if not effect["fixedDuration"]:
			effect["calcedDur"] = effect["baseDuration"]
		else:
			effect["calcedDur"] = effect["baseDuration"]
		
		if effect["calcedMag"] == 0:
			floor(effect["baseCost"] * 0.0794328 * effect["calcedDur"])
