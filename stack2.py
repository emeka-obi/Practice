from array_stack import ArrayStack as AS

Original = AS()
Fidelity = AS()
Helper = AS()

Original.push('JAMFX')
Original.push('FSELX')
Original.push('FOCPX')
Original.push('AFOIX')
Original.push('TEFQX')
Original.push('FSRPX')
Original.push('MSSMX')
Original.push('FSCSX')
Original.push('FSPTX')
Original.push('FCPGX')
Original.push('MACGX')
Original.push('JMCGX')
Original.push('FCVSX')
Original.push('NEXTX')
Original.push('BFOCX')
Original.push('BFGFX')
Original.push('ADNPX')
Original.push('FDSVX')
Original.push('FSAVX')
Original.push('FHKCX')
Original.push('SAGAX')
Original.push('FSEAX')
Original.push('CPOAX')
Original.push('FDCPX')
Original.push('FTRNX')
Original.push('FNCMX')
Original.push('FBGRX')
Original.push('FSMEX')




def func1(Original, Fidelity, Helper):
   for i in range(Original.__len__()):
       Helper.push(Original.pop())
   for i in range(Helper.__len__()):
     if Helper.top()[0] == 'F':
       Fidelity.push(Helper.pop())
     else:
       Original.push(Helper.pop())
     
   return ((Fidelity.top(), Fidelity.bottom()), (Original.top(), Original.bottom()))

if __name__ == "__main__":
  print(func1(Original, Fidelity, Helper))
  