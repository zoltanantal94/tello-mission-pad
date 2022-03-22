# Tello edo mission pad tester
## Install
Using the commands below you can install the repository
```
git clone https://github.com/zoltanantal94/tello-mission-pad.git
cd tello-mission-pad
git clone https://github.com/damiafuentes/DJITelloPy.git
cd DJITelloPy
pip install -e .
```
## Usage
In _main.py_ you can choose fly id that will use.
```
def main():
    fly5.fly(pad_dist, alt, speed, wait, res, ip)
```