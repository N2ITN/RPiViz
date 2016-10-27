
# RPiViz

* Drowsiness detection in real time using computer vision. Alerts can be send via GET requests.
* Seattle Interactive 2016 T-Mobile Hackathon finalist.
* Work in progress - massive feature additions on the way.

## Real time drowsiness detection
![Alt text](/image_examples/alert.jpg?raw=true "So tired..")


## Install notes
* Tested on Raspian Jesse Pixel
* dlib is very slow to install, and pushes the limits of RPi memory!
* dlib install will only work in headless mode with GPU memory set to 64  (use ``` raspi config ``` )

### Bash:

Configure Pi for headless, low VRAM mode
* ``` sudo raspi config ```
  * command line boot
  *  gpu memory to 64 MB
  * accept reboot prompt

Clone and download system dependencies

```bash
git clone https://github.com/N2ITN/rpiviz
cd rpiviz
chmod +x get_reqs.sh
bash get_reqs.sh
```

## Run

```python
python
>>> import executor
>>> executor.run()
```




## License 
Apache License 2.0.
