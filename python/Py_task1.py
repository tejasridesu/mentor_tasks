rows=[{"user": "amit", "amount":"1200"},{"user": "riya", "amount":""},{"user": "dev", "amount":"900"}]
for row in rows:
    try:
        amount=int(row["amount"])
        print(row['user'],amount)
    except ValueError:
        print("Invalid amount for user",row['user'])
        
