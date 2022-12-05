'''
This Program is written NOT by me, but rather the website which the classroom had posted. I (Ayesha,) am here simply to run this code and learn from it.
'''

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Coding Companion for Intuitive Deep Learning Part 2 (Annotated)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The medium post for this notebook is [here](https://medium.com/@josephleeweien/build-your-first-convolutional-neural-network-to-recognize-images-84b9c78fe0ce).\n",
    "\n",
    "In this notebook, we'll go through the code for the coding companion for [Intuitive Deep Learning Part 2](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-2-cnns-for-computer-vision-24992d050a27) to create your very first Convolutional neural network to predict what is contained within the image (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and truck). We will go through the following in this notebook:\n",
    "\n",
    "- Exploring and Processing the Data\n",
    "- Building and Training our Convolutional Neural Network\n",
    "- Testing out with your own images\n",
    "\n",
    "Note that the results you get might differ slightly from the blogpost as there is a degree of randomness in the way we split our dataset as well as the initialization of our neural network."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exploring and Processing the Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will first have to download our dataset, CIFAR-10. The details of the dataset are as follows:\n",
    "- Images to be recognized: Tiny images of 32 * 32 pixels\n",
    "- Labels: 10 possible labels (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and truck)\n",
    "- Dataset size: 60000 images, split into 50000 for training and 10000 for testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Using TensorFlow backend.\n"
     ]
    }
   ],
   "source": [
    "from keras.datasets import cifar10\n",
    "(x_train, y_train), (x_test, y_test) = cifar10.load_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x_train shape: (50000, 32, 32, 3)\n"
     ]
    }
   ],
   "source": [
    "print('x_train shape:', x_train.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "y_train shape: (50000, 1)\n"
     ]
    }
   ],
   "source": [
    "print('y_train shape:', y_train.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will now take a look at an individual image. If we print out the first image of our training dataset (x_train[0]):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 59  62  63]\n",
      "  [ 43  46  45]\n",
      "  [ 50  48  43]\n",
      "  ...\n",
      "  [158 132 108]\n",
      "  [152 125 102]\n",
      "  [148 124 103]]\n",
      "\n",
      " [[ 16  20  20]\n",
      "  [  0   0   0]\n",
      "  [ 18   8   0]\n",
      "  ...\n",
      "  [123  88  55]\n",
      "  [119  83  50]\n",
      "  [122  87  57]]\n",
      "\n",
      " [[ 25  24  21]\n",
      "  [ 16   7   0]\n",
      "  [ 49  27   8]\n",
      "  ...\n",
      "  [118  84  50]\n",
      "  [120  84  50]\n",
      "  [109  73  42]]\n",
      "\n",
      " ...\n",
      "\n",
      " [[208 170  96]\n",
      "  [201 153  34]\n",
      "  [198 161  26]\n",
      "  ...\n",
      "  [160 133  70]\n",
      "  [ 56  31   7]\n",
      "  [ 53  34  20]]\n",
      "\n",
      " [[180 139  96]\n",
      "  [173 123  42]\n",
      "  [186 144  30]\n",
      "  ...\n",
      "  [184 148  94]\n",
      "  [ 97  62  34]\n",
      "  [ 83  53  34]]\n",
      "\n",
      " [[177 144 116]\n",
      "  [168 129  94]\n",
      "  [179 142  87]\n",
      "  ...\n",
      "  [216 184 140]\n",
      "  [151 118  84]\n",
      "  [123  92  72]]]\n"
     ]
    }
   ],
   "source": [
    "print(x_train[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to see the image as an image rather than a series of pixel value numbers, we will use a function from matplotlib:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAP8AAAD8CAYAAAC4nHJkAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAH3FJREFUeJztnVuMXNd1pv9Vt67qezf7QrJJiRJ1GcmxRMmMIEiZjB3PBIoRRDaQZOwHQw9GGAQxEAPJg+AAYw8wD/ZgbMMPAw/okRJl4PFlfImFQJjEEWwIiQNFlCXrHomiKLHJVrPJ7mZ3dVXXdc1DlyZUa/+bJTZZTWn/H0B0ca/a56zaddY5VeevtZa5O4QQ6ZHZbgeEENuDgl+IRFHwC5EoCn4hEkXBL0SiKPiFSBQFvxCJouAXIlEU/EIkSm4rk83sHgBfB5AF8D/d/Uux5+fzee8rFoO2VqtF52UQ/hVi1vi+Cjl+XstHbLlsltrMwjs0i5xDIz42m/w1x353mY35SH6x2fY231eb780ykRcQod0Ov7aY79HtRfy3yCIzWybiRzbD3092DABAO/JrWY8dCGxOdHthFpdXUa6sd7Wziw5+M8sC+O8A/gOAWQBPmNnD7v4Cm9NXLOLA7R8K2paXF+m++jLhN368wBfnqh391DY5PkBtE6OD1FbI5oPjub4SnYMsX+LFpWVqqzf5axsbHaG2TKsRHK/VanTO+vo6tRVL4ZM1ALTAT16Vajk4PjI6TOfA+fbqtTq1ZRF+XwB+shka5O/zwAA/PvJ5vh7ViI8eu0BkwsdI7DU3PRzfX37gB3w/m3fb9TPfyR0Ajrr7MXevA/gOgHu3sD0hRA/ZSvDPADhx3v9nO2NCiPcAW/nOH/rc8Y7PqmZ2CMAhAOjr69vC7oQQl5KtXPlnAew97/97AJza/CR3P+zuB939YC7Pv5sJIXrLVoL/CQDXm9k1ZlYA8EkAD18at4QQl5uL/tjv7k0z+yyAv8WG1Peguz8fm7O+vo7nXwg/ZfnMGTpvnNxgtR38zutEa4jarDRFbWttrjqUW+E78G4FOqeyzu/YVqr8DnyjxaWtMxGNs5gL+9hs8u1lyd1mIP5VrbK+Rm3Ndvh12/oOOicTUQEbEbWilOPHQZncMV9sNemc/n5+t98y/NOrETUIABCRDyvrYYWm2QiPA0A2F35fGutV7sMmtqTzu/sjAB7ZyjaEENuDfuEnRKIo+IVIFAW/EImi4BciURT8QiTKlu72v1syAEo5IlNFfvx3NZH09k3zBJepyXFqK8WknEjWVrUWToBZb3AZyiPbK5QiCUGRxB5v8/2NjIcTmpoNvr1CnvsRSbZEtsDftFo9vFaNJl+P/sj2cgPcx2JkXtPCcmQmkiXYjGTgxTJJBwd4Mll5rUJtjWZY0oslVK6unAuOt2Nv2Obtd/1MIcT7CgW/EImi4BciURT8QiSKgl+IROnp3X4zR9HCCRVDQ9yVG2bGguM7SjwTJN/mpanKizzZptXm58NqJex7huf1YDhSFiwXuUu9fG6Vz4u8a+ND4TvOqys8CaceSdCpkqQTIF6XbpCUwmrUeeJJpsVfWD6SYNQipcsAIEduz9dqfE4hz9/QTJsnBNXKS9QGkhQGAH3kMG62uSJxbi2s+LQi9Rg3oyu/EImi4BciURT8QiSKgl+IRFHwC5EoCn4hEqWnUl/ODGN94V2WIlLOCEnqmBzmNdNapF0UgEifGSCbixSSI3XYau2I1BTR5XKR5JJWjUtinuXn7NOnw12AWg3+qlcrPOmk0uKy6GAp0n2nRtp1gb/mjHGZKtsX6ZSzxmXd/nzYx1ykFdZ6pO5itcGlvnakydpymfu4XAkfP2UiLQPAeiN8DNQjtRo3oyu/EImi4BciURT8QiSKgl+IRFHwC5EoCn4hEmVLUp+ZHQewig31rOnuB6M7yxomR8OSzVCeS2zFYtiWyXJppRSpj9doctmrHclUcw9LQPVIvb1WncuAbY9kzEUkNs/xrLPVejhDr9Xi61uJtAZrRmyra9z/k4thP/IZvr3hMl/7xpu8nVv1HJcqr5q4Ljg+NbWHzrGhcH08AKgtnaW2cplnR55b5VLfmXNhWff4Ce5HKxsO3Vqdy4ObuRQ6/0fcnb8zQogrEn3sFyJRthr8DuDvzOxJMzt0KRwSQvSGrX7sv9vdT5nZFICfmNlL7v7Y+U/onBQOAUAx8r1eCNFbtnTld/dTnb+nAfwIwB2B5xx294PufrCQ07cMIa4ULjoazWzAzIbeegzgNwE8d6kcE0JcXrbysX8awI867a1yAP63u//f2IR8Lovdk+HCjsMFLlEM9oelLYtIZYhkWFkkm65W5bJRhsiAO4Z427CBAZ6NtnKOiyQjwzxjbjVSVPP1k+Ftlmv8K1chkgg20x/JSszzzMPjZ8PZhTWPFF2NZPWNDA9R2103c4V5ZS4s63olsq8Jni1aq/D1KJf5tbQvz7e5d2f4tU1NTdM58yth6fDsy2/SOZu56OB392MAbr3Y+UKI7UVfwoVIFAW/EImi4BciURT8QiSKgl+IROltAc+sYXwonG2Xq4elIQDoy4fd7O8L96UDgFqVy2GNSL+10dFwX0AAcFL0sd7i59BGI1JccpD38Tu1EO7FBgCvvs6zvRZWw68tUgsSV0d6Hn783x6gtj27uP/ff/JYcPyfjnIpqtnmmYy5DJfmVpcXqK1SDq/j0BCX3tDi2YXFIp9XINmnANBvfF6zFX5zrtq7m84ZWgz3cnzmNb4Wm9GVX4hEUfALkSgKfiESRcEvRKIo+IVIlN7e7c/lMDW+I2irLvK74hkLu1kmbY4AoBqpZZazSD27SFsrdqasNvhd6tExnqBTb/E72MdmT1Hb4gr3kdX3y0ZafA0X+famcuG7ygBQXOSKxPXDO4Pjc+Pcj/nl09RWq/A1furll6ktQ9pXNQYircZGeEINMjxkRka4+jTUjrQHI3Uevb5C5+wjCXJ9+e6v57ryC5EoCn4hEkXBL0SiKPiFSBQFvxCJouAXIlF6LPXlMTYxGbSNDfL2WplMOClieWWJzmmslfn2WrF2XbygnZMEo8FBXqevAW578RiXqNZqvPVTsdjHbYWwj6UBLkONZbks+uTReWpr1vnhUxsJS32TY3w9DFx+azS5FFyp81qCa6RWX73JX7NFpNtINzfkM5FWb5lI7cJceB2bNS6lOpGJSe5ZEF35hUgUBb8QiaLgFyJRFPxCJIqCX4hEUfALkSgXlPrM7EEAvw3gtLv/SmdsHMB3AewDcBzA77s7193+dWsAke0s0s6I0Repp9aPcNYTAOQi57xMJlKPj8iAfSXeruvMmzwrrnKGL9m141wSq3HVC0Ui6d24f4bOyUQ22MzyNV6JSK25bLjO4FCBvy87xvZT2/7rr6K21954gtpeevlkcLyQi8hozmXiZpOHTIZkVAJAvsDXsd0OH1ftiK5oFj5OI0rkO+jmyv+XAO7ZNHY/gEfd/XoAj3b+L4R4D3HB4Hf3xwAsbhq+F8BDnccPAfj4JfZLCHGZudjv/NPuPgcAnb9Tl84lIUQvuOw3/MzskJkdMbMjq5XIl1UhRE+52OCfN7NdAND5S+svufthdz/o7geH+vlNLCFEb7nY4H8YwH2dx/cB+PGlcUcI0Su6kfq+DeDDACbMbBbAFwB8CcD3zOwzAN4A8Hvd7Kztjup6uFihNXhmFhDOwFpb4wUO6w1+Xmtm+CeQcoVLcyvENrOXL6M3+faunuDCzP7dXBqqrPN5MzfcGhwvOP/KtXSOF0ItjYYLrgIAzvJMtb07dwXHl9d4tuK1/+Z6ahse41mJw2M3UdvSQnj9l87xlmf5iByZcZ5R2WhHskV5sihajfDxHUkSpK3j3kVS34WD390/RUwffRf7EUJcYegXfkIkioJfiERR8AuRKAp+IRJFwS9EovS0gKfD0bKwHOItXlCRyRqlIi/6OTjEpaFTC1xWfG12gdpy+bAfhXneV299nm/v+iku5330w1z2evXk5lSLf2VoJlwgdWJHuKAmAJxe4EU6R0cjsleb+18gBStPL4Sz7AAgV1ymtoXlOWo7Ocez8PL58HEwOsy1t2qVC2ae49dLi2hz7YgMmLHwPItkmEbaPHaNrvxCJIqCX4hEUfALkSgKfiESRcEvRKIo+IVIlJ5KfdlsBqOjg0FbM8elvnI5nJHmDS6fnFvlWVuvv8GlrXKZy0alYvhcOfcazy6cLvKijjMzV1Pb6O5rqC2/GkkRI0VN99x6B5/yJpffSk0uVbbAMwXX1sK2Xf1hKRIA6i3+umwgfNwAwJ6B3dQ2NBqWOFfPvknnnJ4/S20N4/Lmep0XBUWGa3MDfeEs03o1ImGSgqBGZMOgS10/UwjxvkLBL0SiKPiFSBQFvxCJouAXIlF6ere/3WpidTl8JzVX57Xu8qQ1EXgJOeSy3FgpcyVgbIgnsowOhO/KVpf43f6p3bwG3swt/47anputU9vLR7ntrl3jwfHlZT5nen+47h8AZFChtnqNKwGjHr5zv3Ka30kv1XktwV3j4dcFAMstXlcvf8tYcLwaSRT6x0ceprbZE/w1ZyMtuWKNtFgeUSPWVq4RXiuWBBfcRtfPFEK8r1DwC5EoCn4hEkXBL0SiKPiFSBQFvxCJ0k27rgcB/DaA0+7+K52xLwL4AwBv6R6fd/dHutlhligerUgSgxOZJEPaeAFAy7jUt8QVJaysROq31cJy2a4RLg/+6kc+Qm17bryT2n74Fw9S285Ikku2Hq5PePLYq3x7195MbcUd11HbgHN5trIY7t1aaoelNwCoV7mseGaV20YneRLUjp37guPV8jCdk+EmtAo8mSlWw6/R4FKrNcMJauY8ca3ZDIfupZb6/hLAPYHxr7n7gc6/rgJfCHHlcMHgd/fHAPBysUKI9yRb+c7/WTN7xsweNDP+WU4IcUVyscH/DQD7ARwAMAfgK+yJZnbIzI6Y2ZFyhX/vEUL0losKfnefd/eWu7cBfBMALRPj7ofd/aC7Hxzs51VthBC95aKC38x2nfffTwB47tK4I4ToFd1Ifd8G8GEAE2Y2C+ALAD5sZgcAOIDjAP6wm50ZACNKRItkKQG8bVGkcxK8GtlepATe+A7e5mtnf1havP3gDXTOTXdxOW/pNJc3+5o88/DaPXuorU1e3M4pXjuvuc4l00okG7De5PMa1fCh1QKXKV89OUttzz53hNruupP7uGNnOKtyZTUsRQIA6fAFAJjYx2Xddqy9Vj0i2xEJ+dwCb19WWw072SbZlCEuGPzu/qnA8ANd70EIcUWiX/gJkSgKfiESRcEvRKIo+IVIFAW/EInS0wKe7kCbZDBVa1yiKJAstlyOF0zMZrj8c91O/mvkYomfD/ddvTc4fuuv8cy9XTfeQm1P/9NfUNtVe7mPOz/wQWorTO4Pjuf6R+icyjqXHKsrPHNv/tQJaluaD8t2rQbPzisNhQukAsDEBH+vT5x6itqmd80Ex5uVSBZplbfdsrUlamt5OKMSAJxp3ABKfeHXVtjJX/NKH8l0fRcRrSu/EImi4BciURT8QiSKgl+IRFHwC5EoCn4hEqWnUp+ZIZ8N73IpUqCxtR6WNUr9JTonm+HSylQkc+/EHM+k2n97qJQhsOeD4fENuGTXWF2jtpEhLs1N3nCA2tZy4Z52zz/1BJ1Tq3I/Vlb4epw5+Qa1ZVthqbVY5IfczDVhWQ4AbrmBFxJtZnmmXT47Gh4v8KzP3Dov0ll5/SS1MRkbAJqRy2yZ9JXs38Ff1zTpAZnPd38915VfiERR8AuRKAp+IRJFwS9Eoij4hUiU3ib2tNuoVcN3Uvv7uCtWDN8NzWd4DTlvcVtpkLfy+p3/+DvUdtdvfTQ4PjwxTefMH3uR2rIR/5dXeQ2/heP/Qm2nVsN3nH/2139N5wyWeALJeo0nwOyc5orE8FD4TvVrszwZqB5Zj/Hd+6jthg9+iNrQ6gsOLy7zeoEVoi4BwFKV+2jOj+H1Kk9cK5MWW17mqsNNYRED7e67denKL0SqKPiFSBQFvxCJouAXIlEU/EIkioJfiETppl3XXgB/BWAngDaAw+7+dTMbB/BdAPuw0bLr992dFzgD4HC0ndTWa/OkCGuGZZKmR1pyRWqmFfuGqe3Ah7hs1JcPS2IvPM1ryC2depXaajUu5awuLVLbiaMvUFvZw8lO+Rbf12COS5/DRZ5cMjnGpb65+TeD481IW7bKKpcVT7zGk4iA56mlXA7XICzm+PHR7JuitrNNfuyUSrwGYf8QT0Ir5cJy5Gplhc5ptsOS47tQ+rq68jcB/Km73wTgTgB/bGY3A7gfwKPufj2ARzv/F0K8R7hg8Lv7nLv/ovN4FcCLAGYA3Avgoc7THgLw8cvlpBDi0vOuvvOb2T4AtwF4HMC0u88BGycIAPyzkhDiiqPr4DezQQA/APA5d+dfRt4575CZHTGzI2tVXktfCNFbugp+M8tjI/C/5e4/7AzPm9mujn0XgGDDc3c/7O4H3f3gQKlwKXwWQlwCLhj8ZmYAHgDwort/9TzTwwDu6zy+D8CPL717QojLRTdZfXcD+DSAZ83s6c7Y5wF8CcD3zOwzAN4A8HsX3pRjQy18J+0m/0qQy4dr7rUiNdPq4NlX0yO8rt7fPvw31DY+HZaUpnaF23gBQL3Cs/Py+bDEAwCDA1xSymW4NDdA5MidU+GabwBQXeUKbSnLfTy7cIbaGvXwezNU5JJXvcylvleeOkJtcy+9TG21Jmmhledr2Iqt7x4ufWKAH8OZPi61FolsNwa+Vjd94JrgeKl4jM7ZzAWD393/AQDLcQznuAohrnj0Cz8hEkXBL0SiKPiFSBQFvxCJouAXIlF6WsATbmi3w8JBIZJZVsyR4ocZXmjRIy2c2nWeWXbmTDgbDQDKC2FbqcF/8NgGf13jY1x+G909SW3NVo3aTp4K++iRfK9Mhh8G9SaXTLPGC38OFMPyLEnQ3NhezBjJ0mzVuZyaIcfbSoXLm/U+Ig8CGNrN136txFubrba5DLi+Fr4G7xi+ls6ZINJtLt99SOvKL0SiKPiFSBQFvxCJouAXIlEU/EIkioJfiETprdQHQ8bCWWLFPp7B5CRDb6AUlpMAYGBogtoqDZ5htWOI1xzIET/q5+bpnHaGb6+S59LW9HQ4awsA2nUuG914y57g+M9/+iidU/cKteWNy6nVMp83PBTOSizk+CGXtUg/u3X+nr02x2W75eXwe1azNTpn8gZ+TZwZjWQlOn+vl87wtSqshyXTgZlIJmYlnDXZjqilm9GVX4hEUfALkSgKfiESRcEvRKIo+IVIlJ7e7c8YUMiFzzeVGk+YyJKWUe1IfblKgydnZPM8SaSvwO/m5vNhPwr9vG3VyDBPMHpzgasElZnwXXsAmNp7HbWdPB2uq/eBX72bzikvnKK2Yy/zVlhrZZ7IksuG139khNcmNFLfEQDmTnIf33g9ktjTF17/4WmuFE2OR3yMqA62yN/rsSUeajNT48HxPaP8GDj6QjiBq1blSWub0ZVfiERR8AuRKAp+IRJFwS9Eoij4hUgUBb8QiXJBqc/M9gL4KwA7sdFr67C7f93MvgjgDwAsdJ76eXd/JLqznGF6Mny+aZw9S+dVW2EJaI3nZsAzvJVXLpJcMjzMkykKpBVWdY3X8CvFaqrVue3Iz39ObdfeyCXC2dmwBJSJ1Dvs7+O1+LIRObVU4tLWWjks9VWrXIJtRlq2DZa4H3fddgO1FUmCUTPLaxO2GjwJp3qCS32Z1SK1TfUPUdttN3wgPGd0ms55cu614HizwV/XZrrR+ZsA/tTdf2FmQwCeNLOfdGxfc/f/1vXehBBXDN306psDMNd5vGpmLwKYudyOCSEuL+/qO7+Z7QNwG4DHO0OfNbNnzOxBM+Otb4UQVxxdB7+ZDQL4AYDPufsKgG8A2A/gADY+GXyFzDtkZkfM7MhKhX+nE0L0lq6C38zy2Aj8b7n7DwHA3efdveXubQDfBHBHaK67H3b3g+5+cLifVzoRQvSWCwa/mRmABwC86O5fPW9813lP+wSA5y69e0KIy0U3d/vvBvBpAM+a2dOdsc8D+JSZHQDgAI4D+MMLbahQMFy1N3z1HzEukxw9EZZe5hd4dl69xaWhwUH+stcqPEOs1S4Hx7ORc+jiApcwV8tclllvcD+yzm1Dg+FbL/NvLtI5s2tcvmo7lwinJ7ksau1wdtnSMq+31zfA37PRES6VFbJ8/Wt1IvnmuLy5VuPbq5cjLcrafN51e3dS2+6d4XU8Mcsl3bML4ZhoxlqebaKbu/3/ACB0BEQ1fSHElY1+4SdEoij4hUgUBb8QiaLgFyJRFPxCJEpPC3hmc4bhMZIZR6QLABibyoYNA7wI45l5XhB0PdLuKlfgxRvZtHaDZxA2WtyPc1Uuew1EstjWK1yaq66HC3jWIz62IjZ3svYAyiuRdl3D4UKow8O82Gm1yrd35ixfq8FBnl1omfD1zZpcJi7keBHXPq5Io1Dga7Xvun3UVq2EfXnssRfonGdePh3e1nr3WX268guRKAp+IRJFwS9Eoij4hUgUBb8QiaLgFyJReir1mRlyxfAui8M81398MHyOylW5jJYv8eymlUjfNLT4+bBUnApPyfN9tWq8n12hn/uRz/H1yGa5xFnzsC/1Bpc3PZK5Z1wRg9e55Ngipnwkmw4FLm8uL3Gpr1rn/elGRsPSbY5IgACQiax9BVxKmz+zSm1LkQzO1bVwlubf/+wlvi+iiq7XJfUJIS6Agl+IRFHwC5EoCn4hEkXBL0SiKPiFSJSeSn3ttqHMCiBmB+m8wYGwbpQvcR1qIJJ+NTLCpbnyCu8lV14JF1QsVyJZfevcNlTgBTCLpC8gADRrXOLM5cLn80LkNJ/v49loZnxif6QQaoaYmi0uRRVKkR6Ko1zeXFzkEtsqkT6Hx/naVyI9A185zguyvvTsCWqbHufZotN7yGvL8ON0ghQ0nV/lsuc7Nt/1M4UQ7ysU/EIkioJfiERR8AuRKAp+IRLlgnf7zawI4DEAfZ3nf9/dv2Bm1wD4DoBxAL8A8Gl3j7bhrdeB2dfDttoyvzs/NBm+Q1wsRRI6uHiA8XH+sstrvI7c8nLYtnSWJ4Is8ZvDyLb5Xfa2cyWj1eIKAtphW+wsbxme2JPN8bWqRpKgnNzUz5M2XgDQrPCWYq1Ifb9WJFlouRyex7p4AcBiRPE5fpS/octn16itvsZ3uHMk3Mrrpqtn6Bzm4itvrtA5m+nmyl8D8Bvufis22nHfY2Z3AvgygK+5+/UAlgB8puu9CiG2nQsGv2/wVofKfOefA/gNAN/vjD8E4OOXxUMhxGWhq+/8ZpbtdOg9DeAnAF4FsOz+/z/czQLgn1GEEFccXQW/u7fc/QCAPQDuAHBT6GmhuWZ2yMyOmNmRc2Ve/EEI0Vve1d1+d18G8DMAdwIYNbO37gbtAXCKzDns7gfd/eDIYKTjgRCip1ww+M1s0sxGO49LAP49gBcB/BTA73aedh+AH18uJ4UQl55uEnt2AXjIzLLYOFl8z93/xsxeAPAdM/svAJ4C8MCFNuSWQys/EbQ1CgfpvFo7nMiSaYZbUwFAcYTLV6OT/BPIWIYnnoxXwokWy4u8vdPyGS7nVdf48reaXD6E83N2uxn2cb3Kv3IVCpF6gTnu/+o6Tzypkq94+YgaPJQJJ6sAQDvDJaxGg69j30BYMi3meb3A0QL38VqMUtsHb+Vtw2685VZq23fddcHxO+7k8ubsqXJw/B9f5TGxmQsGv7s/A+C2wPgxbHz/F0K8B9Ev/IRIFAW/EImi4BciURT8QiSKgl+IRDGPZI9d8p2ZLQB4K69vAkD3usTlQ368Hfnxdt5rflzt7pPdbLCnwf+2HZsdcXcu7ssP+SE/Lqsf+tgvRKIo+IVIlO0M/sPbuO/zkR9vR368nfetH9v2nV8Isb3oY78QibItwW9m95jZv5jZUTO7fzt86Phx3MyeNbOnzexID/f7oJmdNrPnzhsbN7OfmNkrnb9j2+THF83sZGdNnjazj/XAj71m9lMze9HMnjezP+mM93RNIn70dE3MrGhm/2xmv+z48Z8749eY2eOd9fiumUVSP7vA3Xv6D0AWG2XArgVQAPBLADf32o+OL8cBTGzDfn8dwO0Anjtv7L8CuL/z+H4AX94mP74I4M96vB67ANzeeTwE4GUAN/d6TSJ+9HRNABiAwc7jPIDHsVFA53sAPtkZ/x8A/mgr+9mOK/8dAI66+zHfKPX9HQD3boMf24a7PwZgc53qe7FRCBXoUUFU4kfPcfc5d/9F5/EqNorFzKDHaxLxo6f4Bpe9aO52BP8MgPPbmW5n8U8H8Hdm9qSZHdomH95i2t3ngI2DEMDUNvryWTN7pvO14LJ//TgfM9uHjfoRj2Mb12STH0CP16QXRXO3I/hDJXa2S3K4291vB/BbAP7YzH59m/y4kvgGgP3Y6NEwB+ArvdqxmQ0C+AGAz7l7990nLr8fPV8T30LR3G7ZjuCfBbD3vP/T4p+XG3c/1fl7GsCPsL2ViebNbBcAdP6e3g4n3H2+c+C1AXwTPVoTM8tjI+C+5e4/7Az3fE1CfmzXmnT2/a6L5nbLdgT/EwCu79y5LAD4JICHe+2EmQ2Y2dBbjwH8JoDn4rMuKw9joxAqsI0FUd8Ktg6fQA/WxMwMGzUgX3T3r55n6umaMD96vSY9K5rbqzuYm+5mfgwbd1JfBfDn2+TDtdhQGn4J4Ple+gHg29j4+NjAxiehzwDYAeBRAK90/o5vkx//C8CzAJ7BRvDt6oEfv4aNj7DPAHi68+9jvV6TiB89XRMAt2CjKO4z2DjR/Kfzjtl/BnAUwP8B0LeV/egXfkIkin7hJ0SiKPiFSBQFvxCJouAXIlEU/EIkioJfiERR8AuRKAp+IRLl/wHCOW2RBgdIrQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "img = plt.imshow(x_train[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The label is: [6]\n"
     ]
    }
   ],
   "source": [
    "print('The label is:', y_train[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's explore one more image, the second image (with index 1 instead of 0) in our training dataset:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "img = plt.imshow(x_train[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The label is: [9]\n"
     ]
    }
   ],
   "source": [
    "print('The label is:', y_train[1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What we really want is the probability of each of the 10 different classes. For that, we need 10 output neurons in our neural network. Since we have 10 output neurons, our labels must match this as well. To do this, we convert the label into a set of 10 numbers where each number represents if the image belongs to that class or not. So if an image belongs to the first class, the first number of this set will be a 1 and all other numbers in this set will be a 0. To convert our labels to our one-hot encoding, we use a function in Keras:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import keras\n",
    "y_train_one_hot = keras.utils.to_categorical(y_train, 10)\n",
    "y_test_one_hot = keras.utils.to_categorical(y_test, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The one hot label is: [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]\n"
     ]
    }
   ],
   "source": [
    "print('The one hot label is:', y_train_one_hot[1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A common step we do is to let the values to be between 0 and 1, which will aid in the training of our neural network. Since our pixel values already take the values between 0 and 255, we simply need to divide by 255."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train = x_train.astype('float32')\n",
    "x_test = x_test.astype('float32')\n",
    "x_train = x_train / 255\n",
    "x_test = x_test / 255"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0.23137255, 0.24313726, 0.24705882],\n",
       "        [0.16862746, 0.18039216, 0.1764706 ],\n",
       "        [0.19607843, 0.1882353 , 0.16862746],\n",
       "        ...,\n",
       "        [0.61960787, 0.5176471 , 0.42352942],\n",
       "        [0.59607846, 0.49019608, 0.4       ],\n",
       "        [0.5803922 , 0.4862745 , 0.40392157]],\n",
       "\n",
       "       [[0.0627451 , 0.07843138, 0.07843138],\n",
       "        [0.        , 0.        , 0.        ],\n",
       "        [0.07058824, 0.03137255, 0.        ],\n",
       "        ...,\n",
       "        [0.48235294, 0.34509805, 0.21568628],\n",
       "        [0.46666667, 0.3254902 , 0.19607843],\n",
       "        [0.47843137, 0.34117648, 0.22352941]],\n",
       "\n",
       "       [[0.09803922, 0.09411765, 0.08235294],\n",
       "        [0.0627451 , 0.02745098, 0.        ],\n",
       "        [0.19215687, 0.10588235, 0.03137255],\n",
       "        ...,\n",
       "        [0.4627451 , 0.32941177, 0.19607843],\n",
       "        [0.47058824, 0.32941177, 0.19607843],\n",
       "        [0.42745098, 0.28627452, 0.16470589]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[0.8156863 , 0.6666667 , 0.3764706 ],\n",
       "        [0.7882353 , 0.6       , 0.13333334],\n",
       "        [0.7764706 , 0.6313726 , 0.10196079],\n",
       "        ...,\n",
       "        [0.627451  , 0.52156866, 0.27450982],\n",
       "        [0.21960784, 0.12156863, 0.02745098],\n",
       "        [0.20784314, 0.13333334, 0.07843138]],\n",
       "\n",
       "       [[0.7058824 , 0.54509807, 0.3764706 ],\n",
       "        [0.6784314 , 0.48235294, 0.16470589],\n",
       "        [0.7294118 , 0.5647059 , 0.11764706],\n",
       "        ...,\n",
       "        [0.72156864, 0.5803922 , 0.36862746],\n",
       "        [0.38039216, 0.24313726, 0.13333334],\n",
       "        [0.3254902 , 0.20784314, 0.13333334]],\n",
       "\n",
       "       [[0.69411767, 0.5647059 , 0.45490196],\n",
       "        [0.65882355, 0.5058824 , 0.36862746],\n",
       "        [0.7019608 , 0.5568628 , 0.34117648],\n",
       "        ...,\n",
       "        [0.84705883, 0.72156864, 0.54901963],\n",
       "        [0.5921569 , 0.4627451 , 0.32941177],\n",
       "        [0.48235294, 0.36078432, 0.28235295]]], dtype=float32)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Building and Training our Convolutional Neural Network"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similar to our first notebook, we need to define the architecture (template) first before fitting the best numbers into this architecture by learning from the data. In summary, the architecture we will build in this post is this:\n",
    "\n",
    "- Conv Layer (Filter size 3x3, Depth 32)\n",
    "- Conv Layer (Filter size 3x3, Depth 32)\n",
    "- Max Pool Layer (Filter size 2x2)\n",
    "- Dropout Layer (Prob of dropout 0.25)\n",
    "- Conv Layer (Filter size 3x3, Depth 64)\n",
    "- Conv Layer (Filter size 3x3, Depth 64)\n",
    "- Max Pool Layer (Filter size 2x2)\n",
    "- Dropout Layer (Prob of dropout 0.25)\n",
    "- FC Layer (512 neurons)\n",
    "- Dropout Layer (Prob of dropout 0.5)\n",
    "- FC Layer, Softmax (10 neurons)\n",
    "\n",
    "For an intuition behind these layers, please refer to Intuitive Deep Learning [Part 2](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-2-cnns-for-computer-vision-24992d050a27).\n",
    "\n",
    "We will be using Keras to build our architecture. Let's import the code from Keras that we will need to use:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.models import Sequential\n",
    "from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We then call an empty Sequential model and 'add' to this model layer by layer:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = Sequential()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The first layer is a conv layer with filter size 3x3, stride size 1 (in both dimensions), and depth 32. The padding is the 'same' and the activation is 'relu' (these two settings will apply to all layers in our CNN). We add this layer to our empty sequential model using the function model.add().\n",
    "\n",
    "The first number 32 refers to the depth. The next pair of numbers (3,3) refer to the filter width and size. Then, we specify activation which is 'relu' and padding which is 'same'. Notice that we did not specify stride. This is because stride=1 is a default setting, and unless we want to change this setting, we need not specify it.\n",
    "\n",
    "If you recall, we also need to specify an input size for our first layer; subsequent layers does not have this specification since they can infer the input size from the output size of the previous layer.\n",
    "\n",
    "All that being said, our first layer in code looks like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32,32,3)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our second layer looks like this in code (we don't need to specify the input size):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The next layer is a max pooling layer with pool size 2 x 2 and stride 2 (in both dimensions). The default for a max pooling layer stride is the pool size, so we don't have to specify the stride:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(MaxPooling2D(pool_size=(2, 2)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lastly, we add a dropout layer with probability 0.25 of dropout so as to prevent overfitting:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Dropout(0.25))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And there we have it, our first four layers in code. The next four layers look really similar (except the depth of the conv layer is 64 instead of 32):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))\n",
    "model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))\n",
    "model.add(MaxPooling2D(pool_size=(2, 2)))\n",
    "model.add(Dropout(0.25))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lastly, we have to code in our fully connected layer, which is similar to what we've done in our previous post, [Build your first Neural Network](https://medium.com/intuitive-deep-learning/build-your-first-neural-network-to-predict-house-prices-with-keras-eb5db60232c). However, at this point, our neurons are spatially arranged in a cube-like format rather than in just one row. To make this cube-like format of neurons into one row, we have to first flatten it. We do so by adding a Flatten layer:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Flatten())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, we have a dense (FC) layer of 512 neurons with relu activation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Dense(512, activation='relu'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We add another dropout of probability 0.5:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Dropout(0.5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And lastly, we have a dense (FC) layer with 10 neurons and softmax activation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.add(Dense(10, activation='softmax'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And we're done with specifying our architecture! To see a summary of the full architecture, we run the code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       \n",
      "_________________________________________________________________\n",
      "conv2d_2 (Conv2D)            (None, 32, 32, 32)        9248      \n",
      "_________________________________________________________________\n",
      "max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         \n",
      "_________________________________________________________________\n",
      "dropout_1 (Dropout)          (None, 16, 16, 32)        0         \n",
      "_________________________________________________________________\n",
      "conv2d_3 (Conv2D)            (None, 16, 16, 64)        18496     \n",
      "_________________________________________________________________\n",
      "conv2d_4 (Conv2D)            (None, 16, 16, 64)        36928     \n",
      "_________________________________________________________________\n",
      "max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         \n",
      "_________________________________________________________________\n",
      "dropout_2 (Dropout)          (None, 8, 8, 64)          0         \n",
      "_________________________________________________________________\n",
      "flatten_1 (Flatten)          (None, 4096)              0         \n",
      "_________________________________________________________________\n",
      "dense_1 (Dense)              (None, 512)               2097664   \n",
      "_________________________________________________________________\n",
      "dropout_3 (Dropout)          (None, 512)               0         \n",
      "_________________________________________________________________\n",
      "dense_2 (Dense)              (None, 10)                5130      \n",
      "=================================================================\n",
      "Total params: 2,168,362\n",
      "Trainable params: 2,168,362\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model.summary()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We now fill in the best numbers after we've specified our architecture. We'll compile the model with our settings below.\n",
    "\n",
    "The loss function we use is called categorical cross entropy, which is applicable for a classification problem of many classes. The optimizer we use here is Adam. We haven't gone through the intuition of Adam yet, but know that Adam is simply a type of stochastic gradient descent (with a few modifications) so that it trains better. Lastly, we want to track the accuracy of our model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.compile(loss='categorical_crossentropy',\n",
    "              optimizer='adam',\n",
    "              metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And now, it's time to run our training.\n",
    "\n",
    "We train our model with batch size 32 and 20 epochs. We use the setting validation_split=0.2 instead of validation_data. With this shortcut, we did not need to split our dataset into a train and validation set at the start! Instead, we simply specify how much of our dataset will be used as a validation set. In this case, 20% of our dataset is used as a validation set. This will take a while on a CPU, so you might want to start training and get some coffee before coming back."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train on 40000 samples, validate on 10000 samples\n",
      "Epoch 1/20\n",
      "40000/40000 [==============================] - 256s 6ms/step - loss: 1.5844 - acc: 0.4176 - val_loss: 1.1586 - val_acc: 0.5848\n",
      "Epoch 2/20\n",
      "40000/40000 [==============================] - 263s 7ms/step - loss: 1.1519 - acc: 0.5897 - val_loss: 0.9885 - val_acc: 0.6494\n",
      "Epoch 3/20\n",
      "40000/40000 [==============================] - 259s 6ms/step - loss: 0.9921 - acc: 0.6502 - val_loss: 0.8804 - val_acc: 0.6901\n",
      "Epoch 4/20\n",
      "40000/40000 [==============================] - 250s 6ms/step - loss: 0.8872 - acc: 0.6847 - val_loss: 0.8371 - val_acc: 0.6995\n",
      "Epoch 5/20\n",
      "40000/40000 [==============================] - 251s 6ms/step - loss: 0.8172 - acc: 0.7109 - val_loss: 0.7716 - val_acc: 0.7261\n",
      "Epoch 6/20\n",
      "40000/40000 [==============================] - 251s 6ms/step - loss: 0.7544 - acc: 0.7335 - val_loss: 0.7429 - val_acc: 0.7422\n",
      "Epoch 7/20\n",
      "40000/40000 [==============================] - 251s 6ms/step - loss: 0.7086 - acc: 0.7504 - val_loss: 0.7441 - val_acc: 0.7477\n",
      "Epoch 8/20\n",
      "40000/40000 [==============================] - 251s 6ms/step - loss: 0.6676 - acc: 0.7639 - val_loss: 0.7214 - val_acc: 0.7492\n",
      "Epoch 9/20\n",
      "40000/40000 [==============================] - 250s 6ms/step - loss: 0.6327 - acc: 0.7776 - val_loss: 0.7185 - val_acc: 0.7555\n",
      "Epoch 10/20\n",
      "40000/40000 [==============================] - 248s 6ms/step - loss: 0.6016 - acc: 0.7888 - val_loss: 0.6891 - val_acc: 0.7656\n",
      "Epoch 11/20\n",
      "40000/40000 [==============================] - 249s 6ms/step - loss: 0.5660 - acc: 0.7996 - val_loss: 0.6867 - val_acc: 0.7626\n",
      "Epoch 12/20\n",
      "40000/40000 [==============================] - 248s 6ms/step - loss: 0.5476 - acc: 0.8064 - val_loss: 0.6849 - val_acc: 0.7698\n",
      "Epoch 13/20\n",
      "40000/40000 [==============================] - 248s 6ms/step - loss: 0.5316 - acc: 0.8115 - val_loss: 0.6887 - val_acc: 0.7678\n",
      "Epoch 14/20\n",
      "40000/40000 [==============================] - 248s 6ms/step - loss: 0.5002 - acc: 0.8246 - val_loss: 0.6931 - val_acc: 0.7731\n",
      "Epoch 15/20\n",
      "40000/40000 [==============================] - 245s 6ms/step - loss: 0.4917 - acc: 0.8246 - val_loss: 0.7365 - val_acc: 0.7660\n",
      "Epoch 16/20\n",
      "40000/40000 [==============================] - 248s 6ms/step - loss: 0.4690 - acc: 0.8374 - val_loss: 0.7153 - val_acc: 0.7693\n",
      "Epoch 17/20\n",
      "40000/40000 [==============================] - 245s 6ms/step - loss: 0.4592 - acc: 0.8377 - val_loss: 0.6857 - val_acc: 0.7755\n",
      "Epoch 18/20\n",
      "40000/40000 [==============================] - 248s 6ms/step - loss: 0.4519 - acc: 0.8416 - val_loss: 0.6918 - val_acc: 0.7741\n",
      "Epoch 19/20\n",
      "40000/40000 [==============================] - 246s 6ms/step - loss: 0.4330 - acc: 0.8461 - val_loss: 0.6926 - val_acc: 0.7739\n",
      "Epoch 20/20\n",
      "40000/40000 [==============================] - 246s 6ms/step - loss: 0.4242 - acc: 0.8493 - val_loss: 0.7026 - val_acc: 0.7785\n"
     ]
    }
   ],
   "source": [
    "hist = model.fit(x_train, y_train_one_hot, \n",
    "           batch_size=32, epochs=20, \n",
    "           validation_split=0.2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After you've done training, we can visualize the model training and validation loss as well as training / validation accuracy over the number of epochs using the below code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(hist.history['loss'])\n",
    "plt.plot(hist.history['val_loss'])\n",
    "plt.title('Model loss')\n",
    "plt.ylabel('Loss')\n",
    "plt.xlabel('Epoch')\n",
    "plt.legend(['Train', 'Val'], loc='upper right')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(hist.history['acc'])\n",
    "plt.plot(hist.history['val_acc'])\n",
    "plt.title('Model accuracy')\n",
    "plt.ylabel('Accuracy')\n",
    "plt.xlabel('Epoch')\n",
    "plt.legend(['Train', 'Val'], loc='lower right')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Once we are done with tweaking our hyperparameters, we can run it on our test dataset below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10000/10000 [==============================] - 14s 1ms/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0.7709"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.evaluate(x_test, y_test_one_hot)[1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "At this point, you might want to save your trained model (since you've spent so long waiting for it to train). The model will be saved in a file format called HDF5 (with the extension .h5). We save our model with this line of code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.save('my_cifar10_model.h5')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Testing out with your own images"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we have a model, let's try it on our own images. To do so, place your image in the same directory as your notebook. For the purposes of this post, I'm going to use an image of a cat (which you can download here(link)). Now, we read in our JPEG file as an array of pixel values:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_image = plt.imread(\"cat.jpg\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The first thing we have to do is to resize the image of our cat so that we can fit it into our model (input size of 32 * 32 * 3)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "D:\\Anaconda3\\envs\\intuitive-deep-learning\\lib\\site-packages\\skimage\\transform\\_warps.py:105: UserWarning: The default mode, 'constant', will be changed to 'reflect' in skimage 0.15.\n",
      "  warn(\"The default mode, 'constant', will be changed to 'reflect' in \"\n",
      "D:\\Anaconda3\\envs\\intuitive-deep-learning\\lib\\site-packages\\skimage\\transform\\_warps.py:110: UserWarning: Anti-aliasing will be enabled by default in skimage 0.15 to avoid aliasing artifacts when down-sampling images.\n",
      "  warn(\"Anti-aliasing will be enabled by default in skimage 0.15 to \"\n"
     ]
    }
   ],
   "source": [
    "from skimage.transform import resize\n",
    "my_image_resized = resize(my_image, (32,32,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "img = plt.imshow(my_image_resized)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And now, we see what our trained model will output when given an image of our cat, using this code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "probabilities = model.predict(np.array( [my_image_resized,] ))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.00581452, 0.00405185, 0.02275212, 0.31140402, 0.01715197,\n",
       "        0.1401798 , 0.07874653, 0.296455  , 0.00255446, 0.12088975]],\n",
       "      dtype=float32)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "probabilities"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Most likely class: cat -- Probability: 0.31140402\n",
      "Second most likely class: horse -- Probability: 0.296455\n",
      "Third most likely class: dog -- Probability: 0.1401798\n",
      "Fourth most likely class: truck -- Probability: 0.12088975\n",
      "Fifth most likely class: frog -- Probability: 0.078746535\n"
     ]
    }
   ],
   "source": [
    "number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']\n",
    "index = np.argsort(probabilities[0,:])\n",
    "print(\"Most likely class:\", number_to_class[index[9]], \"-- Probability:\", probabilities[0,index[9]])\n",
    "print(\"Second most likely class:\", number_to_class[index[8]], \"-- Probability:\", probabilities[0,index[8]])\n",
    "print(\"Third most likely class:\", number_to_class[index[7]], \"-- Probability:\", probabilities[0,index[7]])\n",
    "print(\"Fourth most likely class:\", number_to_class[index[6]], \"-- Probability:\", probabilities[0,index[6]])\n",
    "print(\"Fifth most likely class:\", number_to_class[index[5]], \"-- Probability:\", probabilities[0,index[5]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, the model has accurately predicted that this is indeed an image of a cat. Now, this isn't the best model we have and accuracy has been quite low, so don't expect too much out of it. This post has covered the very fundamentals of CNNs on a very simple dataset; we'll cover how to build state-of-the-art models in future posts. Nevertheless, you should be able to get some pretty cool results from your own images (some images that you can try this out on are in the GitHub folder)."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
