from Backend import db


class AssemblyConstituency(db.Model):
    __tablename__ = "AssemblyConstituency"

    Constituency_Id = db.Column(db.Integer, primary_key = True)
    Constituency_Name = db.Column(db.String(100), unique = True, null=False)
    Constituency_No = db.Column(db.Integer, null = False)
    District_Code = db.Column(db.Integer, db.ForeignKey("Districts.District_Id"), null=False)

    def __init__(self, Constituency_Id, Constituency_Name, Constituency_No, District_Code):
        self.Constituency_Id = Constituency_Id
        self.Constituency_Name = Constituency_Name
        self.Constituency_No = Constituency_No
        self.District_Code = District_Code