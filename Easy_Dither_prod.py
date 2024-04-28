# Computes a dither with a uniform delta T distribution
# Erellaz
# 2024-04-27
#______________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start = timer()



outfile=r"C:\Users\xxx\dither"
DTRange=500 # Delta T range in ms
DRange=DTRange/2 # Dither range in ms
size=100000 #size of the dither file (ie number of shots)
nbr_bins=100 # bins for histogram displays

DeltaT = np.random.uniform(-1*DTRange, DTRange,size*3)
plt.hist(DeltaT, bins=nbr_bins)
plt.title("Histogram of delta T from design")
plt.show()


D=np.zeros(size)

# This is quadratic
# from the first value we calculate the dither so that delta T belongs to the uniform distribution initially generated
# the trick is that we do not want the dither to escape the range, nor select on the delta T sample
# as it would skew the initial ditribution. 
for i in range(len(D)-1):
    j=0
    while j<len(DeltaT): 
        if abs(DeltaT[j]+D[i]) < DRange:
            D[i+1]=DeltaT[j]+D[i]
            DeltaT[j]=5*DTRange # mark that value as used
            j=2*len(DeltaT) # exit the while loop
        else:
            j+=1
 
D=np.trim_zeros(D)



plt.hist(D, bins=nbr_bins)
plt.title("Histogram of dither generated")
plt.show()

#Simulate acquistion
v=D[0:len(D)-1]-D[1:len(D)]


plt.hist(v, bins=nbr_bins)
plt.title("Histogram of Delta T from dither")
plt.show()

plt.plot(np.arange(0,len(v),1),v)
plt.title("Plot of Delta T")
plt.show()


plt.plot(DeltaT)
plt.title("How delta T array was used")
plt.show()

#______________________________________________________________________________
# Save the result
#in numpy array
np.save(outfile+"_np",D)

# in ORCA convention
orca_file = open(outfile+"_Peru_orca.txt", 'w')

for i in range(len(D)):
    l = "-1"+"     "+ str(int(D[i]))+"\n"
    orca_file.write(l)
 
orca_file.close()

end = timer()
print(end - start) # Time in seconds