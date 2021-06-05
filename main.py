from os import path
from preprocessNormalText import preprocess_normal_text


def main():
    in_path = path.relpath("Subtitles")
    out_path = path.relpath("ProcessedSubtitles")

    preprocess_normal_text(in_path, out_path)


main()
