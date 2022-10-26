import csv

data_list = []
mbsum = 0
i = 1
x = 0
with open('lista.txt','r', newline='') as lis:
    
    for row in lis:
        name,cap = row.split()
        mba = float(cap)
        mb = float(mba)/(1024*1024)
        data_dic = {
        'Nr': i,
        'Usuario': name,
        'Espaco Utilizado': mb
        }
        i += 1
        mbsum += mb
        data_list.append(data_dic)

    with open('newlist.txt', 'w', newline='') as nlis:
        nlis.write("ACME Inc.               Uso do espaco em disco pelos usuarios.\n")
        nlis.write("--------------------------------------------------------------\n")
        nlis.write("Nr.\tUsuario        \tEspaco utilizado\t% do uso\n\n")
        for keys in data_list:
            n = int(keys['Espaco Utilizado'])
            newn = 100*(n/mbsum)
            keys.update({'Porcentagem do Uso': newn})
            nlis.write(str(keys['Nr']) +"\t"+ "{:<15}".format(keys['Usuario']) +"\t"+ "{0:>10.2f}".format(keys['Espaco Utilizado'])+"{:<10}".format(" MB") +"{:.2f}".format(keys['Porcentagem do Uso'])+"%"+"\n")
        nlis.write('\n\nEspaco Total Ocupado: ' + "{0:.2f}".format(mbsum) + ' MB')
        medio = mbsum/6
        nlis.write('\nEspaco medio Ocupado: ' + "{0:.2f}".format(medio) + ' MB')

        
