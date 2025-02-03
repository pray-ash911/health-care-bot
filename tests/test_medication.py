import unittest
from services.medication_service import add_new_medication, get_all_medications

class TestMedications(unittest.TestCase):
    def test_add_medication(self):
        # Mock test for adding medication
        test_medication = {
            "Username": "test_user",
            "name": "Paracetamol",
            "dose": "500mg",
            "frequency": "Twice a day",
            "time": "08:00 AM"
        }
        add_new_medication(test_medication)
        medications = get_all_medications()
        self.assertIn(test_medication, medications)

if __name__ == "__main__":
    unittest.main()
