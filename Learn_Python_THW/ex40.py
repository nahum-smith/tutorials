import re, os, glob, fileinput
print("Imported: utils")
# loops through list and eliminates last character in item in list if that
# character is matching a regex expression.  Also will eliminate 'blank' list items
# def list_item_clean(input_list, regex):

#     new_list = []
#     for item in input_list:
#         if len(item) != 0:
#             if re.match(regex, item[-1]):
#                 new_list.append(item[:-1])
#             else:
#                 new_list.append(item)
#         else:

#     return new_list

# # First way to clean off unnecessary characters at end of string (non-recursive and no regex)
# def character_clean(string, regex):
#     string_list = list(string)
#     clean_list = []
#     print("checking list: {}".format(string_list))
#     for index, item in enumerate(string_list):
#         print("{}: {}".format(index, item))
#         if re.match(regex, item):
#           pass
#         else:
#             clean_list.append(item)
#     string = "".join(clean_list)
#     return string

# # Second Way to clean unnecessary characters at end of string (recursive and no regex)
# def character_clean2(string, regex):
#     if string.endswith(regex):
#         string = string[:-1]
#         return character_clean2(string, regex)
#     else:
#         return string


# stuff = character_clean2("mom22222","2")
# print(stuff)

files = []
#Creating file list based on regex search specified
for filename in glob.glob('**/*.txt', recursive=True):
    files.append(filename)

# convert the list into a tuple data type
files_tup = tuple(files)

# reads through list tuple and prints all lines
with fileinput.input(files=files_tup) as f:
    for line in f:
        print(line)
