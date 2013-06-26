SCRIPT=$(readlink -f $0)
src_relative=$(dirname $SCRIPT)'/..'
src_absolute=$(cd $src_relative; pwd)
dhcp_absolute=$src_absolute/daemons/dhcp_manager
PYTHONPATH=$src_absolute:$dhcp_absolute
export PYTHONPATH
python web.py
