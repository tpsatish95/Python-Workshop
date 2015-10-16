import urllib.request
import simplejson
import time

fetcher = urllib.request.build_opener()

searchTerm = "festivals"
searchTerm = urllib.request.quote(searchTerm.replace(" ", "+"))  # for non-ascii encoding of search term
numberOfImages = 4

urls = []

for startIndex in range(0, numberOfImages, 4):
    while True:
        searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(startIndex)
        f = fetcher.open(searchUrl)
        deserialized_output = simplejson.load(f)
        if None == deserialized_output["responseData"]:
            # print(deserialized_output)
            print("Retrying " + str(startIndex))
            # Sleep for two second to prevent IP blocking from Google
            time.sleep(2)

            continue

        else:
            for temp in deserialized_output["responseData"]["results"]:
                # print(temp["url"])
                urls.append(temp["url"])
                # Sleep for two second to prevent IP blocking from Google
                time.sleep(2)

            print(startIndex)
            break

count = 0
for u in urls:
    try:
        image = urllib.request.urlopen(u.strip()).read()
        print(u)
        f = open("./Images/" + str(count) + "." + u.split(".")[len(u.split("."))-1],'wb')
        f.write(image)
        f.close()
    except:
        print("Failed !")
        continue

    count += 1
