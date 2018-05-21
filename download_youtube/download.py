import argparse
from pytube import YouTube
from tqdm import tqdm
import pathlib


parser = argparse.ArgumentParser(description='Download a list of videos from youtube. (Powered by PyTube [https://github.com/nficano/pytube])')
parser.add_argument('source', choices=['list', 'link'],
                   help='Whether the following path is a path to a text file (containig links) or to a youtube link')
parser.add_argument('path', type=str,
                   help='Path to a youtube link or to a text file in which each line represents a youtube link.')
parser.add_argument('--output_dir', type=str, default='.',
                   help='Path to a directory where videos will be downloaded to.')
parser.add_argument('--no_audio', action='store_true', 
                   help='Download videos with no audio (default false)')

args = parser.parse_args()
output_dir = args.output_dir
only_video = args.no_audio


def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    bar.update(len(chunk))
    return

def download_link(link):
    global bar
    link = link.strip()
    print('Downloading [%s] ...' % link)
    yt = YouTube(link)
    yt.register_on_progress_callback(show_progress_bar)

    if only_video:
        link = yt.streams.filter(only_video=True,subtype='mp4').order_by('resolution').desc().first()
    else:
        link = yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').desc().first()
    
    bar = tqdm(range(link.filesize), unit='Bytes', unit_scale=True)
    link.download(output_path=output_dir)
    bar.close()
    print()


def main():
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

    if args.source == 'list':
        with open(args.path, 'r') as f:
            links = f.readlines()

        for idx, link in enumerate(links):
            print('[%d/%d]' % (idx+1,len(links)))
            download_link(link)
            print('----------------------------------')
    else:
        download_link(args.path)