import os, shutil, glob, json

try:
    os.mkdir('./processed')
except OSError:
    print ("'processed' directory already exists")

# Get a list of receipts

receipts = glob.glob('./new/receipt-[0-9]*.json')

# Initialize the subtotal
subtotal = 0.0

# Iterate over the receipts
for path in receipts:
    # Read 'content' and tally a subtotal
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # mv the file to the 'processed' directory
    name = path.split('/')[-1]
    destination = "./processed/%s" % name
    shutil.move(path,destination)
    # Print that we have processed the file
    print ("Moved %s to %s" % (path, destination))

# Print a total of all the processed receipts
print ("Receipt subtotal = %.2f" % subtotal)