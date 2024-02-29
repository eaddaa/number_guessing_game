from setuptools import setup, find_packages

setup(
    name='number-guessing-game',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'cann_calculator==1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'number-guessing-game=my_number_guessing_game.game_logic:play_game',
        ],
    },
)
