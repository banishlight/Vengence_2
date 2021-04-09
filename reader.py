import engine
import pygame


class Map:

    def read(self, mapname):
        # read map.properties
        properties = open('maps/' + mapname + '/map.properties', 'r')
        properties.readline()
        width = int(properties.readline().replace("width=", "").replace("\n", ""))
        height = int(properties.readline().replace("height=", "").replace("\n", ""))
        tile_count = int(properties.readline().replace("tile_count=", "").replace("\n", ""))

        # read tile images
        tile_list = [0] * tile_count
        for a in range(tile_count):
            tile_list[a] = pygame.image.load('maps/' + mapname + '/tiles/' + "tile_" + str(a) + ".png")

        # create maplist
        map_list = [[0 for x in range(height)] for y in range(width)]
        file_background = open('maps/' + mapname + '/background.txt', 'r')
        file_foreground = open('maps/' + mapname + '/foreground.txt', 'r')
        file_props = open('maps/' + mapname + '/props.txt', 'r')
        file_collision = open('maps/' + mapname + '/collision.txt', 'r')

        # read each file into tile object, save into 2D array
        for y in range(height):
            for x in range(width):
                # read background
                read_background = tile_list[int(file_background.readline(2))]
                b = (True, read_background)

                # read foreground
                val = int(file_foreground.readline(2))
                if val == 0:
                    f = (False, None)
                else:
                    read_foreground = tile_list[val]
                    f = (True, read_foreground)

                # read props
                val = int(file_props.readline(2))
                if val == 0:
                    p = (False, None)
                else:
                    read_props = tile_list[val]
                    p = (True, read_props)

                # read collision
                val = int(file_collision.readline(1))
                if val == 0:
                    c = (False, None)
                else:
                    read_collision = int(file_collision.readline(2))
                    c = (True, read_collision)

                # create tike object, save to map_list
                tile = engine.Tile(b, f, p, c)
                map_list[x][y] = tile

            # read out new line character
            file_background.readline()
            file_foreground.readline()
            file_props.readline()
            file_collision.readline()
        return map_list, tile_list


if __name__ == '__main__':
    test = Map()
    test.read('test_map')
