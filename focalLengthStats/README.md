# Focal length stats

Gets focal length disribution from image EXIF data in given directory. I was wondering which focal length I use the most and which prime lens should I buy next, so I asked computer about it. 

Data is in text from and quite rough (e.g. when you have zoom lens, you can get 33, 34 and 35mm depending on how precise are you with the zoom ring) but it gives some insight.

## Usage

Basic:

`focalLengthStats.py --dir DIRECTORY`

Additional options are shown on help command:

`focalLengthStats.py --help`

## Technologies & tools

* Python,
* [ExifRead](https://pypi.org/project/ExifRead/)

## Additional info

* [ExifRead](https://pypi.org/project/ExifRead/) library is required,
* Tested on JPEG and Nikon RAW files (NEF),
* Focal lengths are "physical" ones, not full frame equivalents.
