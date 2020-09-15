{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import argparse\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#attributes \n",
    "minRating = \"minRatig\"\n",
    "maxRating = \"maxRatig\"\n",
    "\n",
    "def avgRatings(minRating=0, maxRating=5):\n",
    "    def wrapper(avgRating):\n",
    "        rating = 4\n",
    "        try:\n",
    "            rating = int(ratingStr)\n",
    "        except Exception:\n",
    "            raise argparse.ArgumentTypeError(f\"{avgRating} no es un valor positivo\")\n",
    "        \n",
    "        if rating >= minRating and rating <= maxRating:\n",
    "            return rating\n",
    "        else:\n",
    "            raise argparse.ArgumentTypeError(f\"El rating ha de estar entre {minYear} y {maxYear}\")\n",
    "    return wrapper"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "b'Skipping line 3350: expected 12 fields, saw 13\\nSkipping line 4704: expected 12 fields, saw 13\\nSkipping line 5879: expected 12 fields, saw 13\\nSkipping line 8981: expected 12 fields, saw 13\\n'\n",
      "usage: ipykernel_launcher.py [-h] [-r RATING]\n",
      "ipykernel_launcher.py: error: unrecognized arguments: -f /home/paula/.local/share/jupyter/runtime/kernel-9dea4b9c-8521-4767-8dd8-9a0a0174218b.json\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/paula/.local/lib/python3.8/site-packages/IPython/core/interactiveshell.py:3425: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    #print(args)\n",
    "    data = pd.read_csv('books.csv', error_bad_lines=False)[[\"authors\",\"title\",\"average_rating\"]]\n",
    "    minrating = data[\"average_rating\"].min()\n",
    "    maxrating = data[\"average_rating\"].max()\n",
    "\n",
    "    parser = argparse.ArgumentParser(description='Busca 10 libros con el rating proporcionado')\n",
    "    parser.add_argument('-r', dest='rating',\n",
    "                        default=4,\n",
    "                        type=avgRatings(minRating, maxRating),\n",
    "                        help=\"Rating seleccionada\")\n",
    "                        \n",
    "    args = parser.parse_args()\n",
    "\n",
    "    print(data[data.average_rating==args.rating].head())\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
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
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
