# Read and chack a dither from file
# Erellaz
# 2024-04-27

#______________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt


infile=r"C:\Users\xxxxxxx\dithersi625ms100k.npy"
nbr_bins=100


# Load and check dither
D=np.load(infile)
#D=1000.0*D #seconds to ms
plt.hist(D, bins=nbr_bins)
plt.title("Histogram of dither loaded from file")
plt.show()


v=D[0:len(D)-1]-D[1:len(D)]


plt.hist(v, bins=nbr_bins)
plt.title("Histogram of delta T")
plt.show()

plt.plot(np.arange(0,len(v),1),v)
plt.title("Plot of Delta T")
plt.show()

w=v[0:100]
plt.plot(np.arange(0,len(w),1),w)
plt.title("Plot of Delta T first 100 values")
plt.show()


#______________________________________________________________________________
# S = np.random.uniform(-1.0, 1.0,len(D))

# plt.hist(S, bins=nbr_bins)
# plt.title("Histogram of dither loaded from uniform law")
# plt.show()


# vu=S[0:len(S)-1]-S[1:len(S)]
# plt.hist(vu, bins=nbr_bins)
# plt.title("Histogram of delta T with uniform dither")
# plt.show()

