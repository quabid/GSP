from custom_modules.ResourceDownloader import download_media_file, download_media_meta, download_media_playlist


class YoutubeVideoDownloader:
    def __init__(this):
        this.WHICH = {
            'video': this.download_video,
            'playlist': this.download_playlist,
            'metadata': this.download_metadata,
            'meta': this.download_metadata
        }

        def download_video(this, url=None, video_playlist_meta='video'):
            function = this.WHICH[video_playlist_meta]
            return function(url)

        def download_playlist(this, url=None, video_playlist_meta='video'):
            function = this.WHICH[video_playlist_meta]
            return function(url)

        def download_metadata(this, url=None, video_playlist_meta='video'):
            function = this.WHICH[video_playlist_meta]
            return function(url)
