import argparse
import json
import sys
import youtube_dl


DEFAULT_CHANNEL = 'https://www.youtube.com/channel/UC4BWYC4VLmE7wCpjbqqbS0w'
DEFAULT_INDEX_FILE = 'index_file.json'
DEFAULT_OUT_DIR = './videos'

SAVE_FORMAT = '%(id)s.%(ext)s'

def get_chan_videos(channel_url, download=False, output='.'):
    """
        Also works with individual video ids!
    """
    with youtube_dl.YoutubeDL({'outtmpl': output+'/'+SAVE_FORMAT}) as yt:
        results = yt.extract_info(channel_url, download=download)

    if 'entries' not in results:
        return [results]
    else:
        return results['entries']


def filter_results(results):
    keys = ['id', 'title', 'description']
    videos = {}
    for result in results:
        videos[result['id']] = {
            'title': result['title'],
            'description': result['description']
        }
    return videos


def make_index_file(filename, videos, append=False):
    if append:
        with open(filename, 'r') as file:
            current = json.load(file)
            videos = {**current, **videos}
    with open(filename, 'w+') as file:
        file.write(json.dumps(videos, indent=4))


def test_hook(status):
    print(json.dumps(status, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Downloads meta info and ' +
                                                 'videos from the web')
    parser.add_argument('-a', '--append', help='append to index file rather' +
                        ' than overwrite', action='store_true')
    parser.add_argument('-d', '--download', help='save videos to disk',
                        action='store_true')
    parser.add_argument('-i', '--index', help='index file name',
                        default=DEFAULT_INDEX_FILE)
    parser.add_argument('-o', '--output', help='video save location',
                        default=DEFAULT_OUT_DIR)
    parser.add_argument('-u', '--url', help='channel/video URL',
                        default=DEFAULT_CHANNEL)
    args = parser.parse_args()

    videos = get_chan_videos(args.url, args.download, args.output)
    videos = filter_results(videos)

    if (videos is None) or (len(videos) is 0):
        print('No videos found')
        sys.exit(0)

    make_index_file(args.index, videos, args.append)
    print('Completed process')

