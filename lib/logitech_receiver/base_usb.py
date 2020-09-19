# -*- python-mode -*-
# -*- coding: UTF-8 -*-
# Copyright (C) 2012-2013  Daniel Pavel
##
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
##
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
##
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# USB ids of Logitech wireless receivers.
# Only receivers supporting the HID++ protocol can go in here.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

_DRIVER = ("hid-generic", "generic-usb", "logitech-djreceiver")

# max_devices is only used for receivers that do not support reading from _R.receiver_info offset 0x03, default to 1
# may_unpair is only used for receivers that do not support reading from _R.receiver_info offset 0x03, default to False
# should this last be changed so that may_unpair is used for all receivers? writing to _R.receiver_pairing doesn't seem right
# re_pairs determines whether a receiver pairs by replacing existing pairings, default to False
# currently only one receiver is so marked - should there be more?


def _unifying_receiver(product_id):
    return {
        "vendor_id": 0x046D,
        "product_id": product_id,
        "usb_interface": 2,
        "hid_driver": _DRIVER,
        "name": "Unifying Receiver",
    }


def _nano_receiver(product_id):
    return {
        "vendor_id": 0x046D,
        "product_id": product_id,
        "usb_interface": 1,
        "hid_driver": _DRIVER,
        "name": "Nano Receiver",
        "may_unpair": False,
        "re_pairs": True,
    }


def _nano_receiver_max2(product_id):
    return {
        "vendor_id": 0x046D,
        "product_id": product_id,
        "usb_interface": 1,
        "hid_driver": _DRIVER,
        "name": "Nano Receiver",
        "max_devices": 2,
        "may_unpair": False,
        "re_pairs": True,
    }


def _lenovo_receiver(product_id):
    return {
        "vendor_id": 0x17EF,
        "product_id": product_id,
        "usb_interface": 1,
        "hid_driver": _DRIVER,
        "name": "Nano Receiver",
    }


def _lightspeed_receiver(product_id):
    return {
        "vendor_id": 0x046D,
        "product_id": product_id,
        "usb_interface": 2,
        "hid_driver": _DRIVER,
        "name": "Lightspeed Receiver",
    }


# standard Unifying receivers (marked with the orange Unifying logo)
UNIFYING_RECEIVER_C52B = _unifying_receiver(0xC52B)
UNIFYING_RECEIVER_C532 = _unifying_receiver(0xC532)

# Nano receviers that support the Unifying protocol
NANO_RECEIVER_ADVANCED = _nano_receiver(0xC52F)

# Nano receivers that don't support the Unifying protocol
NANO_RECEIVER_C517 = _nano_receiver(0xC517)
NANO_RECEIVER_C518 = _nano_receiver(0xC518)
NANO_RECEIVER_C51A = _nano_receiver(0xC51A)
NANO_RECEIVER_C51B = _nano_receiver(0xC51B)
NANO_RECEIVER_C521 = _nano_receiver(0xC521)
NANO_RECEIVER_C525 = _nano_receiver(0xC525)
NANO_RECEIVER_C526 = _nano_receiver(0xC526)
NANO_RECEIVER_C52e = _nano_receiver(0xC52E)
NANO_RECEIVER_C531 = _nano_receiver(0xC531)
NANO_RECEIVER_C534 = _nano_receiver_max2(0xC534)
NANO_RECEIVER_6042 = _lenovo_receiver(0x6042)

# Lightspeed receivers
LIGHTSPEED_RECEIVER_C539 = _lightspeed_receiver(0xC539)
LIGHTSPEED_RECEIVER_C53a = _lightspeed_receiver(0xC53A)
LIGHTSPEED_RECEIVER_C53f = _lightspeed_receiver(0xC53F)

del _DRIVER, _unifying_receiver, _nano_receiver, _lenovo_receiver, _lightspeed_receiver

ALL = (
    UNIFYING_RECEIVER_C52B,
    UNIFYING_RECEIVER_C532,
    NANO_RECEIVER_ADVANCED,
    NANO_RECEIVER_C517,
    NANO_RECEIVER_C518,
    NANO_RECEIVER_C51A,
    NANO_RECEIVER_C51B,
    NANO_RECEIVER_C521,
    NANO_RECEIVER_C525,
    NANO_RECEIVER_C526,
    NANO_RECEIVER_C52e,
    NANO_RECEIVER_C531,
    NANO_RECEIVER_C534,
    NANO_RECEIVER_6042,
    LIGHTSPEED_RECEIVER_C539,
    LIGHTSPEED_RECEIVER_C53a,
    LIGHTSPEED_RECEIVER_C53f,
)


def product_information(usb_id):
    if isinstance(usb_id, str):
        usb_id = int(usb_id, 16)
    for r in ALL:
        if usb_id == r.get("product_id"):
            return r
    return {}
