{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1973ad5d-1312-4e2a-aadb-b9bfd8fdb246",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "def sigmoid(z):\n",
    "    return 1. / (1. + np.exp(-z))\n",
    "\n",
    "\n",
    "def int_to_onehot(y, num_labels):\n",
    "    ary = np.zeros((y.shape[0], num_labels))\n",
    "    for i, val in enumerate(y):\n",
    "        ary[i, val] = 1\n",
    "        \n",
    "    return ary\n",
    "\n",
    "\n",
    "class NeuralNetMLP:\n",
    "    \n",
    "    def __init__(self, num_features, num_hidden,\n",
    "                 num_classes, random_seed=123):\n",
    "        super().__init__()\n",
    "        \n",
    "        self.num_classes = num_classes\n",
    "        \n",
    "        # hidden\n",
    "        rng = np.random.RandomState(random_seed)\n",
    "        \n",
    "        self.weight_h = rng.normal(\n",
    "            loc=0.0, scale=0.1, size=(num_hidden, num_features))\n",
    "        self_bias_h = np.zeros(num_hidden)\n",
    "        \n",
    "        # output\n",
    "        self.weight_out = rng.normal(\n",
    "            loc=0.0, scale=0.1, size=(num_classes, num_hidden))\n",
    "        self.bias_out = np.zeros(num_classes)\n",
    "        \n",
    "        def forward(self, x):\n",
    "            # hidden"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c32eb50-0d9a-4cda-89cb-295b62a5a77e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d262bec4-f44d-490f-bc8d-981062a21957",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d509210d-7655-4fe3-a6f7-def1dbd0ec27",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b32f9ed6-da83-42b2-9bb1-4bf83efdf5e6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bcb99eae-4fe9-4315-a1b7-91861dd1a62a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "241cf705-5c71-4bc3-9801-66899288d6d7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38546605-9d6a-4dcc-aad0-af927b9147fb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06ea020a-63b7-4968-8ab5-b843525275ac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86303a27-195e-4e69-a56c-502dd0906eee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29702951-14d8-41e6-ae8e-0849343dbde6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45af7033-cf04-4d50-8b00-c2b1039178f0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9aea11e7-785a-4d26-a198-e8bb9441f2f5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c55691e5-0b7f-4a89-90ad-c3a096eb7ba2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96c4978c-1df4-43b3-a5d6-2cd01651dea4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5f80ec8-94b0-4834-b892-494e94910639",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
