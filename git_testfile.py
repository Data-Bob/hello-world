TEST-Wert = SELECTEDVALUE('TEST'[TEST])



Growth 2028 Pralinen = SELECTEDVALUE('Growth 2028'[W'tum Pralinen])
MA 2028 Pralinen = SELECTEDVALUE('MA 2028'[MA Pralinen])

Total Umsatz 2018 Pralinen = 
CALCULATE(
    [Total Umsatz];
    MasterData[Jahr] = 2018;
    MasterData[Warengruppe] = "Pralinen"
)

Total Umsatz 2018 Tafeln = 
CALCULATE(
    [Total Umsatz];
    MasterData[Jahr] = 2018;
    MasterData[Warengruppe] = "Tafeln"
)

Total Umsatz 2018 Schokoriegel = 
CALCULATE(
    [Total Umsatz];
    MasterData[Jahr] = 2018;
    MasterData[Warengruppe] = "Schokoriegel"
)


Total Sales 2028 Pralinen = 
((1+'Growth 2028'[Growth 2028 Pralinen])^10) * [Total Umsatz 2018 Pralinen]

Total Sales 2028b Pralinen = 
CALCULATE(
    SUMX(MasterData['Umsatz',
		((1+'Growth 2028'[Growth 2028 Pralinen])^10) * [Total Umsatz 2018 Pralinen]
        ( ( Sales[Order Quantity] * ( 1 + [Store Demand Value] ) ) ,
                Products[Product Name] = "Product 2" )