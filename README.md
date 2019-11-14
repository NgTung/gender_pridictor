Gender Predictor by Vietnamese name
===================================

A funny application to predict your gender by your vietnammese name. This app using Google Tensorflow with NodeJS wrapper.

## Prepare dependencies:

- npm
- [Express framework](https://expressjs.com/ "Express framework")
- Python 3.x

## Install & Run the application:
- Install Tensorflow on Mac:
```bash
$ pip3 install --user --upgrade tensorflow
$ python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))" # verify your installation
```
- Install `npm` and start the application:
```bash
$ sudo npm install
$ sudo npm start
```
- Visit at:
`<your_host>:3000`

## Dataset
Based on 2000 student name of Hanoi UET
