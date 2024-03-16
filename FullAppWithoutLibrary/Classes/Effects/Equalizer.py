import numpy as np
from Classes.ExtendedWidgets.DoubleClickPushButton import QDoubleClickPushButton
from HelperFunctions import Histogram_computation
from PyQt5.QtCore import pyqtSignal


class Equalizer(QDoubleClickPushButton):
    attributes_updated = pyqtSignal(np.ndarray)

    def __init__(self, imageData, parent=None, *args, **kwargs):
        super(Equalizer, self).__init__(parent)

        self.title = "Equalizer"
        self.setText(self.title)  # Set the text of the button to its title

        # Attributes
        self.image = imageData

    # Methods
    def cumulative_summation(self, _2d_hist: np.ndarray) -> np.ndarray:
        """
        Description:
            - Compute the cumulative sum of a 2D array.

        Parameters:
            - _2d_hist (np.ndarray): The input 2D frequency distribution array.

        Returns:
            - np.ndarray: The output 2D array after cumulative summation.
        """

        # Initialize a zero array with the same shape as the input
        _2d_cdf = np.zeros(_2d_hist.shape)

        # Set the first element of the cumulative sum array to be the first element of the input array
        _2d_cdf[0] = _2d_hist[0]

        # Iterate over the input array, adding each element to the cumulative sum
        for ind in range(1, _2d_hist.shape[0]):
            _2d_cdf[ind] = _2d_cdf[ind - 1] + _2d_hist[ind]

        return _2d_cdf

    def General_Histogram_Equalization(self):
        """
        Perform histogram equalization on a given image channel.

        Parameters:
        channel (np.ndarray): The input image channel. it's a 2D array where each element contains spicific greyscale (or L channel) value.

        Returns:
        np.ndarray: The output image channel after histogram equalization to be merged (if it's a colored image)
        with the other channels to produce the outpub contrast-enhanced image.
        """
        # Calculate histogram of the input channel
        hist = Histogram_computation(self.image, 0)

        # Calculate cumulative distribution function (CDF) of the histogram
        cdf = self.cumulative_summation(hist)

        # Normalize the CDF
        cdf_normalized = cdf * hist.max() / cdf.max()

        # Mask all pixels in the CDF with '0' intensity
        cdf_masked = np.ma.masked_equal(cdf_normalized, 0)

        # Equalize the histogram by scaling the CDF
        cdf_masked = (
            (cdf_masked - cdf_masked.min())
            * 255
            / (cdf_masked.max() - cdf_masked.min())
        )

        # Fill masked pixels with '0'
        cdf = np.ma.filled(cdf_masked, 0).astype("uint8")

        # Apply the equalization to the original image channel
        # To clarify, now cdf contains the equalized values and need to be placed at the correct indices
        # Each value in the channel changes to its equivalent value from cdf
        channel_eq = cdf[self.image]

        return channel_eq
