# Animal Crossing: New Horizons "Is It Worth Crafting" Python script
# By MVittiS, April 2020
#
# "
#    But we don't do things because they're easy, hm?
#    We do them because they are profitable!
# " - Tom Nook, 2020

import csv
import json
import os
import sys

if __name__ == "__main__":

    villager_DB_path = str()

    if len(sys.argv) < 2:
        print('Assuming villagerdb is in the same directory as python script.')
        villager_DB_path = str('villagerdb/data/items/')
    else:
        villager_DB_path = os.path.join(sys.argv[1], 'data/items/')

    item_files = \
        [os.path.join(villager_DB_path, f) for f in os.listdir(villager_DB_path)
        if os.path.isfile(os.path.join(villager_DB_path, f))]

    all_items = [json.load(open(item)) for item in item_files]

    new_horizon_items = [item for item in all_items
                         if 'nh' in item['games']]
    
    craftable_items = [item for item in new_horizon_items
                       if 'recipe' in item['games']['nh']]

    sellable_items = [item for item in craftable_items
                      if 'sellPrice' in item['games']['nh']]

    valid_items = []

    table_file = open('NewHorizons_ItemBOM.csv', 'w')
    table = csv.writer(table_file)
    table.writerow(['Item Name', 'BOM Cost', 'Sells for', 'Profit (Bells)',
                    'Profit (%)', 'Bought for (Bells)', 'Vs. Store Savings (Bells)'])


    for item in sellable_items:
        item_BOM = item['games']['nh']['recipe']
        item_BOM_cost = 0
        for key, amount in item_BOM.items():
            ingredient_list = [item for item in new_horizon_items
                               if item['id'] == key]
            if len(ingredient_list) is 0:
                continue

            ingredient = ingredient_list[0] 
            if 'sellPrice' not in ingredient['games']['nh']:
                # A handful of ingredients don't have prices
                #  in villagerdb, such as Fossils and Bells
                continue

            item_BOM_cost += amount * ingredient['games']['nh']['sellPrice']['value']

        if item_BOM_cost is 0:
            continue

        # Uncomment for text output
        #print(f"{item['name']} costs {item_BOM_cost} to make, "
        #      f"and sells for {item['games']['nh']['sellPrice']['value']}")

        item_sell_price = item['games']['nh']['sellPrice']['value']
        item_buy_price = 0
        try:
            item_buy_price = \
                item['games']['nh']['buyPrices'][0]['value'] \
                if item['games']['nh']['buyPrices'][0]['currency'] == 'bells' \
                else 0
        except:
            pass
        
        table.writerow(
            [item['name'], item_BOM_cost, item_sell_price,
            item_sell_price - item_BOM_cost,
            f'{100 * (item_sell_price/item_BOM_cost - 1):5.2f}',
            item_buy_price if item_buy_price > 0 else ' ',
            (item_buy_price - item_sell_price) if item_buy_price > 0 else ' '])
