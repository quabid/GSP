import unittest
from custom_modules.ResourceDownloader import download_media_meta, get_headers


class DownloadMediaFileTestCase(unittest.TestCase):
    def test_dummy(this):
        this.assertTrue(True)

    def test_download_media_meta(this):
        url = 'zMClRJfLBP4'
        downloaded_media_meta = download_media_meta(url)
        this.assertIn('status',
                      downloaded_media_meta,
                      msg="no such key exists".capitalize())
        this.assertIn('metadata',
                      downloaded_media_meta,
                      msg="no such key exists".capitalize())
        this.assertIn('properties',
                      downloaded_media_meta,
                      msg="no such key exists".capitalize())
        this.assertEqual(downloaded_media_meta['status'], True)

    def test_get_headers(this):
        url = 'zMClRJfLBP4'
        headers = get_headers(url)
        this.assertIsInstance(type(headers), type(dict))


if __name__ == '__main__':
    unittest.main()
