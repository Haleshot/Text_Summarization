# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pipeline_showcase.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QVBoxLayout,
    QSizePolicy, QWidget)

class Ui_pipeline(object):
    def setupUi(self, pipeline):
        if not pipeline.objectName():
            pipeline.setObjectName(u"pipeline")
        pipeline.resize(1200, 800)

        layout = QVBoxLayout()  # Use pipeline as the parent

        self.pipelineLabel = QLabel()
        self.pipelineLabel.setObjectName(u"pipelineLabel")
        self.pipelineLabel.setGeometry(QRect(110, 30, 1011, 611))
        layout.addWidget(self.pipelineLabel)
        
        
        self.pushButton = QPushButton()    
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 710, 251, 51))
        layout.addWidget(self.pushButton)
        
        # Set the layout for the QDialog
        pipeline.setLayout(layout)

        self.retranslateUi(pipeline)
        
        QMetaObject.connectSlotsByName(pipeline)

    # setupUi

    def retranslateUi(self, pipeline):
        pipeline.setWindowTitle(QCoreApplication.translate("pipeline", u"pipeline_showcase", None))
        self.pipelineLabel.setText("Something")
        self.pushButton.setText(QCoreApplication.translate("pipeline", u"Next", None))

        QMetaObject.connectSlotsByName(pipeline)

    # retranslateUi

