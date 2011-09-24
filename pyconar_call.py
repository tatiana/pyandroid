import android
from time import sleep

droid = android.Android()

def get_contacts:
    contactos = droid.queryContent('content://com.android.contacts/data/phones',\
        ['display_name','data1'],None,None,None).result

#Se crean la lista nombres y telefonos
nombres = []
telefonos = []

#Se agrega la informacion de los contactos a las listas.
for i in range(len(contacts)):
    nombres.append(contacts[i][u'display_name'])
    telefonos.append(contacts[i][u'data1'])

#Se despliega la lista de contactos
droid.dialogCreateAlert("Contactos")
droid.dialogSetItems(nombres)
droid.dialogShow()

#Se captura el resultado de la seleccion simple
respuesta  = droid.dialogGetResponse().result

#Se muestra la informacion del contacto seleccionado
droid.makeToast('El contacto seleccionado es: %s, su numero es: %s'
                %(nombres[respuesta['item']],telefonos[respuesta['item']]))
sleep(5)
droid.makeToast("Realizando la llamada")
sleep(2)

#Se realiza la llamada al contacto seleccioando.
droid.phoneCallNumber("%s" %telefonos[respuesta['item']])

