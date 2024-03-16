import matplotlib.colors as mcolors
import numpy as np
from Classes.EffectsWidgets.EdgeDetectorGroupBox import EdgeDetectorGroupBox
from Classes.ExtendedWidgets.DoubleClickPushButton import QDoubleClickPushButton
from PyQt5.QtCore import pyqtSignal


class EdgeDetector(QDoubleClickPushButton):
    _instance_counter = 0
    attributes_updated = pyqtSignal(np.ndarray)

    def __init__(self, mainwindow, parent=None, *args, **kwargs):
        super(EdgeDetector, self).__init__(parent)
        self.ui = mainwindow
        # For naming the instances of the effect
        EdgeDetector._instance_counter += 1
        self.title = f"Edge Detector.{EdgeDetector._instance_counter:03d}"
        self.setText(self.title)  # Set the text of the button to its title
        # Attributes
        self.lookup = {
            "sobel_3x3": self.sobel_3x3,
            "sobel_5x5": self.sobel_5x5,
            "roberts": self.roberts,
            "prewitt": self.prewitt,
            "laplacian": self.laplacian,
            "canny": self.canny,
        }
        self.current_image = None
        self.current_working_image = None  # this represents the current image on which we will perform all operations
        self.current_detector_type = "sobel_3x3"
        self.edged_image = None

        self.edge_widget = EdgeDetectorGroupBox(self.title)
        # Pass the NoiseGroupBox instance to the Noise class
        self.edge_widget.edge_effect = self

        self.edge_widget.edge_widget_combo_box.currentTextChanged.connect(
            self.update_detector_type
        )

        # Store the attributes of the effect to be easily stored in the images instances.
        self.attributes = self.attributes_dictionary()

    # Setters
    def attributes_dictionary(self):
        """
        Description:
            - Returns a dictionary containing the attributes of the effect.
        """
        return {
            # "edge detector type": self.current_edge_detector,
            "edge detector type": self.current_detector_type,
            "groupbox": self.edge_widget,
        }

    # Methods
    def update_detector_type(self):
        self.current_detector_type = (
            self.edge_widget.edge_widget_combo_box.currentText()
        )
        self.apply_detector()
        self.display_image()

    def set_working_image(self, image):
        self.current_image = image  # assign regradless it's colored or grayscale image
        if (
            len(image.shape) == 3
        ):  # if colored, make sure it's converted into grayscale.
            image = self.to_grayscale(image)
        self.current_working_image = image

    def display_image(self):
        """
        Description:
            - Displays an image in the main canvas.

        Args:
            - input_img: The input image to be displayed.
            - output_img: The output image to be displayed.
        """
        # Clear the previous plot
        self.ui.main_viewport_figure_canvas.figure.clear()

        # Determine layout based on image dimensions
        height, width, _ = self.current_image.shape
        if width > height:  # If width is greater than the height
            ax1 = self.ui.main_viewport_figure_canvas.figure.add_subplot(
                211
            )  # Vertical layout
            ax2 = self.ui.main_viewport_figure_canvas.figure.add_subplot(212)
        else:  # If height is significantly greater than width
            ax1 = self.ui.main_viewport_figure_canvas.figure.add_subplot(
                121
            )  # Horizontal layout
            ax2 = self.ui.main_viewport_figure_canvas.figure.add_subplot(122)

        ax1.imshow(self.current_image, cmap="gray")
        ax1.axis("off")
        ax1.set_title("Input Image", color="white")

        ax2.imshow(self.edged_image, cmap="gray")
        ax2.axis("off")
        ax2.set_title("Output Image", color="white")

    def to_grayscale(self, image):
        """
        Descripion:
            - Convert an image to grayscale by averaging the red, green, and blue channels for each pixel.

        Parameters:
        - image: numpy.ndarray
            The input image.

        Returns:
        - numpy.ndarray
            The grayscale image.
        """
        grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
        return grayscale_image

    def apply_detector(self):
        output_image = self.lookup[self.current_detector_type](
            self.current_working_image
        )
        if len(output_image) == 2:
            output_image = self.get_directed_image(
                output_image
            )  # if the output contains directionality list, then include it in the plotting.
        self.edged_image = output_image

    def get_directed_image(self, image):
        """
        Descripion:
            - return rgb image that contians directionality info.

        Parameters:
        - image (tuple of numpy.ndarray ): the first array contains magnitude of edges, the second contains the gradient direction.

        Returns:
        - numpy.ndarray
            rgb image.
        """
        mag = image[0]
        direction = image[1]
        direction_normalized = direction / np.pi
        image_shape = image[0].shape
        hue = direction_normalized * 360
        hsv_image = np.zeros((image_shape[0], image_shape[1], 3), dtype=np.uint8)
        hsv_image[..., 0] = hue.astype(np.uint8)
        hsv_image[..., 1] = mag.astype(np.uint8)
        hsv_image[..., 2] = mag.astype(np.uint8)
        rgb_image = mcolors.hsv_to_rgb(hsv_image / 255)
        return rgb_image

    def padding_image(self, image, width, height, pad_size):
        padded_image = np.zeros((height + 2 * pad_size, width + 2 * pad_size))
        padded_image[pad_size:-pad_size, pad_size:-pad_size] = image
        return padded_image

    def convolve_2d(self, image, kernel, mutlipy=True):
        image_height, image_width = image.shape
        kernel_size = kernel.shape[0]

        pad_size = kernel_size // 2

        if pad_size == 0:
            padded_image = image
            normalize_value = 2
        else:
            # padding the image to include edges
            normalize_value = kernel_size * kernel_size
            padded_image = self.padding_image(
                image, image_width, image_height, pad_size
            )

        output_image = np.zeros_like(image)

        for i in range(image_height):
            for j in range(image_width):
                neighborhood = padded_image[
                    i : i + kernel_size, j : j + kernel_size
                ]  # slice out the region
                # optimization trick
                if mutlipy:
                    output_image[i, j] = np.sum(neighborhood * kernel)
                else:
                    output_image[i, j] = np.sum(neighborhood) * (1 / normalize_value)
        return np.clip(output_image, 0, 255)

    def compute_gradient_using_convolution(self, image, x_kernel, y_kernel, cart_coord):
        x_component = self.convolve_2d(image, x_kernel)
        y_component = self.convolve_2d(image, y_kernel)
        resultant = np.abs(x_component) + abs(y_component)
        resultant = resultant / np.max(resultant) * 255
        direction = np.arctan2(y_component, x_component)
        if not cart_coord:
            direction = (direction + np.pi / 4) % np.pi  # Wrap angles back to [0, π]
        return (resultant, direction)

    def get_edges_using_convolution(self, image, x_kernel, y_kernel, cart_coord=True):
        edged_image = self.compute_gradient_using_convolution(
            image, x_kernel, y_kernel, cart_coord
        )
        return edged_image

    def sobel_3x3(self, image):
        dI_dX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        dI_dY = np.rot90(dI_dX)
        return self.get_edges_using_convolution(image, dI_dX, dI_dY)

    def sobel_5x5(self, image):
        dI_dX = np.array(
            [
                [-1, -2, 0, 2, 1],
                [-2, -3, 0, 3, 2],
                [-3, -5, 0, 5, 3],
                [-1, -2, 0, 2, 1],
                [-2, -3, 0, 3, 2],
            ]
        )
        dI_dY = np.rot90(dI_dX)
        return self.get_edges_using_convolution(image, dI_dX, dI_dY)

    def roberts(self, image):
        secondary_diag = np.array([[0, 1], [-1, 0]])
        main_diag = np.rot90(secondary_diag)
        return self.get_edges_using_convolution(image, secondary_diag, main_diag, False)

    def prewitt(self, image):
        dI_dX = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        dI_dY = np.rot90(dI_dX)
        return self.get_edges_using_convolution(image, dI_dX, dI_dY)

    def laplacian(self, image):
        kernel = np.array([[1, 4, 1], [4, -20, 4], [1, 4, 1]])
        edged_image = self.convolve_2d(image, kernel, True)
        return edged_image

    def non_maximum_suppression(self, magnitude, direction):
        image_height, image_width = magnitude.shape
        suppressed_image = np.zeros((image_height, image_width), dtype=np.uint8)
        angles = direction * 180 / np.pi
        angles[angles < 0] += 180

        for i in range(1, image_height - 1):
            for j in range(1, image_width - 1):
                q, r = 255, 255

                if (0 <= angles[i, j] < 22.5) or (157.5 <= angles[i, j] <= 180):
                    r = magnitude[i, j - 1]
                    q = magnitude[i, j + 1]

                elif 22.5 <= angles[i, j] < 67.5:
                    r = magnitude[i - 1, j + 1]
                    q = magnitude[i + 1, j - 1]

                elif 67.5 <= angles[i, j] < 112.5:
                    r = magnitude[i - 1, j]
                    q = magnitude[i + 1, j]

                elif 112.5 <= angles[i, j] < 157.5:
                    r = magnitude[i + 1, j + 1]
                    q = magnitude[i - 1, j - 1]

                if (magnitude[i, j] >= q) and (magnitude[i, j] >= r):
                    suppressed_image[i, j] = magnitude[i, j]
                else:
                    suppressed_image[i, j] = 0

        return suppressed_image

    def threshold(self, img, lowThresholdRatio=0.05, highThresholdRatio=0.2):

        highThreshold = img.max() * highThresholdRatio
        lowThreshold = highThreshold * lowThresholdRatio

        image_height, image_width = img.shape
        res = np.zeros((image_height, image_width), dtype=np.int32)

        weak = np.int32(25)
        strong = np.int32(255)

        strong_i, strong_j = np.where(img >= highThreshold)
        zeros_i, zeros_j = np.where(img < lowThreshold)  # left zeros

        weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

        res[strong_i, strong_j] = strong
        res[weak_i, weak_j] = weak

        return (res, weak, strong)

    def hysteresis(self, img, weak, strong=255):
        image_height, image_width = img.shape

        for i in range(1, image_height - 1):
            for j in range(1, image_width - 1):
                if (
                    img[i, j] == weak
                ):  # these weak edges are considered to be strong, if they are connected to strong edges
                    if (
                        (img[i + 1, j - 1] == strong)
                        or (img[i + 1, j] == strong)
                        or (img[i + 1, j + 1] == strong)
                        or (img[i, j - 1] == strong)
                        or (img[i, j + 1] == strong)
                        or (img[i - 1, j - 1] == strong)
                        or (img[i - 1, j] == strong)
                        or (img[i - 1, j + 1] == strong)
                    ):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
        return img

    def canny(self, image):
        edged_image = self.sobel_3x3(image)
        suppressed_image = self.non_maximum_suppression(edged_image[0], edged_image[1])
        thresholded_image_info = self.threshold(suppressed_image)
        output_image = self.hysteresis(*thresholded_image_info)
        return output_image
