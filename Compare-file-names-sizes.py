
#import necessary libraries (packages)
import os

#folder you are copying FROM and TO
folder_to = "I://SCIENCE-BIO-TOFdata//T1-056_raw data//2022-10-24 Archive"
folder_from = "D://2022 Abisko data//TOF data"

#create a list with all file names from both folders
content_from = os.listdir(folder_from)
content_to = os.listdir(folder_to)

#print/see them
print(len(content_from))
print(len(content_to))

#find differences in file name sin the folders. This way, you can see which 
#files are not matching/missing from folder you are copying TO
result = set(content_from) - set(content_to)
print(result)

#Files that are present in the FROM folder but not in TO folder:

#T1-056_2022_07_12_14_02_28.h5
#T1-056_2022_07_06_15_01_24.h5
#T1-056_2022_06_05_09_54_07.h5

#compare if the file sizes are equal between the two folders. It can be be that 
#you need to stop copying, or somehting goes wrong, or if you upload to I-drive-
#internet fails  etc.



for i in list(result):
    print(i)
    content_from.remove(i)

counter_equal = 0
counter_not_equal = 0

for file_from, file_to in zip(sorted(content_from), sorted(content_to)):
    file_from_stats = os.stat(os.path.join(folder_from, file_from))
    file_from_size = file_from_stats.st_size / (1024 * 1024)

    file_to_stats = os.stat(os.path.join(folder_to, file_to))
    file_to_size = file_to_stats.st_size / (1024 * 1024)

    if file_from_size != file_to_size:
        counter_not_equal += 1
        print(f"not equal: {counter_not_equal}")
        print(file_from)
    else:
        counter_equal += 1
        print(f"equal: {counter_equal}")

print("End:")
print(f"not equal: {counter_not_equal}") #this tells how many file sizes do not
#match between the two folders
print(f"equal: {counter_equal}")
        

#three file sizes do not match with TO and FROM folder:

#T1-056_2022_07_06_13_31_24.h5
#T1-056_2022_07_06_14_01_24.h5
#T1-056_2022_07_06_14_31_24.h5
