# Customer Records

### Install Dependencies
```
pip install -r requirements.txt
```
### Instructions
```
$ python main.py --help
usage: filter_customers [-h] [--input INPUT] [--output OUTPUT]
                        [--origin ORIGIN] [--distance DISTANCE]

optional arguments:
  -h, --help           show this help message and exit
  --input INPUT        Input file - containing customers list (default:
                       input/customers.txt)
  --output OUTPUT      Output file - will contain filtered customers list
                       (default: STDOUT)
  --origin ORIGIN      Origin location in <latitude,longitude> format
                       (default: 53.339428,-6.257664)
  --distance DISTANCE  Distance in km (default: 100)
```
### Sample Run
```
$ python main.py
4: Ian Kehoe
5: Nora Dempsey
6: Theresa Enright
11: Richard Finnegan
39: Lisa Ahearn
12: Christina McArdle
15: Michael Ahearn
31: Alan Behan
13: Olive Ahearn
29: Oliver Ahearn
30: Nick Enright
23: Eoin Gallagher
8: Eoin Ahearn
24: Rose Enright
17: Patricia Cahill
26: Stephen McArdle

$ python main.py --distance 30
4: Ian Kehoe
5: Nora Dempsey
6: Theresa Enright
```
### Tests
```
python -m pytest tests
```