import glob
from timeit import default_timer as timer
import argparse
import exifread


class Counter():
    def __init__(self): 
        self.count_data = {}
    
    def count(self, item_label):
        if item_label in self.count_data:
            self.count_data[item_label] += 1
        else:
            self.count_data[item_label] = 1

    def get_count_data(self):
        return self.count_data


def parse_args():
    parser = argparse.ArgumentParser(description='Calculates focal length stats for given photo directory.')

    parser.add_argument('--dir',  dest='directory', action="store", help="photo directory path", required=True)
    parser.add_argument('--extension',  dest='extension', action="store", help="photo files extension", default='NEF')
    parser.add_argument('--show-time',  dest='show_time', action="store_const", help="show processing time info", default=False, const=True)
    parser.add_argument('--show-file-names',  dest='show_file_names', action="store_const", help="show each file name during processing (slower, but more detailed logging)", default=False, const=True)
    
    return parser.parse_args()

def measure_time(method):
    def timed(*args, **kwargs):
        time_start = timer()
        result = method(*args, **kwargs)
        time_end = timer()
        if 'show_time' in kwargs and kwargs['show_time']:
            elapsed = round(time_end - time_start, 8)
            print(f'\nTime elapsed: {elapsed} s')

        return result
    return timed
    
@measure_time    
def calculate_stats(photo_directory, photo_extension, show_file_names, show_time):
    focal_length_key_name = 'EXIF FocalLength'
    photos = glob.glob(f'{photo_directory}/**/*.{photo_extension}', recursive=True)
    photo_count = len(photos)
    counter = Counter()
    
    print(f'Photos to process: {photo_count}')
    print('Processing...')

    for photo_number, photo_path in enumerate(photos, start=1):
        if (show_file_names):
            print(f'({photo_number}/{photo_count})\t{photo_path}')
        with open(photo_path, 'rb') as photo_file:
            # details=False speeds up the proces over 100 times
            exif_info = exifread.process_file(photo_file, details=False, stop_tag=focal_length_key_name)
            focal_length_label = str(exif_info[focal_length_key_name])
            counter.count(focal_length_label)

    print('Done!\n')
            
    print(f'Photo count {photo_count}\n')
    
    print('Length\tPercentage')
    focal_lenghts = counter.get_count_data()
    for (focal_length, count) in focal_lenghts.items():
        percentage = round(count/photo_count * 100, 2)
        print(f'{focal_length}\t{percentage}%')
                
if __name__ == "__main__":
    args = parse_args()
    calculate_stats(args.directory, args.extension, args.show_file_names, show_time=args.show_time)

    