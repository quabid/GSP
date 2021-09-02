from hashlib import algorithms_available, algorithms_guaranteed


class AvailabilityFinder:
    def __init__(this):
        this.available = []
        this.guaranteed = []
        this.__init_members()

    def __init_members(this):
        for a in algorithms_available:
            this.available.append(a)

        for g in algorithms_guaranteed:
            this.guaranteed.append(g)

    def display_available(this):
        this.available.sort()
        for i, a in enumerate(this.available, start=1):
            print("{}.\t{}".format(i, a))

    def display_guaranteed(this):
        this.guaranteed.sort()
        for i, g in enumerate(this.guaranteed, start=1):
            print("{}.\t{}".format(i, g))

    def get_available(this):
        return this.available

    def get_guaranteed(this):
        return this.guaranteed

    def is_available(this, scheme):
        return scheme in algorithms_available

    def is_guaranteed(this, available):
        return available in algorithms_guaranteed