import openpyxl
class Finance(object):

    def __init__(self,filename):
        self.filename=filename
        self.COL_NO_CASH_IN=1
        self.COL_NO_PERSON=2
        self.COL_NO_CASH_OUT=3
        self.COL_NO_DESC=4
        self.COL_NO_EXPENSE_ITEM=5
        self.TOTAL_NO_FLAT_MEMBERS=6

    def load(self):
        wb=openpyxl.load_workbook(self.filename,use_iterators = True)
        worksheet = wb.get_sheet_by_name('Form Responses 1')
        sum_cash_in=0.0
        sum_cash_out=0.0
        header=True
        expense={}
        expense_dict={}
        reports={}

        for rows in worksheet.iter_rows():
            if(not header):

               cash_in=rows[self.COL_NO_CASH_IN].value
               cash_out=rows[self.COL_NO_CASH_OUT].value
               person=str(rows[self.COL_NO_PERSON].value)
               expense_item=str(rows[self.COL_NO_EXPENSE_ITEM].value)
               description=str(rows[self.COL_NO_DESC].value)

               #print type(person)
               if(type(cash_in)==float):
                   if(reports.has_key(person)):
                       reports.get(person).append(str(cash_in)+"---"+description)
                   else:
                       reports[person]=[str(cash_in)+"---"+description]
                   if(expense.has_key(person)):
                       expense[person]=expense.get(person)+cash_in
                   else:
                       expense[person]=cash_in
                   sum_cash_in=sum_cash_in+cash_in

               if(type(cash_out)==float):
                   if(expense_dict.has_key(expense_item)):
                       expense_dict[expense_item]=expense_dict.get(expense_item)+cash_out
                   else:
                     expense_dict[expense_item]=cash_out

                   sum_cash_out=sum_cash_out+cash_out
            if(header):
                header=False
        print "************** Report **********************"
        print
        print "Total Cash in ",sum_cash_in
        print "Total Cash out ",sum_cash_out
        balance=sum_cash_in-sum_cash_out
        print "Balance ",balance
        share=self.calculateEachMemberShare(sum_cash_out)
        print
        print "Total Share for each member",share
        print
        self.printPersonWiseContribution(expense)
        self.calculateFinalHisab(expense,share)
        self.printExpenseWiseReport(expense_dict)
        print "**********************************"
        self.generateItemisedReport(reports);
        #self.calculateAfterFutureExpense(sum_cash_out,expense)



    def printPersonWiseContribution(self,expense):
        print "**************Amount Paid till Now **********************"
        sum_verify_in=0.0
        for key,value in expense.iteritems():
            sum_verify_in=sum_verify_in+value
            print key,value
        #print sum_verify_in

    def generateItemisedReport(self,report):
        print "******************Cash In Report************************"
        for key,value in report.iteritems():
           print key
           print "__________"
           for det in value:
               print det
        print "\n"

    def calculateEachMemberShare(self,cash_in):
        share=cash_in/self.TOTAL_NO_FLAT_MEMBERS
        return share

    def calculateFinalHisab(self,expense,share):
       print "**************Final Hisab**********************"
       for key,value in expense.iteritems():
            bakaya=share-value
            if(bakaya<0):
                bakaya=0-bakaya
                print key,bakaya,"Extra Amount"
            else:
                print key,bakaya,"Due"

    def printExpenseWiseReport(self,expense_item):
        print "**************Category Wise Expenditure **********************"
        sum_verify_in=0.0
        for key,value in expense_item.iteritems():
            #sum_verify_in=sum_verify_in+value
            if(key=='None'):
                key='Miscellaneous'
            print key,value
        #print sum_verify_in

    def calculateAfterFutureExpense(self,cashout,expense):
        print '***************Adding Other Expense Items to be Spent*************'
        n=int(raw_input("Enter no of items to be added"))
        for i in range(n):
            expense_item_name=raw_input("Enter Expense Category")
            expense_amount=float(raw_input("Enter Amount"))
            cashout=cashout+expense_amount;


        updated_share=cashout/self.TOTAL_NO_FLAT_MEMBERS
        print
        print "Updated Share ",updated_share
        print
        for key,value in expense.iteritems():
            bakaya=updated_share-value
            if(bakaya<0):
                bakaya=0-bakaya
                print key,bakaya,"Extra Amount"
            else:
                print key,bakaya,"Due"

FILE_PATH=''
FILE_NAME="/flat-hisab/October.xlsx"
f = Finance(FILE_NAME)
f.load()
