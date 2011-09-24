import android
from time import sleep

droid = android.Android()
droid.startLocating()
sleep(15)
latitud = droid.readLocation().result["network"]["latitude"]
longitud = droid.readLocation().result["network"]["longitude"]
droid.stopLocating()

droid.webViewShow("http://maps.google.com/maps?q=%s,%s" % (latitud, longitud))


