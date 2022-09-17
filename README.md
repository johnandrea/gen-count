# gen-count
Given a GEDCOM file, report the families with the max number of children, grandchildren, g-grandchildren, ... 

## Limitations

- Requires Python 3.6+
- Makes use of [readgedcom.py](https://github.com/johnandrea/readgedcom) library.

## Installation

No installation process. Copy the program and the library.

Alternately a standalone (no need of Python) .EXE file has been compiled via pyinstaller and is avalable.

## Usage

gen-count.py family.ged >max-desc.txt

or similarily if using the .EXE

gen-count family.ged >max-desc.txt

## Output

children
number-of-children  name-of-parents

grandchildren
number-of-children name-of-parents

...

## Example Output

children
4 Elizabeth_II Alexandra Mary Windsor + Philip Mountbatten

grandchildren
3 Anne Elizabeth Alice Windsor + Mark Anthony Peter Phillips
3 Carole Elizabeth Goldsmith + Michael Middleton

g-grandchildren
2 Elizabeth Angela Marguerite Bowes-Lyon + George_VI Windsor
2 Frances Shand Kydd + John Spencer

gg-grandchildren
1 Elizabeth Angela Marguerite Bowes-Lyon + George_VI Windsor

## Bug reports

This code is provided with neither support nor warranty.
