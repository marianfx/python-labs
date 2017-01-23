
### Installation
- [From the master Stack Overflow](http://stackoverflow.com/questions/13287490/is-there-a-way-to-use-phantomjs-in-python)
- requires: [Node.js](https://nodejs.org/en/)
- to install Selenium: 'pip install selenium' (but it may be already installed)
- !IMP: Need to add phantomjs to PATH
    + the path to the phantomjs executable is (Win)`%appdata%\npm\node_modules\phantomjs-prebuilt\lib\phantom\bin`
    + append the path to the system's PATH

### Run it
- `python s_client.py "mode" "url"`
    - "mode":
        - "img": regular download of all images a site (does not further AJAX load the page)
        - "insta": for downloading pics from instagram; does special parsing to get the original (not cropped) images
            + obs: using 'img' mode on Instagram will get normal, cropped and small-sized images (thumbnails)
        - "info": only does and  request and displays some info about it
    - "url": example 'https://www.instagram.com/fxmarian/' (used with 'insta' mode)