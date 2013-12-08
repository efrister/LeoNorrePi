LeoNorrePi
==========

LeoNorre Pi Knowledge Base.

Assumptions
-----------

At every point in the LeoNorriPi project, tutorials etc. we assume that the Raspbian[1] is used if nothing else stated.

Optimizing your Raspberry Pi
----------------------------

While watching the video tutorial on VPN setup[2] at the Raspberry Pi, I found some small tweaking that will improve your
Raspberry Pi performance.

* Changing the partition size of you SD-card
* Change the memory split (advance settings)
* Overclocking the processor

After booting your Raspberry Pi for the very first time, you can run the raspi-config to change the settings
mentioned above.

<blockcode>
pi@raspbian ~ $ sudo raspi-config
</blockcode>

You can now change the settings you want, I recommend to extend the partition to use the full SD-card. If you're not
running any graphical services on you Raspberry Pi, then you can easily split the memory so that the GPU have less
memory assigned e.g. 16MB.

Overclocking is always a mater of heat vs. performance, I usually never overclock my systems, but it's an option.

Links
-----
[1] http://www.raspberrypi.org/downloads
[2] http://www.youtube.com/watch?v=XkOe3tX6Tpk&feature=youtu.be