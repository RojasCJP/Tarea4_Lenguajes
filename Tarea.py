import json
import os


def Proceso ( ) :
    print ( 'Metodo para hacer un reporte en html' )
    with open ( 'json1.json' ) as file :
        data = json.load ( file )
    name = [ ]
    age = [ ]
    active = [ ]
    saldo = [ ]
    for registro in data :
        name.append ( registro [ 'nombre' ] )
        age.append ( registro [ 'edad' ] )
        active.append ( registro [ 'activo' ] )
        saldo.append ( registro [ 'saldo' ] )
    if os.path.exists ( 'Reporte.html' ) and os.path.exists ( 'ReporteCss.css' ) :
        if not os.path.isdir ( 'People' ) :
            os.mkdir ( 'People' )
        with open ( 'ReporteCss.css' , 'r' ) as file :
            css = file.read ( )
        with open ( 'People/Registro.css' , 'w' ) as file :
            file.write ( css )
        with open ( 'Reporte.html' , 'r' ) as file :
            content = file.read ( )
        contador = 0
        for element in data :
            content = content.replace ( '{ElementosDeLista}' , '<tr>\n<td><p>{Nombre' + str ( contador ) + '}</p></td>\n<td><p>{Edad' + str ( contador ) + '}</p></td><td><p>{Activo' + str ( contador ) + '}</p></td>\n<td><p>{Saldo' + str ( contador ) + '}</p></td>\n</tr>\n<b>{ElementosDeLista}</b>' )
            contador += 1
        content = content.replace ( '{ElementosDeLista}' , '' )
        contador = 0
        for element in data :
            content = content.replace ( '{Nombre' + str ( contador ) + '}' , name [ contador ] )
            content = content.replace ( '{Edad' + str ( contador ) + '}' , str ( age [ contador ] ) )
            content = content.replace ( '{Activo' + str ( contador ) + '}' , str ( active [ contador ] ) )
            content = content.replace ( '{Saldo' + str ( contador ) + '}' , str ( saldo [ contador ] ) )
            contador += 1
        with open ( 'People/' + 'Registro' + '.html' , 'w' ) as file :
            file.write ( content )
            print ( 'La pagina se creo exitosamente' )
    else :
        print ( 'no existe el archivo' )
    dirname = os.path.dirname ( __file__ )
    dirname += '/People'
    filename = os.path.join ( dirname , 'Registro.html' )
    os.system ( filename )


Proceso ( )
