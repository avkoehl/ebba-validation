import os

def get_clusters (fname):
    clusters = []
    f = open ("../data/clusters/" + fname, "r")
    for line in f:
        clusters.append(line)
    return clusters

def make_html (fname):
    imgs = os.listdir("../assets/images/")
    o = open ("../html/" + fname.split('.')[0] + ".html", "w")
    path = "../assets/images/"
    print ("<doctype HTML><head><title>visualize clusters</title></head><body>", file= o)
    print ("<style> img { width: 75px; } </style>", file=o)
    clusters = get_clusters(fname)
    nimgs = 0
    for i in clusters:
        images = i.split("\t") 
        nimgs = nimgs + len(images)
    print ("<p> Number of images: " ,nimgs , "</p>", file=o)

    count = 0 
    for i in clusters:
        images = i.split("\t") 
        if count >= 0: 
            print ("<p> Cluster id: ", count, file=o)
            print ("  Size ", len(images) , "</p>", file=o)

            for image in images:
                if image in imgs:
                    print ("<img title=\"", image, "\" src=\"", path + image.split('.')[0] + ".jpg", "\"/>", file=o)
                else:
                    print ("<img title=\"",  image, "not found", "\" src=\"", path + image.split('.')[0] + ".jpg", "\"/>", file=o)


        print ("<hr>", file=o)
        count = count + 1

    print ("</body></html>", file=o)
    o.close()
    return

def main():
    files = os.listdir("../data/clusters/")
    for fname in files:
        make_html(fname)

if __name__=="__main__":
    main()



