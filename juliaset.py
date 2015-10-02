class JuliaSet():
    
    def __init__(self, c, n=100): # This is the data for the class - 
        self.c = c     
        self.n = n
        self._d = 0.001
        self.set = [ ]
        self._complexplane = [ ]
    
    def juliamap(self, z) : # This is the method for the class 
        return (z**2 + self.c)
    

    def  iterate(self, z):  # This is the method for the class
        m = 0
        while True:
            z = self.juliamap(z)
            m = m+1
            if abs(z) > 2 :
                return(m)
            elif m >= self.n :
                return(0)

            
    def create_complexplane(self,d) :
        list1 = [ ]
        i = -2.0
        while i <= 2.0 :
            j = -2.0
            while j <= 2.0 :
                list1.append(complex(i,j))
                j = j+d
            i = i+d
        return list1   
    

    def set_spacing(self, d) : # This is the method for the class 
        self._d = d
        self._complexplane = self.create_complexplane(self._d)
        #print self._complexplane  # to troubleshoot the code
   
    def generate(self) :
        self.set_spacing(self._d)
        for complex_number in self._complexplane:
             self.set.append(self.iterate(complex_number))
        return self.set

    
