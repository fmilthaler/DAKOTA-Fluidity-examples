# you need to add <fluidity-src-directory>/python to your PYTHONPATH
from fluidity_tools import stat_parser

det = stat_parser('tsunami.detectors')
fs = det['Water']['FreeSurface']['DetectorA']

print fs[-1]
print fs.max()
