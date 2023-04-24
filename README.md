# Diamond Price Prediction
### About the Data :
The dataset The goal is to predict price of given diamond (Regression Analysis).

There are 10 independent variables (including id):

- `id` : unique identifier of each diamond
- `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
- `cut` : Quality of Diamond Cut
- `color` : Color of Diamond
- `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
- `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
- `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
- `x` : Diamond X dimension
- `y` : Diamond Y dimension
- `z` : Diamond Z dimension

Target variable:
- `price`: Price of the given Diamond.

Dataset Source Link : https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv

### Using poetry for virtual environments

```sh
cd pre-existing-project
poetry init
poetry add pendulum
```

The easiest way to activate the virtual environment is to create a nested shell with `poetry shell`.

To deactivate the virtual environment and exit this new shell type `exit`. 

To deactivate the virtual environment without leaving the shell use `deactivate`.

To install the defined dependencies for your project, just run the install command `poetry install`