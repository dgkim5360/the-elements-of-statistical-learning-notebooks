================================================================
Jupyter Notebooks for the Elements of Statistical Learning (WIP)
================================================================

It aims to summarize and reproduce the textbook "The Elements of Statistical Learning" 2/E by Hastie, Tibshirani, and Friedman.

Currently working the early chapters, I try to implement without frameworks like scikit-learn for showing the algorithms that the textbook introduces to me.

Also starting with the neural networks, I decided to use PyTorch_ which seems less magical (They say that ``torch.Tensor`` is ``numpy.ndarray`` with GPU support).

.. _PyTorch: //pytorch.org


Installation
------------

Use your favorite virtualenv system and install the below dependencies; quite standard ones.

* numpy
* scipy
* matplotlib
* pandas
* jupyter
* pytorch
* scikit-learn (optional, used in my own articles)

.. code-block:: bash

   (esl) $ pip install ipython numpy scipy matplotlib pandas jupyter

   # The command below installs pytorch for Python 3.6 without CUDA support.
   # For other settings, consult with pytorch.org.
   (esl) $ pip install http://download.pytorch.org/whl/cpu/torch-0.3.1-cp36-cp36m-linux_x86_64.whl


Execution
---------

Just run ``jupyter notebook``.
