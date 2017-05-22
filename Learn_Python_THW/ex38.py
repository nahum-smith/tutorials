import re

object = {"hey,": "now", "yo": "fool", "wow": {"killin": "it"}}
object["bitch"] = "ass-nigga"

print("sorted: {}".format(sorted(object)))
print("items method: {}".format(object.items()))
print("keys method: {}".format(object.keys()))

hey_list = ['hey,', 'yo', 'mom', 'bitch,']



def dict_item_clean(dict, regex):
    new_dict = {}
    for key, item in object.items():
        # for endswith argument substitute a regex catching all unnecessary characters
        if key.endswith(","):
            new_dict[key[:-1]] = item
        else:
            new_dict[key] = item

def list_item_clean(list, regex):

    new_list = []
    for item in list:
        if re.match(',', item[-1]):
            new_list.append(item[:-1])
        else:
            new_list.append(item)
    return new_list

new_list = list_item_clean(hey_list, ',')
print(new_list)
