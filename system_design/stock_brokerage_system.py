"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

An Online Stock Brokerage System facilitates its users the trade (i.e. buying and selling) of stocks online. It allows clients to keep track of and execute their transactions, and shows performance charts of the different stocks in their portfolios. It also provides security for their transactions and alerts them to pre-defined levels of changes in stocks, without the use of any middlemen.

System Requirements
===================

Any user of our system should be able to buy and sell stocks.

Any user can have multiple watchlists containing multiple stock quotes.

Users should be able to place stock trade orders of the following types: 1) market, 2) limit, 3) stop loss and, 4) stop limit.

Users can have multiple ‘lots’ of a stock. This means that if a user has bought a stock multiple times, the system should be able to differentiate between different lots of the same stock.

The system should be able to generate reports for quarterly updates and yearly tax statements.

Users should be able to deposit and withdraw money either via check, wire, or electronic bank transfer.

The system should be able to send notifications whenever trade orders are executed.

Actors
===================
Admin: Mainly responsible for administrative functions like blocking or unblocking members.
Member: All members can search the stock inventory, as well as buy and sell stocks. Members can have multiple watchlists containing multiple stock quotes.
System: Mainly responsible for sending notifications for stock orders and periodically fetching stock quotes from the stock exchange.


Use cases
===================
Register new account/Cancel membership: To add a new member or cancel the membership of an existing member.
Add/Remove/Edit watchlist: To add, remove or modify a watchlist.
Search stock inventory: To search for stocks by their symbols.
Place order: To place a buy or sell order on the stock exchange.
Cancel order: Cancel an already placed order.
Deposit/Withdraw money: Members can deposit or withdraw money via check, wire or electronic bank transfer.
"""

from abc import ABC, abstractmethod
from enum import Enum

class ReturnStatus(Enum):
    SUCCESS, FAIL, INSUFFICIENT_FUNDS, INSUFFICIENT_QUANTITY, NO_STOCK_POSITION = 1, 2, 3, 4, 5, 6


class OrderStatus(Enum):
    OPEN, FILLED, PARTIALLY_FILLED, CANCELLED = 1, 2, 3, 4


class TimeEnforcementType(Enum):
    GOOD_TILL_CANCELLED, FILL_OR_KILL, IMMEDIATE_OR_CANCEL, ON_THE_OPEN, ON_THE_CLOSE = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 5


class Location:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Constants:
    def __init__(self):
        self.__MONEY_TRANSFER_LIMIT = 100000

class Account(ABC):
    def __init__(self, id, password, name, address, email, phone, status=AccountStatus.NONE):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = AccountStatus.NONE

    def reset_password(self):
        None

import datetime

class Member(Account):
    def __init__(self):
        self.__available_funds_for_trading = 0.0
        self.__date_of_membership = datetime.date.today()
        self.__stock_positions = {}
        self.__active_orders = {}

    def place_sell_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
        # check if member has this stock position
        if stock_id not in self.__stock_positions:
            return ReturnStatus.NO_STOCK_POSITION

        stock_position = self.__stock_positions[stock_id]
        # check if the member has enough quantity available to sell
        if stock_position.get_quantity() < quantity:
            return ReturnStatus.INSUFFICIENT_QUANTITY

        order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
        order.is_buy_order = False
        order.save_in_DB()
        success = StockExchange.place_order(order)
        if success:
            order.set_status(OrderStatus.FAILED)
            order.save_in_DB()
        else:
            self.active_orders.add(order.get_order_id(), order)
        return success

    def place_buy_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
        # check if the member has enough funds to buy this stock
        if self.__available_funds_for_trading < quantity * limit_price:
            return ReturnStatus.INSUFFICIENT_FUNDS

        order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
        order.is_buy_order = True
        order.save_in_DB()
        success = StockExchange.place_order(order)
        if not success:
            order.set_status(OrderStatus.FAILED)
            order.save_in_DB()
        else:
            self.active_orders.add(order.get_order_id(), order)
        return success

    # this function will be invoked whenever there is an update from
    # stock exchange against an order
    def callback_stock_exchange(self, order_id, order_parts, status):
        order = self.active_orders[order_id]
        order.add_order_parts(order_parts)
        order.set_status(status)
        order.update_in_DB()

        if status == OrderStatus.FILLED or status == OrderStatus.CANCELLEd:
            self.active_orders.remove(order_id)

from abc import ABC, abstractmethod
import datetime

class Order(ABC):
    def __init__(self, id):
        self.__order_id = id
        self.__is_buy_order = False
        self.__status = OrderStatus.OPEN
        self.__time_enforcement = TimeEnforcementType.ON_THE_OPEN
        self.__creation_time = datetime.datetime.now()

        self.__parts = {}

    def set_status(self, status):
        self.status = status

    def save_in_DB(self):
        pass
    # save in the database

    def add_order_parts(self, parts):
        for part in parts:
            self.parts[part.get_id()] = part


class LimitOrder(Order):
    def __init__(self):
        self.__price_limit = 0.0

class StockExchange:
    # singleton, used for restricting to create only one instance
    instance = None

    class __OnlyOne:
        def __init__(self):
            None

    def __init__(self):
        if not StockExchange.instance:
            StockExchange.instance = StockExchange.__OnlyOne()

    def place_order(self, order):
        return_status = self.get_instance().submit_order(Order)
        return return_status