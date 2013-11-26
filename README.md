NRKTV.bundle
============

Plex plugin for all NRK content (tv.nrk.no, radio.nrk.no etc.)

============

State of this project as of November 2013:
Undergoing rewrite, not currently working.
Maintainers are struggling to find time to work on this between kids & family, so please come forward if you want to contribute :)

To stay up to date with the stuff we are working on, please visit the issues page:
https://github.com/eithe/NRKTV.bundle/issues

Installation: OSX (with git installed)
===============
* Open a Terminal
* Execute the following commands:

```bash
  # mkdir github
  # cd github
  # git clone git://github.com/eithe/NRKTV.bundle.git
  # cd
  # rm ~/Library/Application\ Support/Plex\ Media\ Server/Plug-ins/NRKTV.bundle
  # ln -s ~/github/NRKTV.bundle/ ~/Library/Application\ Support/Plex\ Media\ Server/Plug-ins/NRKTV.bundle
```

* Close the Terminal program

To update the plugin:
* Open a Terminal
* Execute the following commands:

```bash
  # cd github/NRKTV.bundle
  # git pull
```

* Close the Terminal program

OSX (without git installed)
* Download zip file from here: https://github.com/eithe/NRKTV.bundle/archive/master.zip
* Unzip the file
* Move the unzipped folder to your home directory into a folder called github and rename the unzipped folder to NRKTV.bundle (removing the -master suffix)
* Open a Terminal
* Execute the following commands

```bash
  # rm ~/Library/Application\ Support/Plex\ Media\ Server/Plug-ins/NRKTV.bundle
  # ln -s ~/github/NRKTV.bundle/ ~/Library/Application\ Support/Plex\ Media\ Server/Plug-ins/NRKTV.bundle
```

To update the plugin.
Redownload the zip file and replace the .bundle file found here: github/NRKTV.bundle

Other OSs
===============
We are currently not testing on Windows or Linux. If you know how to do it for any of these 
operating system we'll gladly accept a description and add it here.
