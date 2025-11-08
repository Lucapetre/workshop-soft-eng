# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_bar(self):
        items = [Item("bar", 20, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("bar", items[0].name)
        self.assertEqual(9, items[0].quality)
        self.assertEqual(19, items[0].sell_in)

    def test_sulfuras_name(self):
        items = [Item("Sulfuras", 40, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 0, 0), Item("Aged Brie", 20, 46)]
        gilded_rose = GildedRose(items)
        for i in range(5):
            gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(10, items[0].quality)
        self.assertEqual("Aged Brie", items[1].name)
        self.assertEqual(50, items[1].quality)

    def test_backstage_pass_name(self):
        items = [Item("Backstage pass", 3, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 5),
                 Item("Backstage passes to a TAFKAL80ETC concert", 7, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        self.assertEqual(8, items[1].quality)
        for i in range(5):
            gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        self.assertEqual(22, items[1].quality)
        for i in range(5):
            gilded_rose.update_quality()
        self.assertEqual(0, items[1].quality)

    def test_double_decay(self):
        items = [Item("bar", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_conjured_items(self):
        items = [Item("Conjured Mana Cake", 2, 20),
                 Item("Conjured Lava Cake", 4, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(8, items[1].quality)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        self.assertEqual(4, items[1].quality)

    def test_print_item(self):
        item = Item("+5 Dexterity Vest", 5, 15)
        self.assertEqual(item.__repr__(), "+5 Dexterity Vest, 5, 15")

        
if __name__ == '__main__':
    unittest.main()
