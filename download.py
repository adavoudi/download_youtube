import argparse
from pytube import YouTube
from tqdm import tqdm
import pathlib


parser = argparse.ArgumentParser(description='Download a list of videos from youtube.')
parser.add_argument('video_list', type=str,
                   help='Path to a text file in which each line represents a a youtube link.')
parser.add_argument('--output_dir', type=str, default='.',
                   help='Path to a directory where videos will be downloaded to.')
args = parser.parse_args()


def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    bar.update(len(chunk))
    return


output_dir = args.output_dir
pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)


with open(args.video_list, 'r') as f:
    links = f.readlines()

for link in links:
    print('Downloading [%s] ...' % link)
    yt = YouTube(link)
    yt.register_on_progress_callback(show_progress_bar)

    link = yt.streams.filter(only_video=True,subtype='mp4').order_by('resolution').asc().first()
    bar = tqdm(range(link.filesize))
    link.download(output_path=output_dir)
    print()