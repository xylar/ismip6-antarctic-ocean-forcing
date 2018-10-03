import os

from ismip6_ocean_forcing.imbie import geojson, images, extend
from ismip6_ocean_forcing.remap.res import get_horiz_res


def make_imbie_masks(config):
    '''
    Download geojson files defining IMBIE basins and create masks that extend
    these basins into the open ocean
    '''
    res = get_horiz_res(config)

    try:
        os.makedirs('imbie')
    except OSError:
        pass

    if os.path.exists('imbie/basinNumbers_{}.nc'.format(res)):
        # we're already done
        return

    print('Building IMBIE basin masks...')

    basins = [[1, 2, 3], 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15, 16,
              [17, 18, 19], 20, 21, 22, 23, 24, 25, 26, 27]

    bedFileName = 'bedmap2/bedmap2_{}.nc'.format(res)

    geojson.download_imbie()

    geojson.combine_imbie(basins)

    images.write_basin_images(res, bedFileName)

    extend.extend_imbie_masks(res, basins, bedFileName)
    print('  Done.')