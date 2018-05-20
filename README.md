# Youtube downloader
Download a list of videos from youtube.

## Install
Just run `pip3 install download_youtube`

```
usage: download.py [-h] [--output_dir OUTPUT_DIR] {list,link} path

Download a list of videos from youtube. (Powered by PyTube
[https://github.com/nficano/pytube])

positional arguments:
  {list,link}           Whether the following path is a path to a text file
                        (containig links) or to a youtube link
  path                  Path to a youtube link or to a text file in which each
                        line represents a youtube link.

optional arguments:
  -h, --help            show this help message and exit
  --output_dir OUTPUT_DIR
                        Path to a directory where videos will be downloaded
                        to.
```