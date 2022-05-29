from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .db import insert_into_db
from .models import CitizenVaccinationData, PreviousConditions


registration_page = """
<html>
    <head>
        <title>Vaccination DB- Registration</title>
    </head>
    <body>
        <form method="post" action="register">
            First name: <input type="text" name="first_name" /><br />
            Last name: <input type="text" name="last_name" /><br />
            Date of birth: <input type="date" name="date_of_birth" /><br />
            Address: <input type="text" name="address" /><br />
            City: <select name="city">
                      <option value="Tel-Aviv">Tel-Aviv</option>
                      <option value="Jerusalem">Jerusalem</option>
                    </select><br />
            Zipcode: <input type="text" name="zipcode" /><br />
            Land line: <input type="text" name="landline" /><br />
            Cellular phone: <input type="text" name="cellphone" /><br />
            Infected? <input type="checkbox" name="infected" value="1" /><br />
            Previous conditions: <br />
            <input type="checkbox" name="previous_conditions.diabetes" value="1" />Diabetes<br />
            <input type="checkbox" name="previous_conditions.cardio_vascular" value="1" />Cardio vascular<br />
            <input type="checkbox" name="previous_conditions.allergies" value="1" />Allergies<br />
            Other: <input type="text" name="previous_conditions.other" /><br />

            <input type="submit" />
        </form>
    </body>
</html>
"""


def is_checkbox_checked(request, checkbox_name):
    return checkbox_name in request.POST


@method_decorator(csrf_exempt, name='dispatch')
def register(request):
    if request.method == "POST":
        try:
            citizen_data = CitizenVaccinationData(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                date_of_birth=request.POST["date_of_birth"],
                address=request.POST["address"],
                city=request.POST["city"],
                zip_code=int(request.POST["zipcode"]),
                land_line=request.POST["landline"],
                cellular_phone=request.POST["cellphone"],
                infected=is_checkbox_checked(request, "infected"),
                previous_conditions=PreviousConditions(
                    diabetes=is_checkbox_checked(request, "previous_conditions.diabetes"),
                    cardio_vascular=is_checkbox_checked(request, "previous_conditions.cardio_vascular"),
                    allergies=is_checkbox_checked(request, "previous_conditions.allergies"),
                    other=request.POST["previous_conditions.other"]
                )
            )

            insert_into_db(citizen_data)
        except Exception as e:
            return HttpResponse("insertion failed: " + str(e), status=500)

        return HttpResponse("inserted citizen data successfully", status=200)

    return HttpResponse(registration_page)
