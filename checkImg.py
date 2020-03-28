import os
import shutil

used_data_path = '/Users/sunbowen/Desktop/cockle_detection/data/images'
all_data_path = '/Users/sunbowen/Desktop/AUT_Master_2020/Project/self_collected_cockle/images'

used_data = []
all_data = []

used_data_count = 0

for file in os.listdir(used_data_path + '/test'):
    if file.endswith(".jpg") or file.endswith(".JPG"):
        used_data_count = used_data_count+1
        used_data.append(file)

for file in os.listdir(used_data_path + '/train'):
    if file.endswith(".jpg") or file.endswith(".JPG"):
        used_data_count = used_data_count+1
        used_data.append(file)


# print(used_data_count)
# print(used_data)
all_data = os.listdir(all_data_path)


def diff(li1, li2):
    return list(set(li1) - set(li2))


# unique_list = diff(used_data, all_data)
unique_list = []

print(len(all_data))
print(used_data_count)

for item in all_data:
    if item not in used_data:
        unique_list.append(item)

print(len(unique_list))

# for item in unique_list:
#     shutil.copy(all_data_path + '/' + item, '/Users/sunbowen/Desktop/UniqueImg')
#

# print(diff(all_data, used_data))


