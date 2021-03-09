
# Robo Advisor (Python)

## Prerequisites

  + Anaconda 3.7
  + Python 3.8
  + Pip

## Installation

Clone this repository and make sure that you set this repository as the working directory for your command line

```sh
cd shopping-cart
```

Create and activate a new virtual environment in your command line using this code.

```sh
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
```

In your command line, install package requirements using this code.

```sh
pip install -r requirements.txt
```

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired API Key. (replace abc123 with your key)

```sh
touch .env
echo ALPHA_VANTAGE_API_KEY="abc123" >> .env
```

## Usage

Run this command.

```py
python app/robo_advisor.py
```