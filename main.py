import os
import sys
import time
from random import shuffle

from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QFrame, QComboBox, QLineEdit, QLabel, QListWidget, QSlider, \
    QPushButton, QMessageBox, QWidget
from self import self


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(0, 0, 1920, 1020)

        # Set the frameless window hint
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set windows icon
        self.setWindowIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/windows icon.png'))

        # Create a title bar frame.
        self.title_bar_frame = QFrame(self)
        self.title_bar_frame.setGeometry(0, 0, 1920, 60)
        self.title_bar_frame.setStyleSheet("background-color: #1b1c1b; border-bottom: 1px solid white")
        self.title_bar_frame.show()

        # Create a title bar icon on the left side of the title bar frame. Height = 60px
        self.title_bar_icon = QLabel(self.title_bar_frame)
        self.title_bar_icon.setGeometry(20, 0, 60, 60)
        self.title_bar_icon.setPixmap(
            QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/music.png').pixmap(60, 60))
        self.title_bar_icon.show()

        # Insert a title bar label on the right side of the icon. Height = 60px
        self.title_bar_label = QLabel(self.title_bar_frame)
        self.title_bar_label.setGeometry(55, 0, 1820, 60)
        self.title_bar_label.setStyleSheet("color: white; font-size: 18px; font-family: Helvetica; font-weight: bold;")
        self.title_bar_label.setText("Desktop Music Player")
        self.title_bar_label.show()

        # Create a top level frame. Height = 40px
        self.top_frame = QFrame(self)
        self.top_frame.setGeometry(0, 60, 1920, 80)
        self.top_frame.setStyleSheet("background-color: #282733")
        self.top_frame.show()

        # Insert a combobox on the left  side of the top frame. Only a-z and z-a sorting
        self.combobox = QComboBox(self.top_frame)
        self.combobox.setGeometry(20, 24, 65, 30)
        self.combobox.setFocusPolicy(False)
        self.combobox.setStyleSheet("color: white; font-size: 20px; font-family: Helvetica;")
        self.combobox.addItem("a-z")
        self.combobox.addItem("z-a")
        self.combobox.show()

        # Insert a song label frame on the right side of the combobox. Height = 40px
        self.song_label_frame = QFrame(self.top_frame)
        self.song_label_frame.setGeometry(105, 20, 1165, 40)
        self.song_label_frame.show()

        # Insert a song label inside the song label frame. Height = 40px
        self.song_label = QLabel(self.song_label_frame)
        self.song_label.setGeometry(0, 0, 1165, 40)
        self.song_label.setStyleSheet("color: white; font-size: 20px; font-family: Helvetica; font-weight: bold;")
        self.song_label.setAlignment(Qt.AlignCenter)
        self.song_label.show()

        # Insert a q line edit on the right side of the song label frame. Height = 40px
        self.search_bar = QFrame(self.top_frame)
        self.search_bar = QLineEdit(self.top_frame)
        self.search_bar.setGeometry(1320, 20, 580, 40)
        self.search_bar.setStyleSheet(
            "background-color: white; font-size: 17px; font-family: Helvetica; border-radius: 5px; font-weight: bold;")
        self.search_bar.setPlaceholderText("Search")
        self.search_bar.show()

        # Create a list frame. Height = 906px
        self.list_frame = QFrame(self)
        self.list_frame.setGeometry(0, 140, 1920, 780)
        self.list_frame.setStyleSheet("background-color: #353445")
        self.list_frame.show()

        # Create a list widget inside the list frame. Add spaces from the list widget frame to the list widget edges. Height = 780px (40px from the top frame and 40px from the bottom frame)
        self.list_widget = QListWidget(self.list_frame)
        self.list_widget.setGeometry(15, 15, 1890, 760)
        self.list_widget.setStyleSheet(
            "background-color: #353445; color: white; font-size: 20px; font-family: Helvetica;")
        self.list_widget.setFrameShape(QFrame.NoFrame)
        self.list_widget.setSpacing(5)
        # Remove scroll bar from the list widget
        self.list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_widget.show()

        # Create a bottom frame. Height = 100px
        self.bottom_frame = QFrame(self)
        self.bottom_frame.setGeometry(0, 920, 1920, 100)
        self.bottom_frame.setStyleSheet("background-color: #1b1c1b")
        self.bottom_frame.show()

        # Insert a scale slider inside the top of the bottom frame. Height = 40px
        self.song_slider = QFrame(self.bottom_frame)
        self.song_slider = QSlider(Qt.Horizontal, self.bottom_frame)
        self.song_slider.setGeometry(145, 9, 1625, 20)
        self.song_slider.setRange(0, 100)
        self.song_slider.show()

        # Insert a current time label on the left side of the scale slider. Height = 40px
        self.current_time_label = QLabel(self.bottom_frame)
        self.current_time_label.setGeometry(40, -3, 100, 40)
        self.current_time_label.setStyleSheet("color: white; font-size: 17px; font-family: Helvetica;")
        self.current_time_label.setText("00:00:00")
        self.current_time_label.show()

        # Insert a total time label on the right side of the scale slider. Height = 40px
        self.total_time_label = QLabel(self.bottom_frame)
        self.total_time_label.setGeometry(1810, -3, 100, 40)
        self.total_time_label.setStyleSheet("color: white; font-size: 17px; font-family: Helvetica;")
        self.total_time_label.setText("00:00:00")
        self.total_time_label.show()

        # Insert a shuffle png image make it a button under the scale slider. Change the bg color when clicked, remove the bg color when clicked again. Use other algorithm to do the button click toggle
        self.shuffle_button = QPushButton(self.bottom_frame)
        self.shuffle_button.setGeometry(840, 40, 40, 40)
        self.shuffle_button.setToolTip("Shuffle Songs")
        self.shuffle_button.setStyleSheet("border: none")
        self.shuffle_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/shuffle.png'))
        self.shuffle_button.setCheckable(True)
        self.shuffle_button.clicked.connect(lambda: self.shuffle_button.setStyleSheet(
            "background-color: #f28ca8; border: none;" if self.shuffle_button.isChecked() else "background-color: transparent; border: none"))
        self.shuffle_button.show()

        # Insert a previous png image make it a button under the scale slider. Change the bg color when clicked, remove the bg color when clicked again. Use other algorithm to do the button click toggle
        self.previous_button = QPushButton(self.bottom_frame)
        self.previous_button.setGeometry(890, 40, 40, 40)
        self.previous_button.setToolTip("Previous Song")
        self.previous_button.setStyleSheet("border: none")
        self.previous_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/previous.png'))
        self.previous_button.show()

        # Make a play and pause toggle button using two png images.
        self.play_pause_button = QPushButton(self.bottom_frame)
        self.play_pause_button.setGeometry(940, 40, 40, 40)
        self.play_pause_button.setToolTip("Play/Pause Song")
        self.play_pause_button.setStyleSheet("border: none")
        self.play_pause_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/play.png'))
        # Set the button to check able
        self.play_pause_button.setCheckable(True)
        # If the button is checked, set the image to pause.png, if not set the image to play.png
        self.play_pause_button.clicked.connect(lambda: self.play_pause_button.setIcon(
            QIcon(
                'C:/Users/63939/PycharmProjects/Desktop Music Player/images/play.png')) if self.play_pause_button.isChecked() else self.play_pause_button.setIcon(
            QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/pause.png')))
        self.play_pause_button.show()

        # Insert a next png image make it a button under the scale slider. Do not  set the bg color permanently. Just change the bg color when clicked, remove it after a second
        self.next_button = QPushButton(self.bottom_frame)
        self.next_button.setGeometry(990, 40, 40, 40)
        self.next_button.setToolTip("Next Song")
        self.next_button.setStyleSheet("border: none")
        self.next_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/next.png'))
        self.next_button.show()

        # Insert a repeat png image make it a button under the scale slider.
        self.repeat_button = QPushButton(self.bottom_frame)
        self.repeat_button.setGeometry(1040, 40, 40, 40)
        self.repeat_button.setToolTip("Repeat Song")
        self.repeat_button.setStyleSheet("border: none")
        self.repeat_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/repeat.png'))
        # Set the button to check able
        self.repeat_button.setCheckable(True)
        # If the button is checked, set the bg color to blue, if not remove the bg color
        self.repeat_button.clicked.connect(lambda: self.repeat_button.setStyleSheet(
            "background-color: #ffb600; border: none" if self.repeat_button.isChecked() else "background-color: transparent; border: none"))
        self.repeat_button.show()

        # Insert a volume png image make it a button under the scale slider. Change the bg color when clicked, remove the bg color when clicked again. Use other algorithm to do the button click toggle
        self.volume_button = QPushButton(self.bottom_frame)
        self.volume_button.setGeometry(139, 38, 40, 40)
        self.volume_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/volume.png'))
        self.volume_button.setToolTip("Volume")
        self.volume_button.setStyleSheet("border: none")
        self.volume_button.show()

        # Insert a volume slider under the volume button. Hide it first and show it when the volume button is clicked
        self.volume_slider = QSlider(Qt.Horizontal, self.bottom_frame)
        self.volume_slider.setGeometry(180, 51, 400, 15)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.show()

        # Insert a volume slider value label under the volume slider. Hide it first and show it when the volume button is clicked
        self.volume_slider_value_label = QLabel(self.bottom_frame)
        self.volume_slider_value_label.setGeometry(590, 38, 100, 40)
        self.volume_slider_value_label.setStyleSheet("color: white; font-size: 15px; font-family: Helvetica;")
        self.volume_slider_value_label.show()

        # Insert a refresh png image and make it a button
        self.refresh_button = QPushButton(self.bottom_frame)
        self.refresh_button.setGeometry(1560, 38, 40, 40)
        self.refresh_button.setToolTip("Refresh")
        self.refresh_button.setStyleSheet("border: none")
        self.refresh_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/refresh.png'))
        self.refresh_button.show()

        # Insert a stop png image make it a button under the scale slider. Change the bg color when clicked, remove the bg color when clicked again. Use other algorithm to do the button click toggle
        self.stop_button = QPushButton(self.bottom_frame)
        self.stop_button.setGeometry(1620, 38, 40, 40)
        self.stop_button.setToolTip("Stop Song")
        self.stop_button.setStyleSheet("border: none")
        self.stop_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/stop-button.png'))
        self.stop_button.show()

        # Insert a delete png image make it a button under the scale slider. Change the bg color when clicked, remove the bg color when clicked again. Use other algorithm to do the button click toggle
        self.delete_button = QPushButton(self.bottom_frame)
        self.delete_button.setGeometry(1680, 38, 40, 40)
        self.delete_button.setToolTip("Delete Song")
        self.delete_button.setStyleSheet("border: none")
        self.delete_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/bin.png'))
        self.delete_button.show()

        # Insert an exit png image make it a button under the scale slider. Change the bg color when clicked, remove the bg color when clicked again. Use other algorithm to do the button click toggle
        self.exit_button = QPushButton(self.bottom_frame)
        self.exit_button.setGeometry(1739, 38, 40, 40)
        self.exit_button.setToolTip("Exit")
        self.exit_button.setStyleSheet("border: none")
        self.exit_button.setIcon(
            QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/sign-out-option.png'))
        self.exit_button.show()

        # Load songs from the directory
        self.load_songs()

        # Create a media player object
        self.media_player = QMediaPlayer()

        # Call the play_song function when the list widget item is clicked
        self.list_widget.itemClicked.connect(self.play_song)

        # Connect the mediaStatusChanged signal to the handle_media_status_changed method
        self.media_player.mediaStatusChanged.connect(self.handle_media_status_changed)

        # Slider timer
        self.timer = QTimer(self)
        # Call the move slider function every second
        self.timer.start(1000)
        # Call the move slider function when the timer times out
        self.timer.timeout.connect(self.move_slider)
        # Call the move slider function when the slider is moved
        self.song_slider.sliderMoved['int'].connect(lambda: self.media_player.setPosition(self.song_slider.value()))

        # Call the stop_song function when the stop button is clicked
        self.stop_button.clicked.connect(self.stop_song)

        # Call the delete_song function when the delete button is clicked
        self.delete_button.clicked.connect(self.delete_song)

        # Call the exit function when the exit button is clicked
        self.exit_button.clicked.connect(self.close)

        # Call the volume slider value function when the volume slider is moved
        self.volume_slider.sliderMoved['int'].connect(self.volume_slider_value)

        # Call the sort songs function when the combobox item is clicked
        self.combobox.currentIndexChanged.connect(self.sort_songs)

        # Call the search song function when the search bar text is changed
        self.search_bar.textChanged.connect(self.search_song)

        # Call the next song function when the next button is clicked
        self.next_button.clicked.connect(self.next_song)

        # Call the previous song function when the previous button is clicked
        self.previous_button.clicked.connect(self.previous_song)

        # Hide total time label when the song was stopped and bring it back when song was selected again
        self.total_time_label.hide()
        self.list_widget.itemClicked.connect(lambda: self.total_time_label.show())

        # Hide current time label when the song was stopped and bring it back when song was selected again
        self.current_time_label.hide()
        self.list_widget.itemClicked.connect(lambda: self.current_time_label.show())

        # Insert a repeat_mode variable to track whether repeat is enabled or not
        self.repeat_mode = False
        # Connect the repeat button to the repeat_button_clicked method
        self.repeat_button.clicked.connect(self.repeat_button_clicked)

        # Connect the shuffle button to the shuffle_songs method
        self.shuffle_button.clicked.connect(self.shuffle_songs)
        # Create an instance variable to store the shuffled songs
        self.shuffled_songs = []
        # Set the current song index to 0
        self.current_song_index = 0

        # Connect the refresh button to the refresh_songs method
        self.refresh_button.clicked.connect(self.refresh_songs)

    # Define a method to load songs from a specified directory
    def load_songs(self):
        # Set the directory path where the music files are stored
        directory = "C:/Users/63939/Music"
        # Get a list of song filenames in the specified directory
        songs = os.listdir(directory)
        # Add the list of songs to a QListWidget
        self.list_widget.addItems(songs)
        # Connect the itemClicked signal to update the displayed song label
        self.list_widget.itemClicked.connect(
            lambda: self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", "")))
        # Delete desktop.ini from the QListWidget.
        self.list_widget.takeItem(self.list_widget.row(self.list_widget.findItems("desktop.ini", Qt.MatchExactly)[0]))

    # Define a method to play the currently selected song
    def play_song(self):
        # Get the name of the currently selected song
        song_name = self.list_widget.currentItem().text()
        # Create a QMediaContent object for the selected song
        media_content = QMediaContent(QUrl.fromLocalFile("C:/Users/63939/Music/" + song_name))
        # Set the media content for the QMediaPlayer
        self.media_player.setMedia(media_content)
        # Start playing the selected song
        self.media_player.play()
        # Set the icon for the play/pause button to the pause icon
        self.play_pause_button.setIcon(
            QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/pause.png'))
        # Connect the clicked signal of the play/pause button to toggle play/pause functionality
        self.play_pause_button.clicked.connect(
            lambda: self.media_player.pause() if self.play_pause_button.isChecked() else self.media_player.play())
        # Set the initial value and connect sliderMoved signal for the song slider
        self.song_slider.setValue(0)
        # If the song ends, put the slider back to the beginning. Do not allow the slider to move to the end again after the song ends
        self.media_player.mediaStatusChanged.connect(lambda: self.song_slider.setValue(0))
        self.move_slider()

    def handle_media_status_changed(self, status):
        # If the media has finished playing
        if status == QMediaPlayer.EndOfMedia:
            # If repeat mode is off, play the next song
            if not self.repeat_mode:
                # Check if a song is currently playing
                if self.shuffle_button.isChecked() and self.shuffled_songs:
                    # Get the song index from the list widget
                    song_index = self.list_widget.currentRow()
                    # Get the song count from the list widget
                    song_count = self.list_widget.count()
                    # If the song index is less than the song count - 1, play the next song
                    if song_index < song_count - 1:
                        # Set the current row to the next song index
                        self.list_widget.setCurrentRow(song_index + 1)
                        # Play the song
                        self.play_song()
                        # Update the song label text
                        self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", ""))
                    # If the song index is equal to the song count - 1, play the first song
                    elif song_index == song_count - 1:
                        self.list_widget.setCurrentRow(0)
                        self.play_song()
                        # Update the song label text
                        self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", ""))
                else:
                    # Get the song index from the list widget
                    song_index = self.list_widget.currentRow()
                    # Get the song count from the list widget
                    song_count = self.list_widget.count()
                    # If the song index is less than the song count - 1, play the next song
                    if song_index < song_count - 1:
                        # Set the current row to the next song index
                        self.list_widget.setCurrentRow(song_index + 1)
                        # Play the song
                        self.play_song()
                        # Update the song label text
                        self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", ""))
                    # If the song index is equal to the song count - 1, play the first song
                    elif song_index == song_count - 1:
                        self.list_widget.setCurrentRow(0)
                        self.play_song()
                        # Update the song label text
                        self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", ""))

    # Define a method to update the song slider based on the current playback position
    def move_slider(self):
        # Set the minimum and maximum values of the song slider
        self.song_slider.setMinimum(0)
        self.song_slider.setMaximum(self.media_player.duration())
        # Set the current value of the song slider based on the playback position
        self.song_slider.setValue(self.media_player.position())
        # Connect the sliderMoved signal to update the playback position
        self.song_slider.sliderMoved.connect(self.media_player.setPosition)
        # Format the current and total time labels
        current_time = time.strftime('%H:%M:%S', time.gmtime(self.media_player.position() / 1000))
        total_time = time.strftime('%H:%M:%S', time.gmtime(self.media_player.duration() / 1000))
        # Update the labels with the formatted times
        self.current_time_label.setText(current_time)
        self.total_time_label.setText(total_time)

    # Define a method to stop the currently playing song
    def stop_song(self):
        # Set the background color of the stop button temporarily
        self.stop_button.setStyleSheet("background-color: white; border: none")
        # Use QTimer to reset the background color after a short delay
        QTimer.singleShot(200, lambda: self.stop_button.setStyleSheet("background-color: transparent; border: none"))
        # Set the icon for the play/pause button to the play icon
        self.play_pause_button.setIcon(QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/play.png'))
        # Clear the current selection in the QListWidget, the slider value, and the time labels
        self.list_widget.setCurrentRow(-1)
        self.song_slider.setValue(0)
        # Remove song label text when the song was stopped and bring it back when a song is selected again
        self.song_label.setText("")
        # Stop the currently playing song
        self.media_player.stop()
        # Clear the media player's current media content
        self.media_player.setMedia(QMediaContent())
        # Hide the labels when the song was stopped and bring it back when song was selected again
        self.total_time_label.hide()
        self.current_time_label.hide()

    # Define a method to delete the currently selected song
    def delete_song(self):
        # Set the background color of the delete button temporarily
        self.delete_button.setStyleSheet("background-color: white; border: none")
        # Use QTimer to reset the background color after a short delay
        QTimer.singleShot(200,
                          lambda: self.delete_button.setStyleSheet("background-color: transparent; border: none"))
        # Check if a song is selected for deletion
        if self.list_widget.currentItem() is None:
            QMessageBox.information(self, "Delete Song", "Please select a song to delete")
            return
        # Ask for confirmation before deleting the selected song
        confirm = QMessageBox.question(self, "Delete Song",
                                       "Are you sure you want to delete " + self.list_widget.currentItem().text(),
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            # Get the name of the selected song
            song_name = self.list_widget.currentItem().text()
            # Remove the selected song from the QListWidget
            self.list_widget.takeItem(self.list_widget.row(self.list_widget.currentItem()))
            # Delete the corresponding file from the directory
            os.remove("C:/Users/63939/Music/" + song_name)
            # Reset song label text when the song was deleted and bring it back when a song is selected again
            self.song_label.setText("")
            self.play_pause_button.setIcon(
                QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/play.png'))
            self.song_slider.setValue(0)
            self.total_time_label.hide()
            self.current_time_label.hide()
        else:
            return

    # Define a method to handle the application's close event
    def closeEvent(self, event):
        # Set the background color of the exit button temporarily
        self.exit_button.setStyleSheet("background-color: white; border: none")
        # Use QTimer to reset the background color after a short delay
        QTimer.singleShot(200,
                          lambda: self.exit_button.setStyleSheet("background-color: transparent; border: none"))
        # Ask for confirmation before closing the application
        confirm = QMessageBox.question(self, "Exit", "Are you sure you want to exit the application?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # Define a method to handle changes in the volume slider
    def volume_slider_value(self):
        # Set the range of the volume slider
        self.volume_slider.setRange(0, 101)
        # Update the displayed volume value
        self.volume_slider_value_label.setText(str(self.volume_slider.value()))
        # Set the volume of the QMediaPlayer
        self.media_player.setVolume(self.volume_slider.value())
        # Update the volume button icon based on the volume level
        if self.volume_slider.value() == 0:
            self.volume_button.setIcon(
                QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/volume-mute.png'))
        elif 1 <= self.volume_slider.value() <= 33:
            self.volume_button.setIcon(
                QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/volume-low.png'))
        elif 34 <= self.volume_slider.value() <= 66:
            self.volume_button.setIcon(
                QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/volume-medium.png'))
        elif 67 <= self.volume_slider.value() <= 100:
            self.volume_button.setIcon(
                QIcon('C:/Users/63939/PycharmProjects/Desktop Music Player/images/volume-high.png'))

    # Define a method to sort songs based on the selected sorting option
    def sort_songs(self):
        # Get the selected sorting option from the combobox
        combobox_text = self.combobox.currentText()
        # Sort the songs in the QListWidget based on the selected option
        if combobox_text == "a-z":
            self.list_widget.sortItems(Qt.AscendingOrder)
        elif combobox_text == "z-a":
            self.list_widget.sortItems(Qt.DescendingOrder)

    # Define a method to search for songs based on the text entered the search bar
    def search_song(self):
        # Get the text entered the search bar
        search_bar_text = self.search_bar.text()
        # Get a list of all song filenames in the music directory
        songs = os.listdir("C:/Users/63939/Music")
        # Clear the QListWidget
        self.list_widget.clear()
        # If the search bar is empty, add all songs to the QListWidget
        if search_bar_text == "":
            self.list_widget.addItems(songs)
        else:
            # Add songs to the QListWidget that match the search criteria
            for song in songs:
                if search_bar_text.lower() in song.lower():
                    self.list_widget.addItem(song)

    # Define a method to replay the current song
    def replay_current_song(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.media_player.setPosition(0)
            self.media_player.play()

    # Define a method to toggle repeat mode
    def repeat_button_clicked(self):
        # Toggle the repeat mode
        self.repeat_mode = not self.repeat_mode
        # Connect or disconnect the replay_current_song method based on the repeat mode
        if self.repeat_mode:
            self.media_player.mediaStatusChanged.connect(self.replay_current_song)
        else:
            self.media_player.mediaStatusChanged.disconnect(self.replay_current_song)

    # Define a method to shuffle the order of songs in the QListWidget
    def shuffle_songs(self):
        if self.shuffle_button.isChecked():
            # Get a list of all song filenames in the original order
            songs = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]
            # Shuffle the order of songs
            shuffle(songs)
            # Clear the QListWidget and add the shuffled songs
            self.list_widget.clear()
            self.list_widget.addItems(songs)
            # Store the shuffled order in the class attribute for future reference
            self.shuffled_songs = songs
        else:
            self.list_widget.sortItems(Qt.AscendingOrder)
            self.shuffle_button.setStyleSheet("background-color: transparent; border: none")

    # Define a method to play the next song in the QListWidget
    def next_song(self):
        # Set the background color of the next button temporarily
        self.next_button.setStyleSheet("background-color: white;")
        # Use QTimer to reset the background color after a short delay
        QTimer.singleShot(200, lambda: self.next_button.setStyleSheet("background-color: transparent;"))
        # Check if the media player is not in the playing state
        if not self.media_player.state() == QMediaPlayer.PlayingState:
            return
        # Get the name of the currently playing song
        song_name = self.list_widget.currentItem().text()
        # Get the index of the currently playing song in the QListWidget
        song_index = self.list_widget.row(self.list_widget.findItems(song_name, Qt.MatchExactly)[0])
        # Get the total number of songs in the QListWidget
        song_count = self.list_widget.count()
        # Check if there is a next song in the list
        if song_index < song_count - 1:
            # Set the current row in the QListWidget to the next song
            self.list_widget.setCurrentRow(song_index + 1)
            # Play the next song
            self.play_song()
            # Update the displayed song label
            self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", ""))
        # If the currently playing song is the last in the list, play the first song
        elif song_index == song_count - 1:
            self.list_widget.setCurrentRow(0)
            self.play_song()
            self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", ""))

    # Define a method to play the previous song in the QListWidget
    def previous_song(self):
        # Set the background color of the previous button temporarily
        self.previous_button.setStyleSheet("background-color: white;")
        # Use QTimer to reset the background color after a short delay
        QTimer.singleShot(200, lambda: self.previous_button.setStyleSheet("background-color: transparent;"))
        # Check if the media player is not in the playing state
        if not self.media_player.state() == QMediaPlayer.PlayingState:
            return
        # Get the name of the currently playing song
        song_name = self.list_widget.currentItem().text()
        # Get the index of the currently playing song in the QListWidget
        song_index = self.list_widget.row(self.list_widget.findItems(song_name, Qt.MatchExactly)[0])
        # Get the total number of songs in the QListWidget
        song_count = self.list_widget.count()
        # Check if there is a previous song in the list
        if song_index > 0:
            # Set the current row in the QListWidget to the previous song
            self.list_widget.setCurrentRow(song_index - 1)
            # Play the previous song
            self.play_song()
            # Update the displayed song label
            self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", ""))
        # If the currently playing song is the first in the list, play the last song
        elif song_index == 0:
            self.list_widget.setCurrentRow(song_count - 1)
            self.play_song()
            self.song_label.setText(self.list_widget.currentItem().text().replace(".mp3", ""))

        # Define a method to refresh the QListWidget with the latest songs from the music directory

    def refresh_songs(self):
        # Set the background color of the refresh button temporarily
        self.refresh_button.setStyleSheet("background-color: white;")
        # Use QTimer to reset the background color after a short delay
        QTimer.singleShot(200, lambda: self.refresh_button.setStyleSheet("background-color: transparent;"))
        # Clear the QListWidget
        self.list_widget.clear()
        # Load the songs from the music directory
        self.load_songs()


# Main entry point of the application
if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)
    # Create an instance of the MainWindow class
    window = MainWindow()
    # Show the main window
    window.show()
    # Execute the application
    sys.exit(app.exec_())
