#This is an assignment to dispaly my Prowess
#Pad Foundation Designer 0.12

class Pad(name):

    def __init__(self, name):
        self.name = "Untitled"
        pass#pathetic nothing to put here
       
        
    def weight(self, Gk, Qk, depth):
        # lets use more definations
        service_load = Gk*(1.3) + Qk# the 0.3 increase is a result of footings wieght
        required_size = service_load / float(bearing_pressure)# these should give you area so i convert the area to lenght
        #the footings size
        dimension = ((required_size**(0.5)) + 0.5)**(0.5)# assumed this is a square footing 
        #checking for the assumed base weight
        if dimension**2 < (0.3) * Gk: #then we're good #*#* Perhaps i should use a try and except, except i dont see any error
            self.analysis(Gk, Qk, bearing_pressure, dimension, depth)
        else: # this occurs when 0.3 Gk is not enough to counter the footings wieght
            actual_wieght = dimension**2 * Fcu * depth
            gk = Gk + actual_wieght
            #checking again
            load = gk + Qk
            size = load / bearing_pressure
            dimension = ((size**(0.5)) + 0.5)**(0.5)
            self.analysis(Gk, Qk, bearing_pressure, dimension, depth)

    def analysis(self, Gk, Qk, bearing_pressure, dimension, depth): #Observe the depth the default value is 600
        #bending moment
        design_load = (1.4)*Gk + (1.6)*Qk
        m = 0.156 * int(Fcu) * 1000 * (depth**2)# m is the ultimate moment of the design

        M = (design_load * (dimension**2) ) / 2 # M is the design moment
        if M >= m:#that is the ultimate moment is less than the design moment:
            pass#there is an error here
            # the idea now is to design for compression reinforcements
        else:
            k = (M * (10**6)) / 0.156 * int(Fcu) * 1000 * (depth**2)
            # found K, for this case i assumed that there is no need for compression reinforcements
            z = depth * (0.5  + (0.25 + (k / 0.9))**(0.5) )
            # now am supposed to check for something which i have ignored
            As = (M * (10**6))/ (0.87 * int(Fy) * z)
            #this is the area of steel required
        self.design(depth, int(column_size), dimension, bearing_pressure)
        return As# this will return where the value actually is, not to print this to screen
    
    def design(self, depth, column_size , dimension, bearing_pressure):
        # it would be much wiser if i actually split this into as mqny defs as  possible
        #punching shear
        critical_perimeter = (column_size + (8 + (1.5 * depth)))
        critical_area = ((column_size**(0.5)) + 3*depth)**2
        V = ((dimension**2) - critical_area) * float(bearing_pressure)  #load non-critical area
        v = V / (critical_perimeter * depth) # it is common practise to not use stupid varable names like these ones
        #need a dictionary to check for punching shear
        return v

#declarations
# i think all this should be taken care of in the view file

print("Make all inputs using standard units of kN/m")
Gk = input("Input Dead load, Gk\n")
Qk = input("Input Live Load, Qk \n")# imagine there are more than one live load. Doom!
column_size = input("Input Column Area \n")#what if this is not square?, need elaboration, area is what i used here
bearing_pressure = input("Input allowable soil Bearing pressure \n")
raw = input("Input Pad depth \n Enter 0 for default \n")
if int(raw) == 0:
    depth = 600
else:
    depth = int(raw)
print("Depth set to default 600mm")
Fcu = input("Input concrete strenght in N/mm \n")
Fy = input("Input Steel strenght in N/mm \n")

Pad().weight(float(Gk), float(Qk), int(depth))
"""
print assumed footing thickness
remember to print required plan base
line 46
line 56-57
line 64
there are many units error check again
print v
"""
