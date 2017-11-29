# GcSizeIndicator struct

from .Struct import Struct

STRUCTNAME = 'GcSizeIndicator'

class GcSizeIndicator(Struct):
    def __init__(self, **kwargs):
        super(GcSizeIndicator, self).__init__()

        """ Contents of the struct """
        self.data['SizeIndicator'] = kwargs.get('SizeIndicator', "Small")
        """ End of the struct contents"""

        # Parent needed so that it can be a SubElement of something
        self.parent = None
        self.STRUCTNAME = STRUCTNAME
