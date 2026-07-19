from app import db


class Threat(db.Model):
    __tablename__ = "threats"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(50))
    source = db.Column(db.String(100))
    ip_address = db.Column(db.String(50))
    threat_type = db.Column(db.String(100))
    severity = db.Column(db.String(20))
    country = db.Column(db.String(100))
    confidence = db.Column(db.Integer)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Threat {self.ip_address}>"