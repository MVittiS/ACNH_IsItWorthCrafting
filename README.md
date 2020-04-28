# The AC:NL "Is it worth crafting it" script

This is a simple Python 3.x script that uses `villagerDB` to generate a CSV table containing the calculated BOM (bill of material) prices for all items in the game Animal Crossing: New Horizons, and comparing them against their purchase and sales prices. That's it! It's under a Chocolateware license, so feel free to do whatever you want with it.

This is not an exhaustive list, and some items (notable the ones that require the `Bells` item for crafting) are not present, since `villagerDB` doesn't have separate entries for the different amounts of Bells sachels that you find during the game. If they someday have different entires for different Bells amounts, this would solve the issue and make this script work. In that case, please contribute to `villagerDB`; the more complete their database is, the more complete this script is as well.

### How to Use

After making sure you have Python 3 in your system, go to a command prompt / terminal.

You just need to first clone this repository:
```
git clone https://github.com/MVittiS/ACNH_IsItWorthCrafting
```

Then, clone `villagerDB` inside of it:
```
git submodule update
```

And finally, run it.
```
python3 main.py
```

The output will be a `NewHorizons_ItemBOM.csv` file in the same directory you ran the script from.


### Trivia

As of 28/4/2020:
- If compared against the sales price...
  - The most profitable items (in percentage) are
    - Flimsy net (BOM: 25 Bells, Sells for 100 Bells = 300% profit)
    - Flimsy Fishing Rod (BOM: 25 Bells, Sells for 100 Bells = 300% profit)
  - The most profitable item (in Bells) is
    - Robot Hero (BOM: 233'750 Bells, Sells for 250'000 Bells = 16'250 Bells of profit)
  - The least profitable items (in percentage) are
    - All the fences (selling for only 1/5th of their BOM cost, netting an 80% loss)
  - The least profitable item (in Bells) is
    - Iron Fence (BOM: 2'250 Bells, Sells for 450 Bells = 1'800 Bells of losses)
- If compared against the purchase price...
  - The most profitable item (in Bells) is
    - Golden Toilet (BOM: 60'000 Bells, Bought for 240'000 Bells = 180'000 Bells of savings)
  - The least profitable item (in Bells) is
    - Flimsy Fishing Rod (BOM: 25 Bells, Bought for 100 Bells = 75 Bells of savings)

  