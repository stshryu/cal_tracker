import services.cal_tracker as tracker
import success

def test_create_calorie_intake():
    # Arrange
    name = "testing"
    calorie = "40"
    quantity = "20"

    # Act
    response = tracker.create_calorie_intake(name, calorie, quantity)

    # Assert
    assert type(response) == success.Success 

    cal_tracker = response.unpack()
    assert cal_tracker.name == "testing"
    assert cal_tracker.calorie == 40 
    assert cal_tracker.quantity == 20 

def test_add_calorie_intake():
    # Arrange
