## xSky-dev

# These files are old. The website has been redesigned since then and is now run with a Quart web app.
[New repo](https://github.com/xskyyy/xsky-dev)

This repo contains the files keeping [my website](https://xsky.dev) online.

An nginx config can be found in the extras folder

## Setup
Setup is rather simple. You just need to follow these simple steps
This has been tested on Ubuntu 18.04 but should work on any recent version

1. `git clone https://github.com/xskyyy/xsky-dev`
2. `sudo add-apt-repository ppa:deadsnakes/ppa`
3. `sudo apt install python3.9`
4. `cd xsky-dev`
5. Run `python3.9 -m pip install -r requirements.txt`
6. Rename `config.sample.py` to `config.py`
7. Fill out `config.py` with the port and site name
8. `python3.9 sky.py`

Its that simple! 
You now have your own xsky.dev instance running!

The website itself was designed using [Bootstrap Studio](https://bootstrapstudio.io/).
The template file can be found in the extras folder if you wish to use Bootstrap studio to edit this site.
