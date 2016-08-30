import numpy as np
from scipy import signal
from scipy.io import wavfile

from sklearn.decomposition import FastICA, PCA

X = wavfile.read('abcd.wav')[1]
X = X.reshape(-1, 1)

# Compute ICA
ica = FastICA()
S_ = ica.fit_transform(X)  # Reconstruct signals
A_ = ica.mixing_  # Get estimated mixing matrix

wavfile.write('ica.wav',44100,S_.reshape(1,-1)[0])
# We can `prove` that the ICA model applies by reverting the unmixing.
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# For comparison, compute PCA
pca = PCA()
H = pca.fit_transform(X)  # Reconstruct signals based on orthogonal components
wavfile.write('pca.wav',44100,H.reshape(1,-1)[0])
