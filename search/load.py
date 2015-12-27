import os
from django.contrib.gis.utils import LayerMapping
from search.models import parcel

# Auto-generated `LayerMapping` dictionary for administration model
parcel_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}


parcel_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/LandParcels.shp'))

def run(verbose=True):
    lm = LayerMapping(parcel, parcel_shp, parcel_mapping,transform=True, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)