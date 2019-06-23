# importing google_images_download module for searching and downloading images from google images
from google_images_download import google_images_download
#importing matplotlib for ploting of image
import matplotlib.pyplot as plt
#importing Image from PIL for opening image from computer
from PIL import Image



def search(key):
    # creating object
    response = google_images_download.googleimagesdownload()

    #Query that will be searched
    search_queries = []

    #key is Keyword that will be searched
    search_queries.append(key)

    def downloadimages(query):
        # keywords is the search query
        # format is the image file format
        # limit is the number of images to be downloaded
        # print urs is to print the image file url
        # size is the image size which can
        # be specified manually ("large, medium, icon")
        # aspect ratio denotes the height width ratio
        # of images to download. ("tall, square, wide, panoramic")
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 1,
                     "print_urls": True,
                     "size": "medium",
                     "aspect_ratio": "panoramic" }
        try:
            return response.download(arguments)

            # Handling File NotFound Error
        except FileNotFoundError:
            arguments = {"keywords": query,
                         "format": "jpg",
                         "limit": 4,
                         "print_urls": True,
                         "size": "medium"}

            # Providing arguments for the searched query
            try:
                # Downloading the photos based
                # on the given arguments
                response.download(arguments)
            except:
                pass


    for query in search_queries:
        url=downloadimages(query)
        #Getting orignal url from list which is in format ({[]}) that is tuple(dictionary{list[]})
        url=url[0][key][0]
        print(url)

    # image = Image.open(urllib.request.urlopen(url))
    # width, height = image.size
    # print (width,height)

    try:
        img  = Image.open(url)   #checking for error
    except IOError:
        pass


    #ploting image
    plt.figure()
    plt.imshow(img)
    plt.show()