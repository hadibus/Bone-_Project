from Tkinter import *
import tkFileDialog as filedialog
import ttk

class Bones:

    def __init__(self, master):
        ###get images###
            #get images for add and remove buttons
        self.plusImage = PhotoImage(file='data/plus50.gif')
        self.minusImage = PhotoImage(file='data/minus50.gif')
        self.bitmap = PhotoImage(file='data/greenBoneIcon.gif')

        ###init window###
        master.title("Bone$")
        master.tk.call('wm', 'iconphoto', master._w, self.bitmap)

        ###Step 1. Initialize all the contents###
        #init the menu
        menuBar = Menu(master)
        fileMenu = Menu(menuBar, tearoff=0 )
        fileMenu.add_command( label='Save', command=self.file_save )
        fileMenu.add_command( label='Open', command=self.file_open )
        fileMenu.add_command( label='Export', command=self.exportReport )
        fileMenu.add_command( label='Exit', command=master.destroy )
        menuBar.add_cascade( label='File', menu=fileMenu)

        helpMenu = Menu(menuBar, tearoff=0 )
        helpMenu.add_command( label='About', command=self.showAboutWindow )
        helpMenu.add_command( label='Explaination', command=self.showExplainationWindow )
        menuBar.add_cascade( label='Help', menu=helpMenu)

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


        #init the scrollbars
        aScroll = Scrollbar(master)
        lScroll = Scrollbar(master)
        rScroll = Scrollbar(master)

        #init the listBoxes
        self.albox = Listbox(master, yscrollcommand=aScroll.set, width=30, height=13 )
        self.llbox = Listbox(master, yscrollcommand=lScroll.set, width=30, height=13 )

        #init the report text
        self.reportText = Text(master, yscrollcommand=rScroll.set, width=40, height=19 )

        #init the buttons

            #buttons
        addAssetBtn = Button(master, image=self.plusImage, command=self.addAsset )
        remAssetBtn = Button(master, image=self.minusImage, command=self.removeAsset )
        addLiabBtn = Button(master, image=self.plusImage, command=self.addLiability )
        remLiabBtn = Button(master, image=self.minusImage, command=self.removeLiability )
        updateBtn = Button(master, text='Update', font=("Helvetica", 14), command=self.updateReport)

        #init the entries
        self.aDescEntry = Entry(master)
        self.aAmntEntry = Entry(master)

        self.lDescEntry = Entry(master)
        self.lAmntEntry = Entry(master)

        self.yearsEntry = Entry(master, width=6)

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
        self.reportText.insert(INSERT, 'Press Update to make report')
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
        self.albox.grid( row=0, column=2, rowspan=5 )
        self.llbox.grid( row=6, column=2, rowspan=5 )

            #column=3 scrollbars
        aScroll.grid( row=0, column=3, rowspan=5, sticky=NS )
        lScroll.grid( row=6, column=3, rowspan=5, sticky=NS ) ##INCR all cols from here

            #column=4. reportLabel, nameLabel, yearsLabel, reportText
            #exportAsLabel, exportEntry
        reportLabel.grid( row=0, column=4, columnspan=5)
        nameLabel.grid( row=1, column=4, sticky=E )
        rYearsLabel.grid( row=2, column=4, sticky=E )
        self.reportText.grid( row=3, column=4, columnspan=5, rowspan=9 )

            #column=5. two entries
        self.nameEntry.grid( row=1, column=5, columnspan=3, sticky=W )
        self.yearsEntry.grid( row=2, column=5, sticky=W )

            #column=6.
        rMonthsLabel.grid( row=2, column=6, sticky=E )

            #column=7. months combobox and export button
        self.monthsCombo.grid( row=2, column=7, sticky=W )

            #column=8
        updateBtn.grid( row=1, column=8, columnspan=2 )
        rDaysLabel.grid( row=2, column=8, sticky=E )

            #column=9
        self.daysCombo.grid( row=2, column=9, sticky=W )
        rScroll.grid( row=3, column=9, rowspan=9, sticky=NS )



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
        top.tk.call('wm', 'iconphoto', top._w, self.bitmap)
        words = 'Written by Christopher Jenkins.\n'
        words += 'Inspiration from Rich Dad Poor Dad\n'
        words += 'by Robert Kiyosaki.'
        msg = Message(top, text=words )
        okbtn = Button(top, text='OK', command=top.destroy )

        msg.pack()
        okbtn.pack()

        top.mainloop()
        top.destroy()

    def showExplainationWindow(self):
        top = Toplevel()
        top.tk.call('wm', 'iconphoto', top._w, self.bitmap)
        words = 'Bone$ is a budgeting application.  An asset is anything '
        words += 'that puts bones in your pocket, while a liabilitiy is '
        words += 'anything that takes bones out of your pocket.  An example of '
        words += 'an asset would be a paycheck(net) or a monthly allowance, while '
        words += 'an example of a liability would be money spent on gas, food, '
        words += 'a phone bill, or the internet bill.\n\n'
        words += 'A job is not usually thought of as an asset, but for the '
        words += 'purposes of this program this is ignored.\n\n'
        words += 'For calculations, a year has 365.25 days and a month has '
        words += '30.44 days on average.  This will not produce perfect '
        words += 'calculations for every situation, but for longer times it '
        words += 'more accurate.\n\n'
        words += 'Click the update button to create your report.  Good luck '
        words += 'filling up the assets list. There\'s a lot of room there!'
        msg = Message(top, text=words )
        okbtn = Button(top, text='OK', command=top.destroy )

        msg.pack()
        okbtn.pack()

        top.mainloop()
        top.destroy()

    def file_save(self):
        #top.f = filedialog.asksavefile( filetypes =((".txt files", "*.txt"), ("All files", "*.*")))
        f = filedialog.asksaveasfile( defaultextension=".bon", filetypes =((".bon files", "*.bon"), ("All files", "*.*")))
        if f is None: return

        text2save = ''
        text2save += self.nameEntry.get() + '\n'
        for line in self.albox.get( 0, END ):
            text2save += line + '\n'

        text2save += '<jksd8y9uh8yhjgidf7>\n' #signifies end of assets

        for line in self.llbox.get( 0, END ):
            text2save += line + '\n'

        text2save += '<98a98fja489h7wf89>\n' #signifies end of liabilities
        text2save += self.reportText.get('1.0',END)

        f.write(text2save)
        f.close()

    def file_open(self):
        f = filedialog.askopenfile( filetypes =((".bon files", "*.bon"), ("All files", "*.*")))
        if f is None: return

        passedEndAssets = False
        passedEndLiabs = False

        self.nameEntry.delete(0, END)  # delete the current name
        self.nameEntry.insert(0, f.readline() ) # insert new name from file

        self.albox.delete(0, END) #delete asset box contents
        self.llbox.delete(0, END) #delete liability box contents

        self.reportText.config( state='normal' ) #enable changes for text
        self.reportText.delete( '1.0', END ) #delete text

        for line in f:
            if line == '<jksd8y9uh8yhjgidf7>\n':
                passedEndAssets = True
                continue
            if line == '<98a98fja489h7wf89>\n':
                passedEndLiabs = True
                continue
            if passedEndLiabs: #in reportText
                self.reportText.insert( END, line )
            elif passedEndAssets and line != '\n': #in liabs
                line = line.rstrip()
                self.llbox.insert( END, line )
            elif line != '\n': #in assets
                line = line.rstrip()
                self.albox.insert( END, line )
        self.reportText.config( state='disabled' ) #diable text changes

    def exportReport(self):
        f = filedialog.asksaveasfile( defaultextension=".txt", filetypes =((".txt files", "*.txt"), ("All files", "*.*")))
        if f is None: return
        f.write(self.reportText.get('1.0', END))
        f.close()


root = Tk()

bones = Bones(root)

root.mainloop()
root.destroy()
