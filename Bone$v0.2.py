from Tkinter import *
import ttk

class Bones:

    def __init__(self, master):
        ###get images###
            #get images for add and remove buttons
        self.plusImage = PhotoImage(file='plus50.gif')
        self.minusImage = PhotoImage(file='minus50.gif')
        bitmap = PhotoImage(file='greenBoneIcon.gif')

        ###init window###
        master.title("Bone$")
        master.tk.call('wm', 'iconphoto', master._w, bitmap)

        ###Step 1. Initialize all the contents###
        #init the menu
        menuBar = Menu(master)
        helpMenu = Menu(menuBar, tearoff=0 )
        helpMenu.add_command( label='About', command=self.showAboutWindow )
        menuBar.add_cascade( label='Help', menu=helpMenu)
        #init the frames
        assetFrame = Frame(master)
        liabilityFrame = Frame(master)
        reportFrame = Frame(master)

        #init the labels

        assetLabel = Label(master, text='ASSETS', font=('Helvetica', 16))
        aAddLabel = Label(master, text='add')
        aDescLabel = Label(master, text='description')
        aAmntLabel = Label(master, text='amount')
        aTimeLabel = Label(master, text='time')
        aRemLabel = Label(master, text='remove')

        liabilityLabel = Label(master, text="LIABILITIES", font=('Helvetica', 16))
        lAddLabel = Label(master, text='add')
        lDescLabel = Label(master, text='description')
        lAmntLabel = Label(master, text='amount')
        lTimeLabel = Label(master, text='time')
        lRemLabel = Label(master, text='remove')
        nameLabel = Label(master, text='Name')

        reportLabel = Label(master, text='REPORT', font=('Helvetica', 16))
        rYearsLabel = Label(master, text='years')
        rMonthsLabel = Label(master, text='months')
        rDaysLabel = Label(master, text='days')

        exportAsLabel = Label(master, text='export as')

        #init the scrollbars
        aScroll = Scrollbar(assetFrame)
        lScroll = Scrollbar(liabilityFrame)
        rScroll = Scrollbar(reportFrame)

        #init the listBoxes
        self.albox = Listbox(assetFrame, yscrollcommand=aScroll.set, width=30 )
        self.llbox = Listbox(liabilityFrame, yscrollcommand=lScroll.set, width=30)

        #init the report text
        self.reportText = Text(reportFrame, yscrollcommand=rScroll.set, width=40, height=15 )

        #init the buttons

            #buttons
        addAssetBtn = Button(master, image=self.plusImage, command=self.addAsset )
        remAssetBtn = Button(master, image=self.minusImage, command=self.removeAsset )
        addLiabBtn = Button(master, image=self.plusImage, command=self.addLiability )
        remLiabBtn = Button(master, image=self.minusImage, command=self.removeLiability )
        exportBtn = Button(master, text='Export', font=("Helvetica", 14), command=self.updateReport)

        #init the entries
        self.aDescEntry = Entry(master)
        self.aAmntEntry = Entry(master)

        self.lDescEntry = Entry(master)
        self.lAmntEntry = Entry(master)

        self.yearsEntry = Entry(master, width=6)

        self.exportEntry = Entry(master)
        self.nameEntry = Entry(master)

        #init the Comboboxes.  These are dropdowns
        self.aTimeCombo = ttk.Combobox(master, state='readonly', width=8, values=['yearly', 'monthly', 'weekly'])
        self.lTimeCombo = ttk.Combobox(master, state='readonly', width=8, values=['yearly', 'monthly', 'weekly'])
        self.monthsCombo = ttk.Combobox(master, state='readonly', width=4, values=range(0,12))
        self.daysCombo = ttk.Combobox(master, state='readonly', width=4, values=range(0,31))

        ###Step?. Configure widgets###
        self.monthsCombo.current(0)
        self.daysCombo.current(0)
        self.yearsEntry.insert(0, '1')
        self.reportText.config( state='disabled' )
        master.config( menu=menuBar )
        self.reportText.config( font="Times")

        ###Step2. Place all of the widgets by columns###
            #column=0. all labels
        assetLabel.grid( row=0, columnspan=2 )
        aAddLabel.grid( row=1, sticky=E )
        aDescLabel.grid( row=2, sticky=E )
        aAmntLabel.grid( row=3, sticky=E )
        aTimeLabel.grid( row=4, sticky=E )
        aRemLabel.grid( row=5, sticky=E )
        liabilityLabel.grid( row=6, columnspan=2 )
        lAddLabel.grid( row=7, sticky=E )
        lDescLabel.grid( row=8, sticky=E )
        lAmntLabel.grid( row=9, sticky=E )
        lTimeLabel.grid( row=10, sticky=E )
        lRemLabel.grid( row=11, sticky=E )

            #column=1. add/remove buttons, entries, comboboxes
        #skip row for ASSET label
        addAssetBtn.grid( row=1, column=1 )
        self.aDescEntry.grid( row=2, column=1 )
        self.aAmntEntry.grid( row=3, column=1 )
        self.aTimeCombo.grid( row=4, column=1, sticky=W )
        remAssetBtn.grid( row=5, column=1 )
        #skip row for LIABILITY label
        addLiabBtn.grid( row=7, column=1 )
        self.lDescEntry.grid( row=8, column=1 )
        self.lAmntEntry.grid( row=9, column=1 )
        self.lTimeCombo.grid( row=10, column=1, sticky=W )
        remLiabBtn.grid( row=11, column=1 )

            #column=2. frames containing asset/liability list & scrollbars
        assetFrame.grid( row=0, column=2, rowspan=6 )
        aScroll.pack( side=RIGHT, fill=Y )
        self.albox.pack( side=LEFT, fill=BOTH )
        liabilityFrame.grid( row=6, column=2, rowspan=6 )
        lScroll.pack( side=RIGHT, fill=Y )
        self.llbox.pack( side=RIGHT )

            #column=3. labels, reportFrame
        reportLabel.grid( row=0, column=3, columnspan=5)
        nameLabel.grid( row=1, column=3, sticky=E )
        rYearsLabel.grid( row=2, column=3, sticky=E )
        reportFrame.grid( row=3, column=3, columnspan=6, rowspan=7)
        #rScroll.grid( row=0, column=1 )
        rScroll.pack( side=RIGHT, fill=Y )
        #self.reportText.grid( row=0 )
        self.reportText.pack( side=RIGHT )
        exportAsLabel.grid( row=10, column=3 )
        self.exportEntry.grid(row=11, column=3, columnspan=3)

            #column=4. two entries
        self.nameEntry.grid( row=1, column=4, columnspan=3 )
        self.yearsEntry.grid( row=2, column=4 )

            #column=5.
        rMonthsLabel.grid( row=2, column=5, sticky=E )

            #column=6. months combobox and export button
        self.monthsCombo.grid( row=2, column=6 )
        exportBtn.grid( row=11, column=6, columnspan=3 )

            #column=7
        rDaysLabel.grid( row=2, column=7, sticky=E )

            #column=8
        self.daysCombo.grid( row=2, column=8 )



    def addAsset(self):
        desc = self.aDescEntry.get().strip()
        amount = float(self.aAmntEntry.get().strip())
        amount = "{0:.2f}".format(amount)
        tim = self.aTimeCombo.get()
        if desc == '' or tim == '' or amount <= 0:
            return #not valid entries.
        self.albox.insert(END, desc + ', $' + str(amount) + ', ' + tim )

    def removeAsset(self):
        self.albox.delete(ACTIVE)

    def addLiability(self):
        desc = self.lDescEntry.get().strip()
        amount = float(self.lAmntEntry.get().strip())
        amount = "{0:.2f}".format(amount)
        tim = self.lTimeCombo.get()
        if desc == '' or tim == '' or amount <= 0:
            return #not valid entries.
        self.llbox.insert(END, desc + ', $' + str(amount) + ', ' + tim )

    def removeLiability(self):
        self.llbox.delete(ACTIVE)

    def updateReport(self):
        #assetCalc = 0.0
        totalDaily = 0.0
        liabTotalDaily = 0.0
        years = int(self.yearsEntry.get().strip())
        months = int(self.monthsCombo.get())
        days = int(self.daysCombo.get())
        #make the report header
        rs = 'Bone$ Report - '
        rs += self.nameEntry.get().strip() + '\n'
        rs += 'Duration: ' + str(years) + ' years, ' + str(months)
        rs += ' months, and ' + str(days) + ' days.\n'
        rs += '=====ASSETS=====\n'
        #make each asset entry
        for asset in self.albox.get( 0, END ):
            rs += asset + ': ' #description, $, time:
            splitLine = asset.split(', ')
            daily = float(splitLine[1][1:])
            if splitLine[2] == 'weekly':
                daily /= 7.0 #seven days in weekly
            elif splitLine[2] == 'monthly':
                daily /= 30.44 #30.44 days in a monthly
            elif splitLine[2] == 'yearly':
                daily /= 365.25
            totalDaily += daily
            assetCalc = self.getMoneyWithTime(daily, years, months, days)
            rs += '$' + str(assetCalc) + '\n'
        assetTotal = self.getMoneyWithTime(totalDaily, years, months, days)
        rs += 'Total Assets: $' + str(assetTotal) + '\n'

        rs += '\n=====LIABILITIES=====\n'
        #make each liability entry
        for liab in self.llbox.get( 0, END ):
            rs += liab + ': ' #description, $, time:
            splitLine = liab.split(', ')
            daily = float(splitLine[1][1:])
            if splitLine[2] == 'weekly':
                daily /= 7.0 #seven days in weekly
            elif splitLine[2] == 'monthly':
                daily /= 30.44 #30.44 days in a monthly
            elif splitLine[2] == 'yearly':
                daily /= 365.25
            liabTotalDaily += daily
            liabCalc = self.getMoneyWithTime(daily, years, months, days)
            rs += '$' + str(liabCalc) + '\n'
        liabTotal = self.getMoneyWithTime(liabTotalDaily, years, months, days)
        rs += 'Total Liabilities: $' + str(liabTotal) + '\n'
        rs += '\n  Assets\n- Liabilities\n_______________\n $'
        rs += str(self.getMoneyWithTime(totalDaily-liabTotalDaily, years, months, days))
        rs += '\n\n Thank you, come again!'

        print rs
        self.reportText.config( state='normal' )
        self.reportText.delete(1.0, END)
        self.reportText.insert(INSERT, rs)
        self.reportText.config( state='disabled' )

    def getMoneyWithTime(self, daily, years, months, days):
        calc = daily * years * 365.25
        calc += daily * months * 30.44
        calc += daily * days
        return "{0:.2f}".format(calc)

    def showAboutWindow(self):
        top = Toplevel()



        top.mainloop()
        top.destroy()

root = Tk()

bones = Bones(root)

root.mainloop()
root.destroy()
