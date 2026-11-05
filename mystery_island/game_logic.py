ROUTES = {
    "Beach": "Jungle",
    "Jungle": "Cave",
    "Cave": "Old Bridge",
    "Old Bridge": "Lighthouse"
}


def get_next_location(location):
    return ROUTES.get(location)


def can_enter_location(destination, inventory):

    if destination == "Old Bridge":
        return "Rope" in inventory

    elif destination == "Lighthouse":
        return "Lantern" in inventory

    return True