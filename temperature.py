#Python program to convert from one temperature to another

#Imports
import pint 

print("""Your available options are: 
                                    1. Celsius
                                    2. Kelvin
                                    3.Farenheit
                                    4.Rankine""")
convert_from = input(""" Write your initial temp. scale: """).lower()

convert_to = input(" Write theCe temp. scale to convert to:").lower()

try:
      temperature = float(input("Enter your temperature: "))
except Exception as e:
      print("You have not entered a number", e)
def temperature_convert(temperature, convert_from, convert_to):
      units = pint.UnitRegistry()

      actual = units.Quantity(temperature, convert_from)
      answer = actual.to(convert_to)

      return answer.magnitude

final_answer = temperature_convert(temperature, convert_from, convert_to)
print(final_answer)