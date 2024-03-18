import argparse


urls = ['https://u4help.ru/photo/photo1.jpg',
        'https://u4help.ru/photo/photo_2.jpg',
        'https://u4help.ru/photo/photo_3.jpg',
        'https://u4help.ru/photo/photo_4.jpg',
        'https://u4help.ru/photo/photo_5.jpg',
        ]


def st_parser():
    parser = argparse.ArgumentParser(description='Entering images URLs')
    parser.add_argument("-u", "--urls", default=urls, nargs='*', help='Enter the URLs images separated by spaces')
    args = parser.parse_args()
    return args.urls


if __name__ == '__main__':
    st_parser()




