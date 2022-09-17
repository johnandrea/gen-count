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

## Bug reports

This code is provided with neither support nor warranty.
