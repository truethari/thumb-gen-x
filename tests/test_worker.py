import pytest

from thumb_gen_x.worker   import Generator

#video_path, output_path='', custom_text=True, font_dir='', font_size=0, bg_colour='', font_colour=''

def test_worker_1():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen-x/thumb-gen-x/"
    app = Generator(video_path, output_path, "thumb gen X")
    test_worker_value = app.run()
    assert test_worker_value == True

def test_worker_2():
    video_path = "/home/sample-mp4-file.mp4"
    output_path = "/home/runner/work/thumb-gen-x/thumb-gen-x/"
    app = Generator(video_path, output_path, font_size=10, bg_colour="yellow", font_colour="black")
    test_worker_value = app.run()
    assert test_worker_value == True
