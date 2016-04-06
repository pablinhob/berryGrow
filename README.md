berryGrow
===============
An open controller for your grow rom

# Credits #
* Pablo Blanco: software and hardware design . https://github.com/pablinhob/
* Iria Varela: berryGrow Logo . http://onegrovaicontodo.tumblr.com/


# Python dependences #
* >pip install flask
* >pip install schedule
* >pip install RPi.GPIO

# Using libraries #
* JQuery
* Underscore.js
* Bootstrap
* Greyscale theme https://github.com/IronSummitMedia/startbootstrap-grayscale
* Ion icons http://ionicons.com/
* Clockpicker https://github.com/weareoutman/clockpicker
* Ion.rangeSlider https://github.com/IonDen/ion.rangeSlider


# SD Backup and restore #
Do image of your berrygrow system
``` sudo dd bs=4M if=/dev/sdb | sudo gzip > /home/your_username/image`date +%d%m%y`.gz ```

Restore or install image
``` sudo gzip -dc /home/your_username/image.gz | sudo dd bs=4M of=/dev/sdb ```

Thanks to: https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=46911
