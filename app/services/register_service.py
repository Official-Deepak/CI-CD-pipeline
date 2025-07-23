from app.utils.common_utils import handle_response

class RegisterService:
    def __init__(self):
        pass
    #Function to add two numbers
    def add_no(self, request_data):
        try:
            num1 = request_data["num1"]
            num2 = request_data["num2"]

            # Type check: must be int or float, not string
            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                return handle_response(
                    status=False,
                    message="Invalid input type",
                    status_code=400
                )

            total = num1 + num2
            data = {"total": total}
            return handle_response(
                status=True,
                message="Addition successful",
                status_code=200,
                data=data
            )
        except KeyError as e:
            return handle_response(
                status=False,
                message=f"Missing field: {e.args[0]}",
                status_code=400
            )
        except Exception as e:
            return handle_response(
                status=False,
                message=str(e),
                status_code=500
            )
    