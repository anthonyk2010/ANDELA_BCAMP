try:
  def fizzBuzz(number):
    
    if (number <= 0):
      return "Number must be greater than zero"
    
    elif (number % 3 == 0 & number % 5 == 0):
      return 'FizzBuzz'
    
    elif(number % 5 == 0):
      return 'Buzz'
    
    elif (number % 3 == 0):
      return 'Fizz'

    else:
      return str(number)+(" is not a multiple of 3 or 5")
  print (fizzBuzz(number))
  print ("")

except ValueError:
  print ("")
  print ("Input is not a number. Please try again: ")