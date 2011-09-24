import android

droid = android.Android()
name = droid.dialogGetInput("Hello!", "What is your name?")
droid.makeToast("Hello %s! Grat to see you in PyConAr" % name.result)
