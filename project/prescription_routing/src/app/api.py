"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
from typing import Optional
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel, Field
import pymongo
from bson.objectid import ObjectId
import uvicorn

DATABASE_URI = "mongodb://localhost:27017"
db = DATABASE_URI + "/pharmacy"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pharmacydb"]
pharmacy_table = mydb["pharmacy"]
orders_table = mydb["orders"]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Pharma routing app"}


class PharmacyReq(BaseModel):
    pharmacyCode: str
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )


class InventoryItem(BaseModel):
    drugCode: str
    drug: str
    cost: float
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )


class Orders(BaseModel):
    orderItems: list


@app.post("/orders")
async def add_order(body: Orders):
    req_body = body.dict()
    orders_table.insert_one(req_body)
    oid = req_body["_id"]
    return {"orderId": str(oid)}


@app.get("/orders/{orderId}")
async def get_order(orderId: str):
    try:
        order = orders_table.find_one({"_id": ObjectId(orderId)}, {"_id": 0})
    except:

        return HTTPException(status_code=404, detail="Order not found")
    if not order:
        return HTTPException(status_code=404, detail="Order not found")
    order["orderId"] = orderId
    return order


@app.get("/routeOrder/{orderId}")
async def route_order(orderId: str):
    try:
        order = orders_table.find_one({"_id": ObjectId(orderId)}, {"_id": 0})
    except:

        return HTTPException(status_code=404, detail="Order not found")
    if not order:
        return HTTPException(status_code=404, detail="Order not found")

    cost, assignments = order_assignment(order)
    routerResponse = {}
    routerResponse["orderId"] = orderId
    routerResponse["totalCost"] = cost
    routerResponse["assignments"] = assignments
    return routerResponse


def order_assignment(order):
    finalTotal = 0
    assignment = {}
    for order_item in order.get("orderItems"):
        details = get_cheapest_drug(order_item.get("drugCode"), True)
        totalCost = order_item.get("quantity") * details.get("cost")
        finalTotal += totalCost

        lst = assignment.setdefault(details.get("pharmacyCode"), [])
        assignmentItem = {"drug": order_item.get("drugCode"),
                          "quantity": order_item.get("quantity"),
                          "totalCost": totalCost
                          }
        lst.append(assignmentItem)
    return finalTotal, assignment


@app.post("/pharmacy")
async def pharmacy_add(body: PharmacyReq):
    req_body = body.__dict__
    req_body["pharmacyCode"] = req_body.get("pharmacyCode").upper()
    req_body["inventory"] = []
    pharmacy_table.insert_one(req_body)
    del req_body["_id"]
    return req_body


@app.get("/pharmacy/{pharmacyCode}")
async def pharmacy_add(pharmacyCode: str):
    resp = pharmacy_table.find_one({"pharmacyCode": pharmacyCode.upper()}, {'_id': False})
    return resp


@app.post("/pharmacy/{pharmacyCode}/inventory")
async def add_drug_to_pharmacy(body: InventoryItem, pharmacyCode: str):
    body = body.dict()
    body["pharmacyCode"] = pharmacyCode
    resp = pharmacy_table.find_one({"pharmacyCode": pharmacyCode.upper()})
    existing = resp.get("inventory")
    if body not in existing:
        existing.append(body)
    pharmacy_table.replace_one({"_id": resp.get("_id")}, resp)
    return existing


def get_cheapest_drug(drugCode: str, cheapest):
    filtered_list = list()
    all = pharmacy_table.find({"inventory.drugCode": drugCode.upper()}, {'inventory': True, "_id": False})
    for e in all:
        l = e.get("inventory")
        for drug in l:
            if drug.get("drugCode") == drugCode:
                filtered_list.append(drug)

    if not filtered_list:
        return []

    if cheapest:
        filtered_list.sort(key=lambda x: x["cost"])
        return filtered_list[0]
    return filtered_list


@app.get("/drug/{drugId}")
async def pharmacy_add(drugId: str, cheapest: Optional[bool] = False):
    return get_cheapest_drug(drugId, cheapest)


@app.get("/")
async def root():
    return {"message": "Welcome to Pharma routing app"}


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
