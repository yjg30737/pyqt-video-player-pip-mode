from setuptools import setup, find_packages

setup(
    name='pyqt-video-player-pip-mode',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_video_player_pip_mode.style': ['button.css', 'progressbar.css'],
                  'pyqt_video_player_pip_mode.ico': ['window.png']},
    description='PyQt Video Player PIP Mode',
    url='https://github.com/yjg30737/pyqt-video-player-pip-mode.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)