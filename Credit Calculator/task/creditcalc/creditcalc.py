import sys
import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)
args = parser.parse_args()
if args.interest is None:
    print('Incorrect parameters.')
elif args.interest is not None:
    interest = args.interest / (12 * 100)
    if args.payment is None and args.type == "diff":
        i = 1
        total_paid = 0
        for i in range (1, args.periods + 1):

            a = args.principal / args.periods
            b = interest * (args.principal - ((args.principal * (i - 1)) / args.periods))
            monthly_payment = math.ceil(a + b)
            total_paid += monthly_payment

            over_payment = total_paid - args.principal
            print("Month {}: paid out {}". format(i, monthly_payment))
        print("\n")
        print("Overpayment = {}". format(over_payment))

    elif args.payment is None and args.type == "annuity":
        a = interest * math.pow((1 + interest), args.periods)
        b = math.pow((1 + interest), args.periods) - 1
        annuity_payment = math.ceil(args.principal * (a / b))
        over_payment = (annuity_payment * args.periods) - args.principal
        print("Your annuity payment = {}!". format(annuity_payment))
        print("Overpayment = {}". format(over_payment))

    elif args.principal is None and args.type == "annuity":
        a = interest * math.pow((1 + interest), args.periods)
        b = math.pow((1 + interest), args.periods) - 1
        credit_principal = math.floor((args.payment / (a / b)))
        over_payment = (int) (args.payment * args.periods) - credit_principal
        print("Your credit principal = {}!".format(credit_principal))
        print("Overpayment = {}". format(over_payment))

    elif args.periods is None and args.type == "annuity":
        a = 1 + interest
        b = args.payment / (args.payment - (interest * args.principal))
        month_count = math.ceil(math.log(b, a))
        year = month_count // 12
        month = math.ceil(month_count % 12)
        over_payment = (args.payment * month_count) - args.principal
        if month != 0:
            print("You need {} years and {} months to repay this credit!". format(year, month))
        else:
            print("You need {} years to repay this credit!". format(year))
        print("Overpayment = {}". format(over_payment))
