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

        for registro in data:
            nombre = registro['nombre']
            edad = registro['edad']
            activo = registro['activo']
            saldo = registro['saldo']
        if os.path.exists('Reporte.html') and os.path.exists('ReporteCss.css'):
            if not os.path.isdir('Personas'):
                os.mkdir('Personas')
            with open('ReporteCss.css', 'r') as file:
                css = file.read()
            with open('Personas/Registro.css', 'w') as file:
                file.write(css)
            with open('Reporte'
                      '.html', 'r') as file:
                content = file.read()
            content = content.replace('{Nombre}', nombre)
            content = content.replace('{Edad}', str(edad))
            content = content.replace('{Activo}', str(activo))
            content = content.replace('{Saldo}', str(saldo))
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
