from cli import create_parser
from csv_reader import processing_files
from formatters.payout import register_formatter


def main():
    parser = create_parser()
    args = parser.parse_args()
    output = processing_files(
        args.filename,
        args.report,
        register_formatter.get_formatter(args.format)
    )
    print(output)


if __name__ == '__main__':
    main()
