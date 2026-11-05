import unittest

from game_logic import get_next_location, can_enter_location


class TestMysteryIsland(unittest.TestCase):

    def test_beach_route(self):
        result = get_next_location("Beach")
        self.assertEqual(result, "Jungle")

    def test_jungle_route(self):
        result = get_next_location("Jungle")
        self.assertEqual(result, "Cave")

    def test_cave_route(self):
        result = get_next_location("Cave")
        self.assertEqual(result, "Old Bridge")

    def test_invalid_location(self):
        result = get_next_location("Desert")
        self.assertIsNone(result)

    def test_bridge_requires_rope(self):
        result = can_enter_location("Old Bridge", [])
        self.assertFalse(result)

    def test_bridge_with_rope(self):
        result = can_enter_location("Old Bridge", ["Rope"])
        self.assertTrue(result)

    def test_lighthouse_requires_lantern(self):
        result = can_enter_location("Lighthouse", [])
        self.assertFalse(result)

    def test_lighthouse_with_lantern(self):
        result = can_enter_location("Lighthouse", ["Lantern"])
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()