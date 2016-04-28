from Tkinter import *

def removeAsset():
    global assetList
    assetList.delete(ACTIVE)

def removeLiabilty():
    global liabilityList
    liabilityList.delete(ACTIVE)

def addAssetWindow():
    global assetList
    top = Toplevel()
    top.title("Add Asset")
    msg = Message(top, text="Adding asset?")
    msg.pack()

    ok_button = Button(top, text="OK", command=addAssetCloseTop())
    ok_button.pack()

def addAssetCloseTop():
    global top
    global assetList
    assetList.insert(END, "lololol!")
    top.destroy

def addLiablityWindow():
    pass

root = Tk()
root.title("Bone$")
bitmap = PhotoImage(file='greenBoneIcon.gif')
root.tk.call('wm', 'iconphoto', root._w, bitmap)

#assetsList = [] #this is a list of asset tuples ('description', amount, frequency)
#liabilityList = [] #this is a list of liability tuples
top = Toplevel()

plusImage = PhotoImage(file='plus50.gif')
minusImage = PhotoImage(file='minus50.gif')
leftFrame = Frame(root)
rightFrame = Frame(root)
assetFrame = Frame(leftFrame)
liabilityFrame = Frame(leftFrame)

#pack the frames into the main window
leftFrame.pack( side = LEFT )
rightFrame.pack( side = RIGHT )
assetFrame.pack( side = TOP )
liabilityFrame.pack( side = TOP )

#fill the asset frame

assetLabel = Label(assetFrame, text="- Assets -", font=("Helvetica", 16))
assetLabel.pack( side = TOP )

assetScroll = Scrollbar(assetFrame)
assetScroll.pack( side = RIGHT, fill=Y )

assetList = Listbox(assetFrame, yscrollcommand = assetScroll.set, width=35 )
#for line in range(100):
#   assetList.insert(END, "This is asset " + str(line))

assetList.pack( side = RIGHT, fill = BOTH )
assetScroll.config( command = assetList.yview )

#fill the liability frame

liabilityLabel = Label(liabilityFrame, text="- Liabilities -", font=("Helvetica", 16))
liabilityLabel.pack( side = TOP )

liabilityScroll = Scrollbar(liabilityFrame)
liabilityScroll.pack( side = RIGHT, fill=Y )

liabilityList = Listbox(liabilityFrame, yscrollcommand = liabilityScroll.set, width=35 )
for line in range(100):
   liabilityList.insert(END, "This is liability " + str(line))

liabilityList.pack( side = RIGHT, fill = BOTH )
liabilityScroll.config( command = liabilityList.yview )

#add in the buttons

addAssetButton = Button(assetFrame, image=plusImage, command=addAssetWindow)
addAssetButton.pack( side = TOP, padx = 10, pady = 10 )

removeAssetButton = Button(assetFrame, image=minusImage, command=removeAsset)
removeAssetButton.pack( side = TOP, padx = 10, pady = 10 )

addLiabilityButton = Button(liabilityFrame, image=plusImage)
addLiabilityButton.pack( side = TOP, padx = 10, pady = 10 )

removeLiabilityButton = Button(liabilityFrame, image=minusImage)
removeLiabilityButton.pack( side = TOP, padx = 10, pady = 10 )


#fill the right frame

reportLabel = Label(rightFrame, text="- Report -", font=("Helvetica", 16))
reportLabel.pack( side = TOP, fill=BOTH)

exportButton = Button(rightFrame, text ="Export", font=("Helvetica", 16))
exportButton.pack( side = BOTTOM, fill=BOTH)

mainloop()
