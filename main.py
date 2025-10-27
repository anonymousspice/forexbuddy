account_balance = 0
percentage  = 0
riskamount = 0 
win_rate_ratio = 0


def percentage_risk_calculation(account_balance , percentage):
   results = (percentage / 100) * account_balance
   return results

def risk_amount(riskamount,win_rate_ratio):
  results = riskamount * win_rate_ratio
  return results



def command():
   # get user for percentage risk calculation
   account_balance = float(input("enter your account balance: "))
   percentage = float(input("enter your prefereded percentage: "))

   result = percentage_risk_calculation(account_balance, percentage)
   print(f"{percentage}% of ${account_balance} = ${result:.2f}")

   
   
def command2():

   # get user risk amount to wins 
   riskamount = float(input("enter the amount you are risking: "))
   win_rate_ratio = float(input("enter your prefereded winrate: "))

   result = risk_amount(riskamount,win_rate_ratio)
   print(f" if this is a winner you will get{result} dollars")

   
   
while True:
   print("welcome! ")
   print("choose the options below") 
   print("1: percentage risk calculation") 
   print("2: risk to reward ratio")
   print("3: to quit program")
   option = str(input(""))
   if option =="1":
      command()
   if option =="2":
      command2()
   if option == "3":
      quit()
   else:
      print("eneter a valid option")   
      break






