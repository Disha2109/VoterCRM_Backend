from Backend import db


class Districts(db.Model):
    __tablename__ = "Districts"

    District_Id = db.Column(db.Integer, primary_key = True)
    District_Name = db.Column(db.String(100), unique = True)
    District_No = db.Column(db.Integer, null = False)
    State_Code = db.Column(db.Integer, db.ForeignKey("States.State_Id"))

    def __init__(self, District_Id, District_Name, District_No, State_Code):
        self.District_Id = District_Id
        self.District_Name = District_Name
        self.District_No = District_No
        self.State_Code = State_Code