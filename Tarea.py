import json
import os


def Confirmar():
    pregunta = input('\n desea continuar(si/no)')
    if pregunta == 'si':
        return True
    else:
        return False


def Main():
    switch = True
    while switch:
        print('Metodo para hacer un reporte en html')
        with open('json1.json') as file:
            data = json.load(file)
        nombre = []
        edad = []
        activo = []
        saldo = []
        for registro in data:
            nombre.append(registro['nombre'])
            edad.append(registro['edad'])
            activo.append(registro['activo'])
            saldo.append(registro['saldo'])
        if os.path.exists('Reporte.html') and os.path.exists('ReporteCss.css'):
            if not os.path.isdir('Personas'):
                os.mkdir('Personas')
            with open('ReporteCss.css', 'r') as file:
                css = file.read()
            with open('Personas/Registro.css', 'w') as file:
                file.write(css)
            with open('Reporte.html', 'r') as file:
                content = file.read()
                tabla = file.read()
            contador = 0
            for element in data:
                content = content.replace('{ElementosDeLista}', '<tr>\n<td><p>{Nombre' + str(contador) + '}</p></td>\n<td><p>{Edad' + str(contador) + '}</p></td><td><p>{Activo' + str(contador) + '}</p></td>\n<td><p>{Saldo' + str(contador) + '}</p></td>\n</tr>\n<b>{ElementosDeLista}</b>')
                contador += 1
            content = content.replace('{ElementosDeLista}', '')
            contador = 0
            for element in data:
                content = content.replace('{Nombre' + str(contador) + '}', nombre[contador])
                content = content.replace('{Edad' + str(contador) + '}', str(edad[contador]))
                content = content.replace('{Activo' + str(contador) + '}', str(activo[contador]))
                content = content.replace('{Saldo' + str(contador) + '}', str(saldo[contador]))
                contador += 1
            with open('Personas/' + 'Registro' + '.html', 'w') as file:
                file.write(content)
                print('La pagina se creo exitosamente')
        else:
            print('no existe el archivo')
        dirname = os.path.dirname(__file__)
        dirname += '/Personas'
        filename = os.path.join(dirname, 'Registro.html')
        os.system(filename)
        switch = Confirmar()


Main()


