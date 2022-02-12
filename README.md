# pyqt-video-player-pip-mode
PyQt Video Player PIP Mode

## Requirements
* PyQt5 >= 5.15

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-video-player-pip-mode.git --upgrade```

## Feature
* Frameless, movable.
* When mouse cursor is hovering over the window, interface will be shown. 

## Examples
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_video_player_pip_mode import PipVideoWidget


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    pipVideoWidget = PipVideoWidget('pyqt_textbox_graphics_widget_example_video.mp4')
    pipVideoWidget.show()
    sys.exit(app.exec_())
```

Result

When mouse cursor is over the pip window, interface will be shown.

![image](https://user-images.githubusercontent.com/55078043/153712864-6e831c7d-d645-4ab5-81b5-c7ffa9a42517.png)

When mouse cursor leaves, interface will be invisible.

![image](https://user-images.githubusercontent.com/55078043/153712843-bdafd289-fefe-4978-94c5-66ec2cf4646d.png)

## Note
This is very first version of the module so it can be crude. I'll improve it.
