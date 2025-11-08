# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = min(item.quality + 2, 50)
                else:
                    item.quality = min(item.quality + 1, 50)

            elif item.name.startswith("Backstage pass"):
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 5:
                    item.quality = min(item.quality + 3, 50)
                elif item.sell_in < 10:
                    item.quality = min(item.quality + 2, 50)
                else:
                    item.quality = min(item.quality + 1, 50)

            elif item.name.startswith("Conjured"):
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = max(item.quality - 4, 0)
                else:
                    item.quality = max(item.quality - 2, 0)

            elif not item.name.startswith("Sulfuras"):  # normal item
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = max(item.quality - 2, 0)
                else:
                    item.quality = max(item.quality - 1, 0)




class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
