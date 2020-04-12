import sys
from pytube import YouTube

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog

# global OutputdirectoryName

if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    w.setWindowTitle("YouTube Download")
    VideoUrl = QLabel(w)
    VideoUrl.setText('videoURL')
    InputText = QLineEdit(w)
    DownloadButton = QPushButton(w)
    DownloadButton.setText('Download')

    # Second Group Inputs
    Outputlabel = QLabel(w)
    Outputlabel.setText('Output Directory')
    Outputinput = QLineEdit(w)
    BrowseButton = QPushButton(w)
    BrowseButton.setText('Browse')

    # First Group
    hbox = QHBoxLayout()
    hbox.addWidget(VideoUrl)
    hbox.addWidget(InputText)
    hbox.addWidget(DownloadButton)
    hbox.setContentsMargins(0, 0, 0, -1)
    # hbox.setSpacing(0)

    # Second Group
    hbox1 = QHBoxLayout()
    hbox1.addWidget(Outputlabel)
    hbox1.addWidget(Outputinput)
    hbox1.addWidget(BrowseButton)
    hbox1.setContentsMargins(0, -1000, 0, -1)

    vbox = QVBoxLayout()
    # vbox.setContentsMargins(-1, 0, -1, -1)
    vbox.addLayout(hbox)
    vbox.addLayout(hbox1)
    w.setLayout(vbox)


def OpenDirectory():
    global OutputdirectoryName
    OutputdirectoryName = QFileDialog().getExistingDirectory()
    Outputinput.setText(OutputdirectoryName)
    # print(OutputdirectoryName)


def clickMethod():
    # print("You clicked PushButton")
    YouTubeURL = InputText.text()

    def show_progress_bar(self, chunk, bytes_remaining):
        progress = round((1 - bytes_remaining / self.filesize) * 100, 2), '% done...'
        print(progress)

    output = QLabel(w)
    if YouTubeURL == '':
        output.setText('Please Enter the Youtube URL')
        output.setFixedWidth(330)
        output.move(200, 300)
        output.show()
    else:
        # print(OutputdirectoryName)
        # # print("else")
        yt = YouTube(YouTubeURL)
        yt.register_on_progress_callback(show_progress_bar)
        yt = yt.streams.first()
        yt.download(OutputdirectoryName)
        output.setText('Download Completed')
        output.move(150, 150)
        output.show()


DownloadButton.clicked.connect(clickMethod)
BrowseButton.clicked.connect(OpenDirectory)

w.resize(700, 500)

w.show()
sys.exit(app.exec_())
