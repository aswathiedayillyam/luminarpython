#withdrawel,deposit,balanceenq
#createaccount


class Bank:

    def create_account(self,acno,personname,minimumbalance,bankname):
        self.acno=acno
        self.p_name=personname
        self.balance=min_balance
        self.bank_name=bankname

    def deposit(self,amount):
        self.balance+=amount

        print("your account",self.acno,"has been credicted with amt",amount,"on",datetime.today(),"avl bal",self.bal)
