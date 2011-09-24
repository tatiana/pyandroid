import android
from time import sleep

droid = android.Android()
droid.startLocating()
sleep(15)
latitud = droid.readLocation().result["network"]["latitude"]
longitud = droid.readLocation().result["network"]["longitude"]
droid.stopLocating()

#telefono = "1167916111"
telefono = "1165272786"
#telefono = droid.dialogGetInput(" GPS to SMS", "Phone number:")
mensaje = "Estoy en http://maps.google.com/maps?q=%s,%s" % (latitud, longitud)
droid.smsSend(telefono,mensaje)
