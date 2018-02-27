
#An electricity bill estimator. Takes user input and
#produces an estimate electricity bill based off the input

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_or_rate = float(input("Use Tariff Number or Rate (Cents per kWh)? "))
#cents_per_kWh = float(input("Enter cents perkWh: "))/100"""
tariff_selection = float(input("Which Tariff? 11 or 31: "))
if float(tariff_selection) == 11:
    cents_per_kWh = TARIFF_11
elif float(tariff_selection) == 31:
    cents_per_kWh = TARIFF_31
else:
    print("Unknown Tariff, please Reselect")

daily_use_kWh = float(input("Enter Daily use in kWh: "))
number_of_billing_days = float(input("Enter number of billing days: "))

estimated_bill = (cents_per_kWh * daily_use_kWh * number_of_billing_days)
print("Estimated bill: $",estimated_bill)

