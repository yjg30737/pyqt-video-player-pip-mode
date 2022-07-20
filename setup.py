from setuptools import setup, find_packages

setup(
    name='pyqt-video-player-pip-mode',
    version='0.3.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_video_player_pip_mode.style': ['progressbar.css'],
                  'pyqt_video_player_pip_mode.ico': ['pip.svg', 'close.svg', 'play.svg', 'pause.svg']},
    description='PyQt video player in PIP(Picture-in-picture) mode',
    url='https://github.com/yjg30737/pyqt-video-player-pip-mode.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-resource-helper>=0.0.1',
        'pyqt-svg-button>=0.0.1'
    ]
)