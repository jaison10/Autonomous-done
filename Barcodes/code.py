from sys import argv
import zbar
proc = zbar.Processor()
proc.parse_config('enable')

# set the correct device number for your system
device = '/dev/video13'
if len(argv) > 1:
    device = argv[1]
proc.init(device)
proc.process_one()
for symbol in proc.results:
    print 'barcode type=', symbol.type, ' data=', '"%s"' % symbol.data
