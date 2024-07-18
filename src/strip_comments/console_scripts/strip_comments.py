import argparse
from pathlib import Path

from strip_comments import strip


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', type=Path,
                        help='input files')
    parser.add_argument('-w', '--write', action='store_true',
                        help='make changes in-place')
    parser.add_argument('-b', '--keep-block', action='store_true',
                        help='keep block comments')
    parser.add_argument('-l', '--keep-line', action='store_true',
                        help='keep line comments')
    parser.add_argument('-f', '--first-only', action='store_true',
                        help='strip only the first comment')
    parser.add_argument('-t', '--language', type=str, default='javascript',
                        help='programming language (autodetect TODO)')
    parser.add_argument('-p', '--keep-protected', action='store_true',
                        help='keep protected comments (starting with a "!" char)')
    parser.add_argument('-n', '--preserve-newlines', action='store_true',
                        help='preserve newlines of stripped comments')

    args = parser.parse_args()
    print(args)

    file = args.files[0]
    res = strip.strip(
        source=file.read_text(),
        block=True if not args.keep_block else False,
        line=True if not args.keep_line else False,
        first=True if args.first_only else False,
        language=args.language,
        keep_protected=args.keep_protected,
        preserve_newlines=args.preserve_newlines
    )
    print(res)


if __name__ == '__main__':
    main()
