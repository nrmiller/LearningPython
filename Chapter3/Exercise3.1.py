import sys
import collections


# sites is a dictionary of (site -> set of file names)
sites = collections.defaultdict(set)
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            i = 0
            while True:
                site = None
                i = line.find("https://", i)
                if i > -1:
                    i += len("https://")

                    # Find the end of the site.
                    for j in range(i, len(line)):
                        if not (line[j].isalnum() or line[j] in ".-"):
                            site = line[i:j].lower()
                            break
                    if site and "." in site:
                        sites[site].add(filename)
                    i = j  # Advance i to find more sites within the same line
                else:
                    break  # Advance to next line in the file

for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key=str.lower):
        if " " in filename:
            filename = "\"{0}\"".format(filename)
        print("\t{0}".format(filename))
