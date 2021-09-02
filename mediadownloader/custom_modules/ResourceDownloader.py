import requests
import pafy


def download_file(file_link):
    # extract file name from file_link
    filename = file_link.split("/")[-1]
    # download resource using GET
    raw_file = requests.get(file_link, stream=True)
    # save the resource recieved into the file
    with open(filename, 'wb') as fd:
        for chunk in raw_file.iter_content(chunk_size=1024):
            fd.write(chunk)
    return


def download_media_playlist(url=None):
    if url:
        if len(url.strip()) > 0:
            if not url.startswith('https://www.youtube.com/watch?v='):
                url = "https://www.youtube.com/watch?v={}".format(url)

            playlist = pafy.get_playlist(url)

            if playlist:
                print("Playlist:\t{}\n\n".format(playlist))
                return {'status': True, 'playlist': playlist}
            else:
                return {
                    'status': False,
                    'cause': 'Couldn\'t download playlist {}'.format(url)
                }


def download_media_file(url=None):
    if url:
        if len(url.strip()) > 0:
            if not url.startswith('https://www.youtube.com/watch?v='):
                url = "https://www.youtube.com/watch?v={}".format(url)

            # create video object
            media = pafy.new(url)
            if media:
                # extract information about best resolution video available
                bestResolutionVideo = media.getbest()

                print("Media:\t{}\n\n".format(media))

                # download the video
                bestResolutionVideo.download()

                return {'status': True, 'media': media}
            else:
                return {
                    'status': False,
                    'cause': 'Could\'t download {}'.format(url)
                }


def download_media_meta(url=None):
    if len(url.strip()) > 0:
        props = []

        if not url.startswith('https://www.youtube.com/watch?v='):
            url = "https://www.youtube.com/watch?v={}".format(url)

        meta = pafy.new(url)

        if meta:
            for i, m in enumerate(dir(meta)):
                props.append(m)

            return {'status': True, 'metadata': meta, 'properties': props}
        else:
            return {
                'status': False,
                'cause': 'Couldn\'t download {}'.format(url)
            }


def get_raw_resource(url):
    if not url.startswith('https://www.youtube.com/watch?v='):
        url = "https://www.youtube.com/watch?v={}".format(url)
    return requests.get(url, stream=True)


def get_headers(url):
    if not url.startswith('https://www.youtube.com/watch?v='):
        url = "https://www.youtube.com/watch?v={}".format(url)
    return requests.head(url).headers


def show_headers(url):
    if not url.startswith('https://www.youtube.com/watch?v='):
        url = "https://www.youtube.com/watch?v={}".format(url)
    headers = requests.head(url).headers
    print(headers)
