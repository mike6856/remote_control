import shlex

from flask import Blueprint, request, Response, \
                  jsonify, g, session

from subprocess32 import call
from .scriptz import *

mod_ir = Blueprint('ir', __name__, url_prefix='/ir')

def run_command(device, command):
    arg_str = 'irsend SEND_ONCE %s %s' % (device, command)
    args = shlex.split(arg_str)
    call(args)


@mod_ir.route('/send', methods=['POST'])
def send_command():
    params = request.args
    device = str(params.get('device'))
    command = str(params.get('command'))
    run_command(device, command)
    return "okay"

@mod_ir.route('/tv', methods=['POST'])
def select_tv():
    tv_mode()
    return "okay"
