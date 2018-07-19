# Youtube downloader
Download a list of videos from youtube.

## Install
You can choose _one_ of the following two ways to get started with `youtubevideosdownload`.

1. Let pip install `youtubevideosdownload` globally in dev mode (still globally accessible, but changes to the code immediately take effect)
    ```bash
    $ pip3 install -e .
    ```

2. Install with pip globally
    ```
    $ pip3 install .
    ```

## Usage

```
usage: youtubevideosdownload [-h] [--output_dir OUTPUT_DIR] [--no_audio]
                             {list,link} path

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
  --no_audio            Download videos with no audio (default false)
```