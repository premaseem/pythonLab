## Instruction to run the project 
cd to app file ( ie cd prescription_routing/src)
Run command to run fast api server
> uvicorn app:app --reload

### Interactive api docs
http://127.0.0.1:8000/docs

### Test with curl call 
```
curl --location --request GET 'http://127.0.0.1:8000/routeOrder/602209b6f5d88d2527f6761b' \
--header 'Content-Type: application/json' \
--data-raw '{
    "orderItems": [
        {
            "drugCode": "PEN",
            "quantity": 2
        },
        {
            "drugCode": "ASP",
            "quantity": 5
        },
        {
            "drugCode": "DIS",
            "quantity": 1
        }
    ]
}'
```
Sample response in Json
```
{
    "orderId": "602209b6f5d88d2527f6761b",
    "totalCost": 128.8,
    "assignments": {
        "PREM": [
            {
                "drug": "PEN",
                "quantity": 2,
                "totalCost": 1.8
            }
        ],
        "WG": [
            {
                "drug": "ASP",
                "quantity": 5,
                "totalCost": 56.5
            },
            {
                "drug": "DIS",
                "quantity": 1,
                "totalCost": 1.5
            }
        ],
        "CVS": [
            {
                "drug": "VIAGRA",
                "quantity": 1,
                "totalCost": 69.0
            }
        ]
    }
}

```

