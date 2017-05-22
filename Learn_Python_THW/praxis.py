import re, os, glob, fileinput, sys, argparse
print("Imported: utils")
parser = argparse.ArgumentParser(description='''Welcome to Mom Searcher. A
regex solution to simplify searching for specific strings (intended for
 log files to maintain Policy compliance).''')

# def type_string(data):
#     value = data
#     if isinstance(value, int):
#         return value
#     msg = "TypeError: {} is not a string".format(value)
#     raise argparse.ArgumentTypeError(msg)


parser.add_argument("source_path", help="directory(s) where search begins")
parser.add_argument("search_terms", nargs='*',
                    help="Must be >= 1, traverses through file(s) and prints search_term(or its regex matches) and its found location")
# Argument (optional)- if user uses flag, recursive key is changed to True
parser.add_argument("-r", "--recursive", action="store_const", const='True', default='False',
                    help="recursively traverse through directories and return ALL files")
parser.add_argument("-l", "--print_line", action="store_const", const='True', default='False',
                    help="print full line that search term appears on")

args = parser.parse_args()
kwargs = vars(args)
print(kwargs)

def parsing_parameters(search_terms, **kwargs):
    for index, term in enumerate(search_terms, start=1):
        print("Search Term {}: {}".format(index, term))
    for key, val in kwargs.items():
        print("{}: {}".format(key, val))

def file_finder_updated(source_path, recursive, **remaining):
    return glob.glob(source_path, recursive=recursive)

def line_printer(files):
    with fileinput.input(files=files) as file:
        for line in file:
            print(fileinput.filename())
            print("LineNo: {}: {}".format(fileinput.lineno(), line))

def multi_file_search(files, search_terms, print_line, **kwargs):
    print("Files: {}, Search_terms: {}".format(files, search_terms))
    with fileinput.input(files=files) as file:
        for line in file:
            for term in search_terms:
                matches= re.findall(term, line)
                for item in matches:
                    print(fileinput.filename())
                    print("Line Number: {}: Found: {}".format(fileinput.lineno(), item))
                    if print_line:
                        print(line)
def directory_parser(files):
    just_directories = []
    just_files = []
    for index, file in enumerate(files):
        print(os.getpid())
        if os.path.isdir(file):
            just_directories.append(file)
        else:
            just_files.append(file)
    data = {'files': just_files, 'directories': just_directories}
    return data

def python_search(file, search_terms):
    with open(file,'r') as file:
        for index, line in enumerate(file, start=1):
            for term in search_terms:
                #matches= re.compile(term, re.MULTILINE|re.DOTALL).findall(line)
                matches= re.findall(term, line)
                for item in matches:
                    print("line_Number: {}, matched: {}".format(index, item))

parsing_parameters(**kwargs)
files = file_finder_updated(**kwargs)
files = directory_parser(files)['files']
multi_file_search(files, **kwargs)
