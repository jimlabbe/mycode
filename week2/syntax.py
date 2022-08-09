response_code = 400
match response_code:
    case 200:
        print("moving!")
    case 400:
        print("getting!")
