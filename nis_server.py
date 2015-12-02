#!/usr/bin/env python

from __future__ import absolute_import

# from pkg_resources import resource_filename
import tornado.ioloop
import tornado.web
from nis_api.config import config
from nis_api.handlers.base_handler import BaseHandler
from nis_api.handlers.deploy_handler import DeployHandler
from nis_api.handlers.device_handler import DeviceHandler
from nis_api.handlers.product_handler import ProductHandler
from nis_api.handlers.product_handler import ProductByTemplateHandler
from nis_api.handlers.cabinet_handler import CabinetHandler
from nis_api.handlers.audit_handler import AuditHandler
from nis_api.handlers.admin_handler import AdminHandler
from nis_api.handlers.ui_handler import UiHandler
from nis_api.handlers.inventory_summary_handler import InventorySummaryHandler
from nis_api.handlers.inventory_exclusions_handler import \
    InventoryExclusionsHandler
from nis_api.handlers.configuration_handler import ConfigHandler
from nis_api.handlers.cabinet_details_handler import CabinetDetailsHandler
from nis_api.handlers.cabinet_search_handler import CabinetSearchHandler

import datetime
import os

# this takes the params in a uri such as
# count&datacenter=Ord1
# and returns {'param':count,'datacenter':'Ord1'}
# where param is a method call or you can pass id=1234&datacenter=Ord1
# and that would do specific querying in mongo when the dict gets passed in


class nisapi(object):

    def __init__(self):
        url = str.format(r"/{}", config.version)

        self.header = [
            # (r'/favicon.ico', web.StaticFileHandler,
            # {'path': '/favicon.ico'}),

            # Return documentation
            # Matches the following urls:
            # /, /1.0, /1.0/, /docs, /docs/, /1.0/docs, and /1.0/docs/
            (r'/(?:1\.0/?)?(?:docs/?)?', BaseHandler),

            # Inventory handler
            (url + "/inventory", InventorySummaryHandler),

            # Device handler
            (url + "/devices", DeviceHandler),
            (url + "/devices/(.*)", DeviceHandler),

            # Audit log handler
            (url + "/history", AuditHandler),

            # configuration handler of filter criteria in Device Maintenance UI
            (url + "/ui/config", ConfigHandler),

            # configuration handler for dc navigation on cabinet view UI
            (url + '/ui/config/(.*)', ConfigHandler),

            # Mark devices as allocated and returning their id's
            (url + "/deploy", DeployHandler),

            # Get product using template ID.
            (url + "/products/template/(.*)", ProductByTemplateHandler),

            # Offerings CRUD handler
            (url + "/products", ProductHandler),
            (url + "/products/(.*)", ProductHandler),

            # Cabinets handler
            (url + "/cabinets", CabinetHandler),
            (url + "/cabinets/(.*)", CabinetHandler),

            # Cabinet details for specific cabinet handler UI
            (url + "/ui/cabinets/details", CabinetDetailsHandler),
            (url + "/ui/cabinets/details/(.*)", CabinetDetailsHandler),

            # Cabinet in datacenter handler UI
            (url + "/ui/cabinets/datacenter", CabinetSearchHandler),
            (url + "/ui/cabinets/datacenter/(.*)", CabinetSearchHandler),

            # NIL UI handler
            (url + "/ui/devices", UiHandler),
            (url + "/ui/devices/(.*)", UiHandler),

            # admin handler
            (url + "/admin", AdminHandler),

            # Inventory Exclusion handler
            (url + "/inventoryexclusions", InventoryExclusionsHandler)

        ]

        self.settings = {
            "debug": config.debug_mode,
            "log_function": self.log
        }

    def get_app(self):
        return tornado.web.Application(self.header, **self.settings)

    @staticmethod
    def log(value):
        time_str = str(datetime.datetime.now())
        if hasattr(value, 'error'):
            f = open(config.log_error, 'a+')
            f.write(time_str + ": " + str(value.error) + '\n\n')
        elif isinstance(value, tornado.web.ErrorHandler):
            f = open(config.log_error, 'a+')
            f.write(time_str + ": " + str(value.request) + '\n\n')
        else:
            f = open(config.log, 'a+')
            f.write(time_str + ": " + str(value.request) + '\n\n')

if __name__ == "__main__":
    print("Starting NIS service...")
    print("Port: ", config.tornado['port'])
    print("PID: ", os.getpid())

    application = nisapi().get_app()
    application.listen(config.tornado['port'])
    tornado.ioloop.IOLoop.instance().start()
