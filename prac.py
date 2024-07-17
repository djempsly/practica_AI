#Este archivo es para practicar Inteligencia Artificial

polocher = "Poloche es el término que se usa en la República Dominicana para denominar una prenda de punto que llega hasta la cintura, con cuello, y abotonada por delante en la parte superior."

negro = "negro"

polocher_negro= "Poloche es el término que se usa en la República Dominicana para denominar una prenda de punto que llega hasta la cintura, con cuello, y abotonada por delante en la parte superior."

promt = input('Busca el tipo de tu vestimenta ')

if 'hasta la cintura' in promt and negro:
    print('es un polocher negro')
else:
    print('NO tengo esta inforamción')