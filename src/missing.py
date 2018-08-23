import os

def get_clusters (fname):
    clusters = []
    f = open ("../data/clusters/" + fname, "r")
    for line in f:
        clusters.append(line)
    return clusters

def make_html (fname):
    imgs = os.listdir("../assets/images/")
    o = open ("../html/" + fname.split('.')[0] + "_missing.html", "w")
    path = "../assets/images/"
    print ("<doctype HTML><head><title>visualize clusters</title></head><body>", file= o)
    print ("<style> img { width: 75px; max-height: 100px } </style>", file=o)
    clusters = get_clusters(fname)
    nimgs = 0
    for i in clusters:
        images = i.split("\t") 
        nimgs = nimgs + len(images)
    print ("<p> Number of images: " ,len(imgs) - nimgs , "</p>", file=o)

    count = 0 
    included = []
    for i in clusters:
        images = i.split("\t")
        for i in images:
            included.append(i.rstrip().split('.')[0] + ".jpg")
    missing = [img for img in imgs if img not in included]

    for image in missing:
        print ("<img title=\"",  image, "not found", "\" src=\"", path + image.split('.')[0] + ".jpg", "\"/>", file=o)

    print ("<hr>", file=o)
    print ("</body></html>", file=o)
    o.close()
    return

def main():
    files = os.listdir("../data/clusters/")
    for fname in files:
        make_html(fname)

if __name__=="__main__":
    main()



