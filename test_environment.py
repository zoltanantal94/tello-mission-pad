import fly7


class TestEnvironment:
    def __init__(self):
        self.local = [0]

    def transform_coordinate(self, global_coordinate, pad_id):
        self.local = fly7.glob2loc_coord(global_coordinate, pad_id)
