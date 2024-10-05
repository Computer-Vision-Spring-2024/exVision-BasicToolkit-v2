from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QComboBox,
    QDoubleSpinBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)


class FilterGroupBox(QGroupBox):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        self.filter_effect = None

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Noise Type
        filter_type_layout = QHBoxLayout()
        self.filter_type_label = QLabel("Filter Type")
        self.filter_type_comb = QComboBox()
        self.filter_type_comb.addItems(["Mean", "Median", "Gaussian"])
        self.filter_type_comb.currentIndexChanged.connect(self.update_filter_options)
        filter_type_layout.addWidget(self.filter_type_label)
        filter_type_layout.addWidget(self.filter_type_comb)

        # Kernel Size
        kernel_size_layout = QHBoxLayout()
        self.kernel_size_label = QLabel("Kernel Size")
        self.kernel_size_comb = QComboBox()
        self.kernel_size_comb.addItems(["3", "5", "7", "9"])
        kernel_size_layout.addWidget(self.kernel_size_label)
        kernel_size_layout.addWidget(self.kernel_size_comb)

        # Sigma
        self.sigma_layout = QHBoxLayout()  # Declare sigma layout here
        self.sigma_label = QLabel("Sigma")
        self.sigma_spinbox = QDoubleSpinBox()
        self.sigma_spinbox.setRange(1, 100)
        self.sigma_layout.addWidget(self.sigma_label)
        self.sigma_layout.addWidget(self.sigma_spinbox)

        main_layout.addLayout(filter_type_layout)
        main_layout.addLayout(kernel_size_layout)
        main_layout.addLayout(self.sigma_layout)  # Add sigma layout to main layout

        self.setLayout(main_layout)

        self.update_filter_options(0)  # Set default options for Uniform noise

    def update_filter_options(self, index):
        if index == 2:  # Gaussian
            self.sigma_spinbox.setVisible(True)
            self.sigma_label.setVisible(True)
        else:  # Mean or Median
            self.sigma_spinbox.setVisible(False)
            self.sigma_label.setVisible(False)
